grades_file = open("grades.txt", "r")
grades_lines = grades_file.readlines()

grades_sum = 0
grades_count = 0

for line in grades_lines:
  grades_float = float(line)
  grades_sum += grades_float
  grades_count += 1

average = grades_sum / grades_count
print(average)

grades_file.close()
