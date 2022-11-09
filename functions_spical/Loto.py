class Loto:
    def __init__(self):
        self.numbers = self.list_number()
        self.max_win = self.sum_maxwin()


    def list_number(self):
        from random import randint
        list1 = []
        for i in range(6):
            number = randint(1, 45)
            list1.append(number)
        return list1

    def sum_maxwin(self):
        sum_win=int(input("enter winning amount: "))
        return sum_win

    def __str__(self):
        return f"the list of number is {self.numbers}"

    def guess(self,num_guess):
        if num_guess in self.numbers:
            return True
        else:
            return False


    def sum_win_user(self,succses_guess):
        amount_win=0
        if succses_guess<=1:
            return amount_win
        if succses_guess>=2 and succses_guess<=5:
            amount_win=(succses_guess*self.max_win)/6
            return amount_win
        if succses_guess==6:
            amount_win=self.max_win
            return amount_win

Loto1=Loto()
print(Loto1)


succses_guess=0
for i in range (6):
    guess_num = int(input("enter your guess -number 1-45:"))
    if guess_num>=1 and guess_num<=45:

        if Loto1.guess(guess_num):
            print("success guess")
            succses_guess+=1

    else:
        print("invalid number ! GAME OVER.")
        succses_guess==0
        break

    print(Loto1.sum_win_user(succses_guess), "this your amount!")







