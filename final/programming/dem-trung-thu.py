#!/usr/bin/python3
import time
import socket
import re

# Địa chỉ IP và port của server
IP, PORT = ("178.128.19.56", 23444)

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


class Party:
    def __init__(self) -> None:
        self.possible_target_list = list(range(0, 40))
        self.current_target = -1
        self.ans = -1

    def to_new_target(self):
        self.current_target = self.possible_target_list[0]
        self.not_target(self.current_target)

    def not_target(self, id):
        try:
            self.possible_target_list.remove(id)
        except ValueError:
            pass


def try_person(socket_: socket.socket, party: Party, guest_list):
    for guest in guest_list:
        # go to guest
        # print(guest)
        send_one_line(socket_, str(guest))
        reply = receive_one_line(socket_)
        # print(reply)
        # ask if guest knows the person
        ask_mess = f"0 {party.current_target}"
        # print(ask_mess)
        send_one_line(socket_, str(ask_mess))
        reply = receive_one_line(socket_)
        # print(reply)

        # if "no" then the target is not the one
        if "không" in reply:
            return False
        # if "yes" then the guest is not the one too
        reply = receive_one_line(socket_)
        # print(reply)
        party.not_target(guest)
        continue
    return True


def main():
    # Tạo một socket và kết nối đến server
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((IP, PORT))
    party = Party()

    # Nhận và in dòng đầu mà server trả về
    while True:
        challenge = receive_one_line(socket_)

        if "buổi tiệc CyberKid lần thứ" in challenge:
            # reset, for next party
            party = Party()

        if "Hãy nhập số thứ tự" not in challenge:
            print(challenge)
            continue
        # print("---------------")
        # print(challenge)

        ###### IMPLEMENT HERE
        # try a person, remove him from the possible target list
        party.to_new_target()
        person_to_try = party.current_target

        # from a guest list
        guest_list = list(range(0, 40))
        guest_list.remove(person_to_try)

        # try if the person is the target
        result = try_person(socket_, party, guest_list)

        if result:
            print(f"Person {person_to_try} IS the one.")
            ans = person_to_try
        else:
            print(f"Person {person_to_try} is NOT the one.")
            continue

        ###### ANSWER
        send_one_line(socket_, str(ans))
        reply = receive_one_line(socket_)
        print(reply)
        send_one_line(socket_, str(1))
        reply = receive_one_line(socket_)
        print(reply)
        reply = receive_one_line(socket_)
        print(reply)

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    socket_.close()


if __name__ == "__main__":
    main()
