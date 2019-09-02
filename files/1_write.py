# Creating and Writing to a file 

# 1. open the file 
data = open("data.txt", "w")

#2. Write to file using print 
print("Hello World!!", file=data)

# 3. Write using write function 
data.write("I am from write function. I am from write function.I am from write function.\nI am from write function.")

lines = ["this is line number"+str(i) for i in range(10) ]

# 4. Using writeline 
data.writelines(lines)