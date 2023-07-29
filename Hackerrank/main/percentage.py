'''
Created on 15. 7. 2023

@author: valic
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    values = student_marks.get(query_name)
    sums = 0
    for x in values :
        sums +=x
    print("%.2f" % (sums/len(values)))
        