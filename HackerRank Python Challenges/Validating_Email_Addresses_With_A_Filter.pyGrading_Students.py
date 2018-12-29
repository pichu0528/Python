'''
Code challenge from HackerRank

HackerLand University has the following grading policy:
  1. Every student receives a grade in the inclusive range from 0 to 100.
  2. Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:
  1. If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the 
  next multiple of 5.
  2. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
  
For example, grade = 84 will be rounded to 85 but grade = 29 will not be rounded because the rounding would
result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

Function Description
Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.
gradingStudents has the following parameter(s):
  grades: an array of integers representing grades before rounding

Input Format
The first line contains a single integer, n, the number of students. 
Each line i of the n subsequent lines contains a single integer, grades[i], denoting student i's grade.

Constraints
  1. 1 <= n <= 60
  2. 0 <= grades[i] <= 100

Output Format
For each grades[i], print the rounded grade on a new line.

Sample Input 0
4
73
67
38
33
Sample Output 0
75
67
40
33
Explanation 0
Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 75 - 73 < 3, the student's grade is rounded to 75.
Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70 - 67 = 3, the grade will not be modified and the student's final grade is 67.
Student 3 received a 38, and the next multiple of 5 from 38 is 40. Since 40 - 38 < 3, the student's grade will be rounded to 40.
Student 4 received a grade below 38, so the grade will not be modified and the student's final grade is .
'''

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    
    # method 1: for loop and append the value to a list
    # final_grade = []
    # for i in grades:
    #     if i >= 38 and ((i // 5)+1)*5 - i < 3:
    #         final_grade.append(((i // 5)+1)*5)
    #     else:
    #         final_grade.append(i)
    # return final_grade

    # method 2: list comprehension
    return [((i // 5)+1)*5 if i >= 38 and ((i // 5)+1)*5 - i < 3 else i for i in grades]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
