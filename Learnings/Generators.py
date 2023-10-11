def my_generator():
    for i in range(1, 50+1):
        yield i


gen = my_generator()

# print(next(gen))      # We can print values like this also
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:   # We can print values like this also if there are many values
    print(j)
