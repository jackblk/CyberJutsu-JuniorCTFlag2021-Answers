#!/usr/bin/python3
import socket
import re

# Địa chỉ IP và port của server
IP, PORT = ("178.128.19.56", 20001)

# Hàm này nhận một dòng (line) từ socket
def receive_one_line(socket_):
    result = b""

    # Lần lượt nhận từng ký tự, nếu là ký tự xuống dòng thì ngưng
    while True:
        t = socket_.recv(1)
        if t == b"\n":
            break
        result = result + t

    # Trả về kết quả dạng string
    return result.decode()


# Hàm này gửi một dòng (line) đến socket
def send_one_line(s, data):
    # Bỏ hết ký tự xuống dòng trong data (nếu có) và gửi đến server
    data = data.strip()
    s.send((data + "\n").encode())


def main():
    # Tạo một socket và kết nối đến server
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((IP, PORT))

    # Nhận và in dòng đầu mà server trả về
    banner = receive_one_line(socket_)
    print(banner)
    for i in range(6):
        print(f"Challenge {i}")
        challenge = receive_one_line(socket_)
        print(challenge)
        ans = re.search(r"số (\d+) ", challenge)
        if ans is None:
            continue
        ans = ans.group(1)
        print(ans)
        send_one_line(socket_, ans)

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    socket_.close()


if __name__ == "__main__":
    main()
