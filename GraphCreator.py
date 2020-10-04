#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импорит библиотеки
import numpy #импорт другой библиотеки
import matplotlib.pyplot as mpp #импорт третьей библиотеки с изменением имени

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #это вроде как то заклинание
    arguments = numpy.r_[0:200:0.1] #numpy берет значения от 0 до 200 с шагом 0,1
    mpp.plot(                                               #график создается
        arguments,                                          #в выбранном
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #диапазоне
    )                                                       #аргументов
    mpp.show() #график выводится


# In[ ]:




