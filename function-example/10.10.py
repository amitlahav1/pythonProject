def str_plindrum (str):
    if (str[::-1])==str:
        return True
    else:
        return False

str="madam"
str2="amit"

if str_plindrum(str):
    print("plindrum !",{str})
else:
    print("not!")

if str_plindrum(str2):
    print("plindrum !")
else:
    print("not!")



