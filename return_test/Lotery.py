from random import randint

class Lottery:
    def __init__(self):
        self.list_numbers= self.numbers()
        self.sum_winner= self.amount()
        self.lower=1
        self.high=45

    def numbers(self):
        for i in range(6):
            num=randint(self.lower,self.high)
            self.list_numbers.append(num)
    def amount(self):
        num=int(input("enter max amount:"))
        return num

    def __str__(self):
        return f"the numbers:{self.list_numbers}"

    def guss(self,num):
        if num in self.list_numbers:
            return True
        else:
            return False
    def num_guess(self,num):
        amount_win=0
        if num<=1:
            amount_win=0
            return amount_win
        elif num>2 and num<=5:
            amount_win=(num*self.sum_winner)/6
            return amount_win
        elif num==6:
            amount_win=self.sum_winner
            return amount_win


Loto1 = Lottery()
print(Loto1)
count=0
for i in range(6):
    gusses=int(input("enter guss 1-45"))
    if Loto1.guss(gusses):
        count+=1

print(Loto1.num_guess(count))





