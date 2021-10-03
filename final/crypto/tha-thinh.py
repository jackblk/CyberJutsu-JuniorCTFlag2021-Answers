#!/usr/bin/python3
import time
import socket
import re
import random

# Địa chỉ IP và port của server
IP, PORT = ("178.128.19.56", 25555)

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


def find_original_seed(user_id: int):
    anchor = int(time.time() * 256)
    for test_seed in range(anchor - 1000, anchor + 1000):
        random.seed(test_seed)
        test_id = random.randint(1000000, 9999999)
        if test_id == user_id:
            return test_seed
    raise Exception("Cannot find seed")


# original code to shuffle
def shuffle(arr: list):
    res = []
    while len(arr) > 0:
        randIndex = random.randint(0, len(arr) - 1)
        res.append(arr[randIndex])
        arr.pop(randIndex)
    return res


def get_fish():
    arr = [1, 0, 0]  # vàng, mập, cơm
    return shuffle(arr)


def main():
    # Tạo một socket và kết nối đến server
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((IP, PORT))

    # Nhận và in dòng đầu mà server trả về
    banner = receive_one_line(socket_)
    print(banner)

    # # list of correct answers
    # ans_list = []
    while True:
        challenge = receive_one_line(socket_)
        print(challenge)
        if id_check_regex := re.search(r"id = (\d+)", challenge):
            user_id = int(id_check_regex.group(1))
            seed = find_original_seed(user_id)
        else:
            continue

        # sync the seed with server
        random.seed(seed)
        assert user_id == random.randint(1000000, 9999999)

        # create list of answer
        ans_list = []
        for turn in range(0, 60):
            fish_list = get_fish()
            ans_list.append(fish_list.index(1) + 1)  # bait = index + 1
        for turn in range(0, 60):
            send_one_line(socket_, str(ans_list[turn]))
            reply = receive_one_line(socket_)
            print(reply)

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    socket_.close()


if __name__ == "__main__":
    main()
