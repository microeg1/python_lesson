#Напишите программу, которая принимает на вход координаты двух точек
#и находит расстояние между ними в 2D пространстве.


x1 = int(input('ВВедите x1:'))
y1 = int(input('ВВедите y1:'))
x2 = int(input('ВВедите x2:'))
y2 = int(input('ВВедите y2:'))

range = ((x1-x2)**2+(y1-y2)**2)**0.5

print(round(range, 2))
