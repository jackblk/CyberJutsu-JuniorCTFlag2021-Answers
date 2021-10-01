#!/usr/bin/python3
import socket
import json
import struct
import logging


class KidServer:
    def __init__(self, host, port):
        # Khởi tạo UDP socket và lắng nghe kết nối
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.host = host
        self.port = port

    # Gửi phản hồi về cho client
    def response(self, data):
        self.socket.sendto(data, (self.host, self.port))
        return self.socket.recv(1024)


class KidPacket:
    def __init__(self, rawPacket):
        self.parse(rawPacket)

    # Hàm xử lý / kiểm tra cấu trúc gói tin
    def parse(self, rawPacket):
        #
        #   Dòng code bên dưới đang chuyển đổi 2 bytes đầu của gói tin
        # từ dạng little endian về dạng số, đây là phần contentLength.
        # Em có thể tìm hiểu thêm hàm struct.pack(), nó sẽ giúp em
        # chuyển đổi theo chiều ngược lại.
        #
        self.contentLength = struct.unpack("<H", rawPacket[0:2])[0]

        # Các bytes còn lại của gói tin được xem là phần dữ liệu
        data = rawPacket[2:]

        if self.contentLength != len(data):
            raise Exception("Bad content-length")

        # Chuyển đổi dữ liệu nhận được thành JSON object
        try:
            self.body = json.loads(data)
        except:
            raise Exception("Bad format")
def encode(data):
    json_data = json.dumps(data)
    length = struct.pack("<H", len(json_data))
    # print(length, len(length))
    final = length + bytes(json_data, encoding="utf8")
    # print(len(final))
    return final


def main():
    # Khởi tạo server lắng nghe trên 0.0.0.0:3108
    server = KidServer("178.128.19.56", 3108)
    data = {"action":"read", "file":"flag.txt"}
    stream_byte = encode(data)
    print(stream_byte)
    print(KidPacket(stream_byte).body)
    resp = server.response(stream_byte)
    print(str(resp))



main()