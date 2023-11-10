# READING

# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# WRITING

# f = open('myfile.txt', 'w')
# f.write("Hello World! ")
# f.close()

# APPEND

# f = open('myfile.txt', 'a')
# f.write("Hello Ranjit! ")
# f.close()
#
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()


# We can use this method then we don't need to close files

# with open('myfile.txt', 'w') as f:
#     f.write('Hey I am Ranjit')
#
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)

f = open('myfile.txt', 'r')
print(type(f))
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of students {i} in Maths is: {m1}")
#     print(f"Marks of students {i} in English is: {m2}")
#     print(f"Marks of students {i} in SST is: {m3}")
#     print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line1\n', 'line2\n', 'line3\n']
# f.writelines(lines)
# f.close()
