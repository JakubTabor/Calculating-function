import figures
from enum import IntEnum

Menu_Figure = IntEnum(
    'Menu_Figure' , 'Square, Rectangle, Circle, Triangle, Trapeze, End')

print(list(Menu_Figure))

choose = int(input("""Choose figure to calculate their area:
1. Square
2.Rectangle
3.Circle
4.Triangle
5.Trapeze
6.End
"""))

if (choose == Menu_Figure.Square):
    a = float(input("give the side of the square: "))
    print("figure area is: ", figures.area_sqare(a))

elif (choose == Menu_Figure.Rectangle):
    a = float(input("enter the length of the first side: "))
    b = float(input("enter the length of the secound side: "))
    print("figure area is: ", figures.area_rectangle(a, b))

elif (choose == Menu_Figure.Circle):
    r = float(input(""))
    print("figure area is: ", figures.area_circle(r))

elif (choose == Menu_Figure.Triangle):
    a = float(input("enter the length of the first side: "))
    h = float(input("enter the length of the first side: "))
    print("figure area is: ", figures.area_triangle(a, h))

elif (choose == Menu_Figure.Trapeze):
    a = float(input("enter the length of the first side: "))
    h = float(input("enter the length of the first side: "))
    b = float(input("enter the length of the secound side: "))
    print("figure area is: ", figures.area_trapeze(a, b, h))

elif (choose == Menu_Figure.End):
    print("good bye")

else:
    print("You choose the wrong number")
