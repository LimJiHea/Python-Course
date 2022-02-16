num1, num2 = map(int,input('두개의 숫자를 입력해주세요').split())
char = input('연산자:')
print('입력하신 숫자는',num1,'과',num2,'입니다')


if char=='+':
  print(plus(num1, num2))

if char=='-':
  print(minus(num1,num2))

if char=='/':
  print(division(num1,num2))

if char=='*':
  print(times(num1,num2))

if char=='%':
  print(remainder(num1,num2))

if char=='**':
  print(power(num1,num2))

if char=='--':
  print(negation(num1))



