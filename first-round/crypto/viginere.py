alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plain = list("HELLOWORLDCRYPTOGRAPHERS")
cipher = list("HRNTSJHTTSJVPHTFKRWTZSDW")

dict_ = {}
for i in range(0, len(alphabet)):
    dict_[alphabet[i]] = i

print(dict_)
inv_dict = {v: k for k, v in dict_.items()}
print(inv_dict)

key = []
# kn=cn−pn mod 26
# https://crypto.stackexchange.com/questions/12195/find-the-key-to-a-vigen%C3%A8re-cipher-given-known-ciphertext-and-plaintext
for i in range(0, len(cipher)):
    key.append(inv_dict[(dict_[cipher[i]] - dict_[plain[i]]) % len(alphabet)])

print("".join(key))
