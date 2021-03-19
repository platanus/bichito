grades_file = open("grades.txt", "r")

first_grade = float(grades_file.readline())
second_grade = float(grades_file.readline())
third_grade = float(grades_file.readline())
fourth_grade = float(grades_file.readline())

average = sum([first_grade, second_grade, third_grade, fourth_grade]) / 4
print(average)

grades_file.close()
