#-*- coding: UTF-8 -*-
s = "Eto stroka i tochka, a eto samoe-bolshoe-slovo-v-stroke"
d = s.split(" ")
t = [x for x in d if len(x)==max(map(len, d))]
print t