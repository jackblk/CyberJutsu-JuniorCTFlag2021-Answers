#!/usr/bin/python3
import socket
import re

# Địa chỉ IP và port của server
IP, PORT = ("178.128.19.56", 9797)

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


def convert_num(num, base, target_base):
    num = int(num, base=base)
    if target_base == 2:
        return format(num, "b")
    elif target_base == 8:
        return format(num, "o")
    elif target_base == 10:
        return num
    elif target_base == 16:
        return format(num, "x")
    else:
        raise


def main():
    # Tạo một socket và kết nối đến server
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((IP, PORT))

    # Nhận và in dòng đầu mà server trả về
    banner = receive_one_line(socket_)
    print(banner)
    for i in range(102):
        challenge = receive_one_line(socket_)
        print(challenge)
        resp = re.search(r"chuyển ([\d\D]+) từ hệ-(\d+) sang hệ-(\d+)", challenge)
        if resp is None:
            print("skip")
            continue
        num = resp.group(1)
        base = int(resp.group(2))
        target = int(resp.group(3))
        print(num, base, target)
        ans = convert_num(num, base, target)
        print(ans)
        send_one_line(socket_, str(ans))

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    socket_.close()


if __name__ == "__main__":
    main()
