import requests
from lxml import html
import json


SERVER_URL = "http://178.128.19.56:17789"


def get_content(site_path: str):
    url = SERVER_URL + site_path
    res = requests.get(url)
    tree = html.fromstring(res.content)
    contents = tree.xpath('//div[@class]/a[@class="anchor"]/text()')
    return contents


def map_directory(path: str):
    path_list = list(filter(len, path.split("/")))
    if len(path_list) == 0:
        last_node = "/"
    else:
        last_node = path_list[-1]
    node_structure_dict = {}

    contents: list[str] = get_content(path)
    contents = [node_.strip() for node_ in contents]

    # find flag
    if "flag.txt" in contents:
        raise Exception(f"Flag found, path is {path}")

    # node is empty
    if len(contents) == 0:
        node_structure_dict[last_node] = ""

    # map next node
    for node in contents:
        if path == "/":
            next_path = path + node
        else:
            next_path = path + "/" + node
        node_structure_dict[node] = map_directory(next_path)
    return node_structure_dict


print(json.dumps(map_directory("/")))  # for testing purpose
