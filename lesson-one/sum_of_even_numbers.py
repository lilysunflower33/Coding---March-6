total=0

lowestnum= int(input("What is your lowest value?\n"))
highestnum=int(input("What is you greatest value?\n"))

i = lowestnum
while i<=highestnum:
  if i % 2 == 0:
    total=total +i
  print("i={1} total = {0}".format(total, i))
  i=i+1
print("final total = {0}".format(total))