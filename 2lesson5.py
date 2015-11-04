#-*- coding: UTF-8 -*-
s = "Eto stroka i tochka, a eto samoe samoe bolshoe slovo v stroke"
str = raw_input("Введите слово которое нужно посчитать его количество в предложении: ")
sum = 0
for word in s.split(" "):
	if word == str:
		sum += 1
print sum