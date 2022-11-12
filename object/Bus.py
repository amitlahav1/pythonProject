class Bus:
    def __init__(self, number_seats):
        self.number_seats = number_seats
        self.list_seats = []
        for i in range(number_seats):
            self.list_seats.append("free")

    def geton(self, name_passenger):
        if "free" in self.list_seats:
            self.list_seats.remove("free")
            self.list_seats.append(name_passenger)
        else:
            print(f" sorry no place in the bus, {name_passenger} - He didn't get on the bus")

    def getoff(self, name_passenge_off):
        if name_passenge_off in self.list_seats:
            place = self.list_seats.index(name_passenge_off)
            self.list_seats[place] = "free"
        else:

            print(f"the passenger-{name_passenge_off} not in the bus!")

    def __str__(self):
        return f"the number of seats in the bus: {self.number_seats}, the list of passenger is:{self.list_seats}"


number_seat = int(input("enter number of seats to the bus:"))
BUS1 = Bus(number_seat)
print("if you want to get on passenger press - 1")
print("if you want to get off passenger press - 2")
print("if you want to finish press - 0")
num_press = int(input("enter your choice 1 or 2 or 0:"))
while num_press != 0:
    name1 = (input("enter name of passenger - get on:"))
    if num_press == 1:
        BUS1.geton(name1)
    elif num_press == 2:
        BUS1.getoff(name1)
    else:
        print("enter again , 1 or 2 , or 0")

    num_press = int(input("enter your choice 1 or 2 or 0:"))
print(BUS1)
