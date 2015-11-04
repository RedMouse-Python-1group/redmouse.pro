#-*- coding: UTF-8 -*-
s = "Eto stroka i tochka, a eto samoe bolshoe slovo-v-stroke"
str = raw_input("Введите пробел или зяпятой: ")
d = s.split(str)
t = [x for x in d if len(x)==min(map(len, d))]
print t