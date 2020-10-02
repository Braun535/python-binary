num1 = '0001'
num2 = '0010'




a = 5
b = 2

if num1 == '0000':
	a = 0
if num1 == '0001':
	a = 1
if num1 == '0010':
	a = 2
if num1 == '0011':
	a = 3
if num1 == '0100':
	a = 4
if num1 == '0101':
	a = 5
if num1 == '0110':
	a = 6
if num1 == '0111':
	a = 7
if num1 == '1000':
	a = 8
if num1 == '1001':
	a = 9
if num1 == '1010':
	a = 10
if num1 == '1011':
	a = 11
if num1 == '1100':
	a = 12
if num1 == '1101':
	a = 13
if num1 == '1110':
	a = 14
if num1 == '1111':
	a = 15


if num2 == '0000':
	b = 0
if num2 == '0001':
	b = 1
if num2 == '0010':
	b = 2
if num2 == '0011':
	b = 3
if num2 == '0100':
	b = 4
if num2 == '0101':
	b = 5
if num2 == '0110':
	b = 6
if num2 == '0111':
	b = 7
if num2 == '1000':
	b = 8
if num2 == '1001':
	b = 9
if num2 == '1010':
	b = 10
if num2 == '1011':
	b = 11
if num2 == '1100':
	b = 12
if num2 == '1101':
	b = 13
if num2 == '1110':
	b = 14
if num2 == '1111':
	b = 15







c = a + b;
d = (bin(c))
d = d.strip('0b')
print(d)
