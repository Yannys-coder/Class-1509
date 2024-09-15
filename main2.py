my_set={2,4,6,8,10,12}
my_set2={1,2,3,4,5,6,7,8,9,10}
my_set2.add(11)
print(my_set2)
my_set2.add(12)
print(my_set2)
c= my_set.difference(my_set2)
print(c)
d= my_set.symmetric_difference(my_set2)
print(d)

a= my_set.union(my_set2)
print(a)

b=my_set.intersection(my_set2)
print(b)