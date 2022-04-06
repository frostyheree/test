MIN_LEN = 9
password = input("Input password: ")

while len(password) < MIN_LEN:
    password = input("Input password: ")
for i in range(len(password)):
    print("*", end="")