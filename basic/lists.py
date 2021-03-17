# difine a list
l = ['a', 'b', 23, 45, "hello",
  [1,2,3,'a']
]

print(l)

print("first item: {0}".format(l[0]))
legnth = len(l)
print("list legnth: {0}".format(legnth))
print("last item: {0}".format(l[legnth-1]))
print("last item: {0}".format(l[-1]))

for item in l:
  print(item)

print(l[-1])
print(l[-1][-1])
print(l[-1][-2])