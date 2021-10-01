import re

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
mess = "F7C6C18FCCC76C0FC0838FC3C64E1428DA8FCD4E150EC18FCC6C1C8FDBC74E142C8FCBCACCDDD6DFDB8F6B3E691F4E140CCC8FECFBE9D4FAFBE99782E2EEF682FCECFD9CF882F69FFAD28FC4C76C1BC1C88FC1C74E142690A5"
# mess = "080b0a0d0c0f0e010009585b5a" # test -> 1234567890abc
cipher = [mess[i : i + 2] for i in range(0, len(mess), 2)]

print(cipher)


def test_ctf(mystring):
    if re.search(r"CTF", mystring, flags=re.IGNORECASE):
        return True
    return False


def decrypt(byte_message, key):
    result = []
    for text in byte_message:
        current: int = int(text, 16) ^ key
        ans = chr(current)
        result.append(ans)
    final = "".join(result)
    if test_ctf(final):
        print("found key: ", key)
        return final
    return


for i in range(256):
    ans = decrypt(cipher, i)
    if ans is not None:
        print(ans)
