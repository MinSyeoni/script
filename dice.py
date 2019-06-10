import random

class Dice:
    def rollDie(self):
        self.roll = random.randint(1,6) #[1:6] 랜덤 정수
    def getRoll(self):
        return self.roll