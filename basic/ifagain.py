i = 1
total = 0
while i<5:
  total = total +i
  print("i = {0}, total = {1}".format(i, total))
  i=i+1
print("final total: {0}".format(total))

while True:
  animal = input("What animal is it? ")
  if animal == "dog": 
    print("bark bark")
  elif animal == "cat":
    print("meow meow")
  else animal == 'bye':
      break
  elif animal =='con':
    continue
  else:
    print("I don't know you!")
 
  print('going to next round!')