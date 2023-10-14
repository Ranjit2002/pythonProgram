# def armstrong(number):
#     num_str = str(number)
#     num_digits = len(num_str)
#     total = sum(int(digit) ** num_digits for digit in num_str)
#     return total == number
#
#
# a = int(input("Enter a Number:- "))
# if armstrong(a):
#     print(f"{a} is an Armstrong number")
# else:
#     print(f"{a} is not an Armstrong number")

l = [i for i in range(1, 101)]
a = list(map(lambda x: 2 * x, l))
print(a)
