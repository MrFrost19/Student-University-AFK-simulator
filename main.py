import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.cash = 50
        self.alive = True

    def to_study(self):
        print(f"{self.name} is going to study")
        self.progress += 0.15
        self.gladness -= 3

    def to_sleep(self):
        print(f"{self.name} will sleep!")
        self.gladness += 3

    def to_chill(self):
        print(f"{self.name} will chill")
        self.cash -= 15
        self.gladness += 5
        self.progress -= 0.1

    def to_work(self):
        print(f"{self.name} is going to work!")
        self.cash += 20
        self.gladness -= 3

    def is_alive(self):
        if self.progress < -0.5:
            print(f"{self.name} has been casted out by director...")
            self.alive = False
        elif self.gladness <= 0:
            print(f"{self.name} has got Depression...")
            self.alive = False
        elif self.progress > 6:
            print(f"{self.name} passed externally")
            self.alive = False
        elif self.cash <= 0:
            print(f"{self.name} is poor now...")
            self.alive = False
        elif i == 365:
            print(f"Time out {self.name} didn't make it")

    def end_of_day(self):
        print(" ")
        print("STATS")
        print(" ")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 1)}")
        print(f"Money = {self.cash}")

    def live(self, day):
        d = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        if self.cash <= 40:
            print(f"{self.name} needs some money")
            self.to_work()
            self.end_of_day()
            self.is_alive()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                work_or_no = random.randint(1, 2)
                if work_or_no == 1:
                    print(f"{self.name} decided to work")
                    self.to_work()
                else:
                    print(f"{self.name} decided to not work now")
            self.end_of_day()
            self.is_alive()


name = input("Input name ")
nick = Student(name=name)
for i in range(1, 366):
    if nick.alive == False:
        break
    nick.live(i)