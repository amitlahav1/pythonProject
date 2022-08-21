string=input("enter world:")
signal=input("enter signal:")

if signal in string:

        for i in string:
            if i==signal:
                print (string.index(signal))




else:
    print("-1")


