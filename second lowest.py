# Name: Ryan Talalai
# Date: 03 March 2021
# Assignment: 2nd Lowest
# This program outputs the name and score of the student with 2nd lowest score

n = int(input("Enter number of students: "))

lowscore = 101
lowscore2 = 102
lowscorename = 0
lowscorename2 = 0

i = 1
while i <= n:
    print("Please enter student",i,"name:")
    x = input()
    print("Please enter student",i,"score:")
    y = int(input())


    if y < lowscore:
        lowscore2 = lowscore
        lowscorename2 = lowscorename
        lowscore = y
        lowscorename = x
    elif y < lowscore2:
        lowscore2 = y
        lowscorename2 = x
    
    i += 1

print("2nd lowest student is",lowscorename2,"with score",lowscore2)
