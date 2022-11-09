class Hard_disk:
    def __init__(self,size_disk:int):
        self.size_disk=size_disk
        if self.size_disk!=int:
            raise TypeError("size of disk must to be type int!!!")
        if self.size_disk<=0:
            self.size_disk=10
        self.dic_flie={}

    def __str__(self):
        return (f"size disk:{self.size_disk},the flie in disk:{self.dic_flie}")

    def used_space(self):
        use_space=sum(self.dic_flie.values())
        return use_space

    def free_space(self):
        free_space=self.size_disk-self.used_space()
        return free_space

    def add_flie(self,name_flie,size_flie):
        if size_flie<=self.free_space() and name_flie not in self.dic_flie:
            self.dic_flie.update({name_flie:size_flie})
            return True
        if size_flie>self.free_space():
            print("no have space in disk")
            return False
        if name_flie in self.dic_flie:
            print ("the name exist!")
            return False

    def del_flie(self,name_flie):
        if name_flie in self.dic_flie:
           del self.dic_flie[name_flie]
           return True
        else:
            print("the name not exist!")
            return False
    def update_file(self,name_file,size_file):
        if name_file in self.dic_flie:
            self.dic_flie.update({name_file:size_file})
            return True
        else:
            print("the file not exist!")
            return False
