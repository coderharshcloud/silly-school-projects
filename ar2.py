len=input("enter len of side")
ques=input("do you want to calculte area or perimetrer of the square") #if you want to calculate area then enter "area" otherwise enter "perimeter"

def area():
    area=int(len)*int(len)
    print(str(area))

if ques=="area":
    area()

def peri():
    perime=4*(int(len))
    print(str(perime))

if ques=="perimeter":
    peri()