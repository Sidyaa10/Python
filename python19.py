#For Loop
#A for loop is special type of loop in python which allows us to through different arrays, or we can loop over letters inside a string etc

Genius=["Tesla","Curie","Homi","Einstein"]

#to know length of the array
print(len(Genius))

#to loop through the array using for loop and print the names 1st to last
for names in Genius:
    print(names)

#to print numbers from index 0 to 9
for index in range(10):
    print(index)

#Same as above but for determining a range in array
for index in range(len(Genius)):
    print(Genius[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Next Iteration")