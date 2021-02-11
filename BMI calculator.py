weight=int(input())
height=float(input())

bmi=weight/(height**2)

one="Underweight"
two="Normal"
three="Overweight"
four="Obesity"


if bmi<18.5:
    print(one)
else:
    if bmi>=18.5 and bmi<25:
        print(two)
    else:
        if bmi>=25 and bmi <30:
            print(three)        
        else:
            print(four)