#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
 #и проверяет, является ли этот день выходным.


day = int(input('ВВедите номер дня недели:'))

if 0<day<6:
    print('сегодня будний день')
elif 5<day<8:
    print('сегодня Выходной день')
else:
    print('где ты Видел день недели с таким номером, дурачок')