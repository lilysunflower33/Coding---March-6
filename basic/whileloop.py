i = 1
total = 0
while i <= 10:
    total += i #or total = total + 1
    if i % 2 == 0:
      print("i = {0} Total = {1}".format(i, total))
    i = i + 1


print("Final total: ", total)