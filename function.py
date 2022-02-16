a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None
print(type(a_number))
print(type(a_float))
print(type(a_boolean))
print(type(a_none))


days = ["Mon","Tue","Wed","Thur","Fri"]
print(days[3])
print(type(days))
print(len(days))
print("Modn" in days)
days.append("rrr")
print(days)
days.reverse()
print(days)

days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

jihae = {
  "name" : "Jihae",
  "age": 27,
  "korean":True,
  "fav_food" : ["Kimchi","Sunde"]
}

print(jihae)
print(jihae["age"])
print(jihae["name"])

jihae["cool"] = True
print(jihae)

print(len("lkjejkdjkfjdkjkej"))

age = "18"
print(type(age))
n_age = int(age)
print(type(n_age))

def say_hello(who="Hs"):
  print("hello", who)
  print("bye")

say_hello("Jihae")
say_hello()


def plus(a,b):
  print(a+b)

def minus(a,b=0):
  print(a-b)
  
plus(2,5)
minus(2)

def p_plus(a,b):
  print(a+b)

def r_plus(a,b):
  return a + b
  print("ekfkfkffkfk",True)

p_result = p_plus(2,3)
r_result = r_plus(2,3)

print(p_result,r_result)


def pplus(a,b):
  return a -b

result = pplus(b=30, a=1)
print(result)


def hello(name, age):
 return f"Hello {name} you are {age} years old"

hello = hello(age = "12",name="jihae")
print(hello)





def plus(a,b):
  try:
    return a+b
  except:
    print("오류가 발생했습니다.")
  

def minus(a,b):
  try:
    return a-b
  except:
    print("오류가 발생했습니다.")

def times(a,b):
  try:
    return a*b
  except:
    print("오류가 발생했습니다.")  

def division(a,b):
  try:
    return a/b
  except:
    print("오류가 발생했습니다.")

def remainder(a,b):
  try:
    return a%b
  except:
    print("오류가 발생했습니다.")  

def power(a,b):
  try:
    return a**b
  except:
    print("오류가 발생했습니다.")

def negation(a):
  try:
    return -a
  except:
    print("오류가 발생했습니다.")

str = "12"
print(type(str))
print(type(int(str)))