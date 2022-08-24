first_digit = 0
second_digit = 1

x = input("Number: ")
# print(type(x))
i = 0
while i < int(x):
    temp = first_digit + second_digit
    print(second_digit)

    first_digit = second_digit
    second_digit = temp

    i = i + 1
