#Loops

#definite for loop

for i in range(1,10):
    print(i)

for a in range(4):
    print("Hello")

num=1
for count in range(1,5):
    num=num*count
    print(num)

for name in "Vienna Philharmoic":
    print(name)

#indefinite while loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Checking the valid account number")
valid_account = "12345"

account_number = input("Enter your account number: ")

while account_number != valid_account:
    print("Invalid account number. Please try again.")
    account_number = input("Enter your account number: ")
print("Account number is valid. Login successful!")


#nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()
