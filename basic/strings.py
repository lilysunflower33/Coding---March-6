n=135
# 35 / 2 = 17.3 
print("{0} / 2 = {1}".format(n, n / 2))
# 35 // 2 = 17 
print("{name} // 2 = {result}".format(name=n, result=(n // 2)))

a='345\n\t35 \'86\''
print("{0} / 2 = {1}".format(n, n / 2))

a='1123'
b="2\n123"
print(a)
d='123\n\t23\'77\''
c='''
hi
bye
hello
'''

print("b={0}".format(b))
print(c)
print('======= UPPER')
print(d)
print(a+c)
print(len(c+a))
print("a = {av}".format(av=a))

print(a*100) 

age = input("How old are you?")
print("Age is: {0}".format(age))

print("35 / 2 = ", 35 / 2)
print("35 // 2 = ", 35 // 2)

a = 'Hello Somebody'
print("Repeating \"{0}\" {1} times: {2}".format(a, 4, a * 4))
#print(a * 50)

print("Try the named index placegolder:")
print("Name: {name}, Age: {age}".format(age=13, name="Julia"))

b = "Hello\n\"World\"!"
#print(b + a)
c = """
Hello 
Line one "World"
line two
line 4
"""
#print("original: " + c)

#print("Title cases:" + c.title())
#print("Capitalize:" + c.capitalize())
#print("Upper cases:" + c.upper())
#print("lower cases:" + c.lower())