def deadals (name, age,**more):
    print(name,age)
    for i in more:
        print(f"{i}:{more[i]}")


deadals('amit', 14,phone=458345843)
