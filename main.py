#Student Grade Analysis

#import random integers
import random

#Random grades list
random_grades_list = []

#Generate random Grades in function


def random_grade_function():
    #Create 50 nicknames
    for i in range(50):
        random_grades_list.append(random.randint(1,100))

#Global variable
honours = 0

#call upon function
random_grade_function()

#Main Loop
loop = True
while loop:
    #Print out menu
    print("""
    \nMain Menu
    1.Display All Grades
    2.Randomize Grades
    3.Stats
    4.Count Honours
    5.Exit""")
    #Get user command
    Number = int(input("Please enter your command here: "))
    #Print out all the random grades
    if Number == 1:
        for element in random_grades_list:
            print(element)
    #Generate new random grades
    if Number == 2:
        #Empty out list
        random_grades_list = []
        #Call upon function again
        random_grade_function()
    #Get the statistic of the random grades
    if Number == 3:
        #Find the maximum grade
        max_value = max(random_grades_list)
        #Find the minimum grade
        min_value = min(random_grades_list)
        #Find the average grade
        average = sum(random_grades_list)/len(random_grades_list)
        #Print out answers
        print("The maximum value is: " + str(max_value))
        print("The minimum value is: " + str(min_value))
        print("The average is: " + str(average))
    #Count number of honours
    if Number == 4:
        #Cycle through random numbers to see if they are equal to or greater than 80
        for element in random_grades_list:
            if element >= 80:
                honours += 1
        print("The number of honour grades is: " + str(honours))
    #Exit program
    if Number == 5:
        loop = False
        print("Exit")





