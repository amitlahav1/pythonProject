class Hard_Disk:
    def __init__(self,size_disk,flie_list):
        self.size_hardDisk=size_disk
        self.flie_list={}                               #key=name , val=size of flie

    def used_space(self,):
        return sum(self.flie_list.values())

    def free_space(self):
        return self.size_hardDisk-self.used_space()

    def add_flie(self, name_flie, size_flie):
        if name_flie in self.flie_list:
            print("the name Exists, sorry")
            return False

        if self.free_space()>=size_flie>0:
            self.flie_list.update({name_flie:size_flie})
            return True
        else:
            print("not have place in the hard disk , sorry")
            return False

    def del_flie(self,name_flie):
        if name_flie in self.flie_list:
            del self.flie_list[name_flie]
            return True
        else:
            print("the name not exists")
            return False

    def update_flie(self,new_name,new_size):
        if new_name in self.flie_list and self.free_space()<new_size:
            self.flie_list.update({new_size:new_size})
            return True
        else:
            print("the name not exists")
            return False

    def __str__(self):
        return (f"the size of hard Disk is:{self.size_hardDisk}, the list of flies is:{self.flie_list},free space:{self.free_space()}")




size_hardDisk=int(input("enter a size of hard disk:"))
list={}

hardDisk1=Hard_Disk(size_hardDisk,list)
print(hardDisk1)

name_flie=input("enter name of flie 1:")
size_flie=int(input("enter size of the flie 1:"))

hardDisk1.add_flie(name_flie,size_flie)

print(hardDisk1)

name2=input("enter name of flie 2:")
size2=int(input("enter size to flie 2:"))
hardDisk1.add_flie(name2,size2)
print(hardDisk1)



print(hardDisk1.used_space(),"used space")
print(hardDisk1.free_space(),"free sapce")
