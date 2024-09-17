number = int(input(": ")) 
counter = 1
hasil = f"{number}! = "

while number > 1:
    counter *= number
    hasil += f" {number} X"
    number-=1

hasil += " 1"
print(hasil)
"""
1. take input from user
2. make a variable "counter" for the contained result
3. make a variable "hasil" for the total result to be displayed

5. start the while loop with the parameter of "when variable "number" is less than one: do this
6. make the counter variable to multiply by itself - 1
7. append the "hasil" variable with "number" variable including the string template to be displayed
8. decrease the number with 1 and reassign it to the variable "number"

10. append hasil with 1 so that the factorial displayed is complete
11. print the result template 
"""
