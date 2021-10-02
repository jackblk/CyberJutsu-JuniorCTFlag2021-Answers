#!/usr/bin/python3
import socket
import re
import base64
import io
from PIL import Image


IP, PORT = ("178.128.19.56", 19999)

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


def index_of_coordinate(img: Image.Image, x, y):
    # index = width*y + x # https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
    width = img.size[0]
    return width * y + x


def solve(img: Image.Image, x, y):
    width = img.size[0]
    height = img.size[1]
    if x < width / 2 and y < height / 2:
        return 2
    if x > width / 2 and y < height / 2:
        return 1
    if x < width / 2 and y > height / 2:
        return 3
    if x > width / 2 and y > height / 2:
        return 4
    raise Exception("Something went wrong.")


def main():
    # Tạo một socket và kết nối đến server
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((IP, PORT))

    while True:
        challenge = receive_one_line(socket_)
        print(challenge)

        # Accept challenge
        if "y/n" in challenge:
            send_one_line(socket_, "y")

        # Skip all except for the image
        keyword_search = re.search(r"Length: (\d+)", challenge)
        if keyword_search is None:
            continue

        # Catch the image and solve
        img_string = receive_one_line(socket_)
        img_data = base64.b64decode(img_string)

        # with open("mario-test.png", "wb+") as f:  # for testing
        #     f.write(img_data)

        img = Image.open(io.BytesIO(img_data))
        # https://stackoverflow.com/questions/49720605/pixel-coordinates-vs-drawing-coordinates
        pixel_coordinates = list(img.getdata())

        width = img.size[0]
        height = img.size[1]

        ans = 0
        for x in range(width):
            for y in range(height):
                color = sum(pixel_coordinates[index_of_coordinate(img, x, y)])
                if color == 0:
                    continue
                ans = solve(img, x, y)
                break
            else:
                continue
            break

        print(f"Ans: {ans}")
        send_one_line(socket_, str(ans))

    # Các bạn đừng ngần ngại mà chạy file python này.
    # Hãy cố gắng tìm hiểu cách giao tiếp với máy chủ thông qua socket tại đây nhé,
    # Tắt connection đến server
    socket_.close()


if __name__ == "__main__":
    main()
