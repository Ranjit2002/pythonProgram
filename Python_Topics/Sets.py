"""
s = {1, 3, 3, 5}
print(s)   # This will not print the repeated values of the set s like 3 is repeated 3 will print only once

n = {"Carla", 19, False, 5.9, 19}
print(n)

t = set()
print(type(t))

for i in n:
    print(i)

s1 = {1, 6, 2, 4, 6}
s2 = {6, 8, 9}
print(s1.union(s2))  # This will print both the sets elements to not the same elements
print(s1, s2)       # This will print the set 1 and set 2
s1.update(s2)       # This will merge the set 1 and set 2 together
print(s1)           # This will print the updated set 1

cities1 = {"Tokyo", "California", "Seoul", "Beijing", "Shanghai"}
cities2 = {"Mumbai", "California", "Melbourne", "Beijing"}
print(cities1.union(cities2))           # Jo dono me same hai o 1 baar hi print karega
print(cities1.intersection(cities2))    # Jo dono set me hai o print karega
cities1.intersection_update(cities2)    # First set ko update kar dega aur print karne k baad jo dono me hai o nahi hogo
print(cities1)
cities = cities1.symmetric_difference(cities2)
print(cities)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities = cities1.symmetric_difference(cities2)  # Jo dono me same nahi hai o print karega
print(cities)

cities3 = cities1.difference(cities2)
print(cities3)   # Print the cities are not there in the cities2

print(cities1.isdisjoint(cities2))   # It will print the true if both the sets are different

city1 = {"Tokyo", "Madrid", "Delhi", "Berlin"}
city2 = {"Seoul", "Kabul"}
print(city1.issuperset(city2))
city3 = {"Tokyo", "Delhi"}
print(city1.issuperset(city3))   # Means agar city1 k elements city3 me hai
print(city3.issubset(city1))     # Agar city3 ki value city1 me hai to true print karega

city1.remove("Madrid")      # remove method is used to remove any element from the set
                            # if remove element was not there in the set it will throw an error
print(city1)

city1.discard("Kenya")      # This method will also remove the element from the set
                            # if element was not there in the set it will not throw an error like remove method
print(city1)

del city1   # If you use del method it will delete the set
print(city1)
"""

n = {"Carla", 19, False, 5.9, 19}
if "Carla" in n:
    print("Carla is present")
else:
    print("Carla is absent")

