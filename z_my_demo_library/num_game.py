import random

random_num = random.randint(1, 20)
time = 0
while time < 5:
    num = int(input("请输入你的数字:"))
    if num == random_num:
        break;
    elif num < random_num:
        print("小")
    else:
        print("大")
    time = time + 1
if time < 5:
    print("恭喜!你赢了^_^.")
else:
    print("别灰心，再来一次你可以的^_^")
