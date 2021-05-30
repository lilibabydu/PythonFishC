score = input("请输入你的分数：")
score = int(score)


if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")
elif score == 180:
    print("SSS++")
else:
    print("请输入 0～180 之间的分值")