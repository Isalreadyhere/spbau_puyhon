#Мы вычислим количество точек, попавших в четвертьокружности в квадрате 1х1
#Площадь этой четвертьокружности - S=pi*R^2/4
#Приняв за S количество попавших в четвертьокружность точек, а за R^2 - общее количетво точек в квадрате 1х1, вычислим pi по формуле pi=4*(S/R^2)


import random
import multiprocessing
dotnumber = 10000 #количество создаваемых точек

def dots_generating(n):
    count = 0;

    for i in range(n): # создаем точки и проверяем, попадают ли в четвертьокружность

        x=random.random() 
        y=random.random()
        if ((((x ** 2) + (y ** 2)) ** 0.5) <= 1):
            count += 1
        pi = 4*(count/dotnumber) #вычисляем пи

    return pi


def run_generation(pool): #распараллеливаем и берем среднее из множества результатов, повышая точность
    l = pool.map(dots_generating, [dotnumber]*20)
    final = sum(l)/len(l)
    return final


if __name__ == '__main__': #собственно выполняем все
    pool = multiprocessing.Pool()
    print(run_generation(pool))
    
    


