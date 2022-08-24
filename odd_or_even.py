from tabnanny import check


num = input("Input number: ")
# print(type(num))
check = int(num) % 2
# print(type(check))
if check == 0:
    print("even")
else:
    print("odd")
