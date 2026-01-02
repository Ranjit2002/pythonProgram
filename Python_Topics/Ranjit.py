def welcome():
    print("Hey you are welcome from Ranjit")


# print(__name__)     # If I run this program here then it will print __main__ and from somewhere else then Ranjit

if __name__ == "__main__":      # If you are importing this somewhere then it will help watch Harry's video
    welcome()

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a+b

x = int(input("Enter a number: "))
fibonacci(x)
