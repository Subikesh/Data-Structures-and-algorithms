def get_second_top(marksheet):
    # line 1
    marks = []
    for name, mark in marksheet:
        marks.append(mark)    
    # here marks.sort()[1] gives the second highest mark in the class
    marks.sort()
    second_highest = marks[1]

    # line 2
    names = []
    for name, mark in marksheet:
        if mark == second_highest:
            names.append(name)
    # names contains all the student names who got second mark
    # names.sort() to sort it alphabatically
    names.sort()
    print('\n'.join(names))
    # join() puts the string in between all the strings passed as argument

T = int(input())
marksheet = []
for i in range(T):
    marksheet.append([input(), float(input())])
get_second_top(marksheet)