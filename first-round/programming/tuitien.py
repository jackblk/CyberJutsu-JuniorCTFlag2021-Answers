#!/usr/bin/python3
import time
import socket
import re

# Địa chỉ IP và port của server
IP, PORT = ("178.128.19.56", 20002)

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


class MoneyBag:
    def __init__(self, bag):
        self.bag = bag
        self.memo = {}

    def choose_bag(self, i, j):
        # bag is an array from i to j
        # T[i,j]
        # Max{
        #   (Ti +
        #       Min{T[i+2, j], T[i+1, j-1]}
        #   ),
        #   (Tj +
        #       Min{T[i, Tj-2], T[i+1, j-1]}
        #   )
        # }
        try:
            return self.memo[(i, j)]
        except KeyError:
            pass
        if i == j:
            self.memo[(i, j)] = (self.bag[i], 0)
            return self.memo[(i, j)]
        if j == i + 1:
            if self.bag[i] > self.bag[j]:
                self.memo[(i, j)] = (self.bag[i], 0)
                return self.memo[(i, j)]
            else:
                self.memo[(i, j)] = (self.bag[j], 1)
                return self.memo[(i, j)]
        cal1 = self.bag[i] + min(
            self.choose_bag(i + 2, j)[0], self.choose_bag(i + 1, j - 1)[0]
        )
        cal2 = self.bag[j] + min(
            self.choose_bag(i, j - 2)[0], self.choose_bag(i + 1, j - 1)[0]
        )
        if cal1 > cal2:
            self.memo[(i, j)] = (cal1, 0)
            return self.memo[(i, j)]
        else:
            self.memo[(i, j)] = (cal2, 1)
            return self.memo[(i, j)]


def main():
    # Tạo một socket và kết nối đến server
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((IP, PORT))

    # Nhận và in dòng đầu mà server trả về
    banner = receive_one_line(socket_)
    print(banner)
    while True:
        challenge = receive_one_line(socket_)
        print(challenge)
        if re.search(r"Bạn đã", challenge):
            print("\n")
        resp = re.search(r"\[([\d ]+)\]", challenge)
        if resp is None:
            continue
        bag = resp.group(1).split(" ")
        bag = [int(x) for x in bag]
        print(bag)
        start_time = time.time()
        chooser = MoneyBag(bag)
        money, ans = chooser.choose_bag(0, len(bag) - 1)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(f"Chọn {ans} - {money}.", end=" ")
        send_one_line(socket_, str(ans))

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    socket_.close()


if __name__ == "__main__":
    main()
