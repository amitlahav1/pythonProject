class Animal:
    def __init__(self,animal_name):
        self.name=animal_name
        self.hunger=5
        self.energy=5

    def __str__(self):
        return f"the name of animal is: {self.name}, the level of hunger is: {self.hunger}, the level of energy is :{self.energy}"

    def eat(self,volume_food_gr):
        if self.hunger<volume_food_gr/50:
            volume_food_gr=self.hunger*50
            print(f"the animal dont want to eat more, she not finish the food, she ate only : {volume_food_gr} grm")

        sum_down_hunger=volume_food_gr/50
        self.hunger=self.hunger-sum_down_hunger
        sum_down_energy=volume_food_gr/100
        self.energy=self.energy-sum_down_energy
        if self.hunger<0:
            self.hunger=0


    def play(self,time_game):
        if self.energy<time_game*0.2:
            time_game=self.energy/0.2
            print(f"the animal too tired she play: {time_game} minutes")

        self.energy-=time_game*0.2
        self.hunger+=time_game*0.2

        if self.energy>10:
            self.energy=10
        if self.hunger<0:
            self.hunger=0


    def rest(self,time_rest):
        self.energy+=time_rest/20
        self.hunger+=time_rest/30
        if self.energy>10:
            self.energy=10
            time_rest=(10-self.energy)*20
            print("the animal finish rest she rest ,she want to play!, she rest:",{time_rest})
        if self.hunger<10:
            self.hunger=10
            time_rest=(10-self.hunger)*30
            print("the animal finish to rest , she want to eat! she rest:", {time_rest})


name_animal=input("enter a name to your animal:")
Animal1=Animal(name_animal)
print("you have 4 options :\nto feed animal press - 1\nto play press- 2\nto rest press- 3\nto finish program press - 0")
num=int(input("enter your action:"))

while num!= 0:
    if num==1:
        food=int(input("enter a how much grm in this food:"))
        Animal1.eat(food)

    if num==2:
        play=int(input("enter time in minutes of play"))
        Animal1.play(play)

    if num==3:
        rest=int(input("enter time of rest in minutes:"))
        Animal1.rest(rest)

    else:
        print("enter again valid number : 1,2,3 or o to finish program")
        print(Animal1)

    num = int(input("enter your action:"))

print(Animal1)


















