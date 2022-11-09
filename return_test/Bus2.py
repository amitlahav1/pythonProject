class Bus:
    def __init__(self,number_seat):
        self.number_seats=number_seat
        self.list_seat=[]
        for i in range(number_seat):
            self.list_seat.append("free")
        self.num_passenger=0
    def __str__(self):
        return f"number set in bus:{self.number_seats},number passengers:{self.num_passenger} all the list:{self.list_seat}"
    def get_on(self,name):
        if "free" in self.list_seat:
            index=self.list_seat.index("free")
            self.list_seat[index]=(name)
            self.num_passenger+=1
        else:
            print(f"to {name} no place at Bus")

    def get_off(self,name):
        if name in self.list_seat:
            self.number_seats-=1
            self.list_seat.remove(name)
            self.list_seat.append("free")
        else:
            print(f"sorry {name} not in Bus")


number_seat = int(input("enter number of seats to the bus:"))
BUS1 = Bus(number_seat)
print("if you want to get on passenger press - 1")
print("if you want to get off passenger press - 2")
print("if you want to finish press - 0")
num_press = int(input("enter your choice 1 or 2 or 0:"))

while num_press!=0:
    name1 = (input("enter name of passenger - get on:"))
    if num_press == 1:
        BUS1.get_on(name1)
    elif num_press == 2:
        BUS1.get_off(name1)
    else:
        print("enter again , 1 or 2 , or 0")

    num_press = int(input("enter your choice 1 or 2 or 0:"))
print(BUS1)
