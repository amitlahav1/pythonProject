def sring_upper_lower(str):
    coun_upper=0
    count_lower=0

    for i in str:
        if i.isupper():
            coun_upper+=1
        if i.islower():
            count_lower+=1

    print(count_lower,"lower")
    print(coun_upper,"upper")


list="amitLAamit"

sring_upper_lower(list)
