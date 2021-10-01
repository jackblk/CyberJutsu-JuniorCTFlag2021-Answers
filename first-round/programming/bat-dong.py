with open("bai-van-1.txt", "r") as f:
    van1 = f.read()
    van1_ = list(van1)

with open("bai-van-2.txt", "r") as f:
    van2 = f.read()
    van2_ = list(van2)

for i in range(len(van1)):
    if van1_[i] != van2_[i]:
        print(van2_[i], end="")
