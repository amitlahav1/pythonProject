class Animal:
    def __init__(self,name_animal:str):
        self.name_animal=name_animal
        if type(name_animal)!=str:
            raise TypeError("name numst to be type str!")
        self.energy=5
        self.hunger=5
    def __str__(self):
        return (f"name animal:{self.name_animal},level hunger:{self.hunger},level energy:{self.energy}")

    def eat(self,food:int):
        if type(food)!=int:
            food=0
        if food<0:
            food=0
        sum_hunger_down=food/50
        if sum_hunger_down>self.hunger:
            sum_hunger_down=self.hunger
            food=self.hunger*50
        self.hunger-=sum_hunger_down
        if self.hunger<0:
            self.hunger=0
            print("the animal not finish the food. she full.")
        sum_energy_down=food/100
        self.energy-=sum_energy_down
        if self.energy<0:
            self.energy=0

    def play(self,time_play):
        if type(time_play)!=int:
            time_play=0
        if time_play<0:
            time_play=0

        sum_energy_down=time_play/10 * 2
        self.energy-=sum_energy_down
        if self.energy<0:
            self.energy=0
            print("the animal want to rest!")
        if sum_energy_down>self.energy:
            time_play=self.energy
        sum_up_hunger=time_play/10 * 2
        self.hunger+=sum_up_hunger
        if self.hunger>10:
            self.hunger=10


    def rest(self,time_rest):
        if type(time_rest)!=int:
            time_rest=0
        if time_rest<0:
            time_rest=0

        up_energy=time_rest/20
        x = 10 - self.energy
        self.energy+=up_energy
        if self.energy>10:
            self.energy=10
            print("finish rest. want play!")
        if up_energy>x:
            time_rest=x*20
        up_hunger=time_rest/30
        self.hunger+=up_hunger
        if self.hunger>10:
            self.hunger=10
            print("finish rest. want eat!!!!")







