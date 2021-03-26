numofterms = int(input("Number of terms you would like in this pattern: "))

n1, n2 = 0, 1
count = 0

if numofterms <= 0:
   print("Please try again and enter a positive integer.")
elif numofterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < numofterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1