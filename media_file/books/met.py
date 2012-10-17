# -*- coding: utf-8 -*-EdIzmer
import math


a = 4
b = 4
e = 0.000000000000001
s = 0.0
m = a 
ss = 0
#f = 4 - 4 * b * x / (a * math.sqrt(a * a - x * x))
x1 = (m + s) / 2
while math.fabs(4 - 4 * b * x1 / (a * math.sqrt(a * a - x1 * x1))) > e:
	if (4 - 4 * b * x1 / (a * math.sqrt(a * a - x1 * x1))) > 0:
		s = x1
	else:
		m = x1
	x1 = (s + m) / 2
	ss = ss+1

print "Итераций  ", ss
print "x = ", x1
print "Периметр равен",  4 * (x1 + b / a * math.sqrt(a * a - x1 * x1))