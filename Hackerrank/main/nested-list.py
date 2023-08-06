'''
Created on 15. 7. 2023

@author: valic
'''

if __name__ == '__main__':
    n = int(input())
    students = []
    grades = []
    for _ in range(n):
        name = input()
        score = float(input())
        grades.append(score)
        students.append([name, score])
    # find and delete lowest grades    
    min_value = min(grades)
    lowest_grades_neg = [i for i, x in enumerate(grades) if x != min_value]
    
    students_without = []
    grades_without = []
    for i in lowest_grades_neg:
        students_without.append(students[i])
        grades_without.append(grades[i])
    min_value = min(grades_without)
    second_lowest_grades = [i for i, x in enumerate(grades_without) if x == min_value]
    
    result_names = []
    for j in second_lowest_grades :
        result_names.append(list(students_without[j]).pop(0))
    
    sorted_result_names = sorted(result_names)
    
    for _ in sorted_result_names :
        print(_)
        