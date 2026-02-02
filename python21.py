#2D lists and Nested loops

num_grid=[
    [1,2,3],  #row0
    [4,5,6],  #row1
    [7,8,9],  #row2
    [10]  #row3
]

#I printed a number from second list which is at the position 1 and the number which is in position 1 which is 5
print(num_grid[1][1])

for row in num_grid:
    print(row)

for row in num_grid:
    for col in row:
        print(col)