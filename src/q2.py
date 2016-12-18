Pre = 0
O = 1
E = 2

while E < 4000000 :
	if O < E : 
		pre = O
		O += E
	else : 
		pre = E
		E += O

print pre, O, E
print O - pre - 1
