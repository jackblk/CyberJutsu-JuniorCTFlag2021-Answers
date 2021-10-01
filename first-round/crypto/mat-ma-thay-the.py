plain = list("HELLO WHAT ARE YOU DOING".strip(" "))
cipher = list("PYZZC SPFK FEY JCQ ACBHX".strip(" "))
target = list("DKWKPBGSFGQGYABHSFE")

dict_ = {}
for i in range(0, len(plain)):
    dict_[cipher[i]] = plain[i]

print(dict_)
# inv_dict = {v: k for k, v in dict_.items()}
# print(inv_dict)

key = []
for i in range(0, len(target)):
    ans = dict_.get(target[i], "x")
    print(ans, end="")
