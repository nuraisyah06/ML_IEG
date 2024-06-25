'''tuple is a read only list
- not modifiedable, cannot append, delete, remove
- tuple use ()
- allows duplicate
- index for tuple use []
- count, is to count the quantity of an item
- can delete entire t uple by using del keyword
'''

x = (10, 20, 30, 40, 50, 60, 70)
print(x)
print(type(x))
print(x[3])



fruits = ("apple", "orange", "apple", "mango", "banana", "durian", "grapes", "mango", "apple")
print(fruits.count("apple"))



del x # to delete entire tuple

