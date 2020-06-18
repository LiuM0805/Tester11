# 自行车
class Bike:
    def run(self, km):
        print(f"骑行的里程数为：{km}")


# 电动车
class DianBike(Bike):
    # 电量
    def __init__(self, dianchi):
        self.dianchi = dianchi

    # 充电
    def fill_charge(self, vol):
        print(f"充电：{vol}")

    # 计算行程
    def run(self, km):
        max_mile = self.dianchi * 10
        lc = km - max_mile
        if lc > 0:
            print(f"已使用的里数为:{max_mile}")
            # super（）调用父类的方法
            super().run(lc)
        else:
            print(f"骑行的里程数:{km}")


if __name__ == "__main__":
    p = int(input("请输入电量:"))
    b = int(input("请输入里程数:"))
    myeb = DianBike(p)
    myeb.run(b)
