set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.intersection(set2)
set1.symmetric_difference_update(set2)
set5 = set1.pop()


print(set4)
print(set1)
print(set5)