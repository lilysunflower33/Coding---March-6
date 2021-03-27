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


#define a list:
alist = ["a", "b", 12, 34,
  [2, 3, 4]
]

print("length of a list:", 
len(alist))

#how to access items in a list.
print("First Item: ", alist[0])
print("4th Item: ", alist[3])
print("Last Item: ", alist[-1])
print("The first item of the last item for list {0}: {1}".format(alist, alist[4][0]))
print("The second item of the last item for list {0}: {1}".format(alist, alist[4][1]))