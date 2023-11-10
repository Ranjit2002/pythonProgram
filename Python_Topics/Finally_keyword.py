# try:
#     l = [1, 2, 3, 4, 5]
#     a = int(input("Enter the index:-"))
#     print(l[a])
# except:
#     print("Some error occurred")
#
# print("I am always executed")       # Why to use finally you can directly do this also
# but print will not run in function but finally will run in function also that's why it's important

# finally:  #
#     print("I am always executed")

def func1():
    try:
        l = [1, 2, 3, 4, 5]
        a = int(input("Enter the index:-"))
        print(l[a])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")

    print("I will not execute in function")  # Why to use finally you can directly print like this also


x = func1()
print(x)
