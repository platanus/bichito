grades_file = open("grades_spanish.txt", "r")
grades_lines = grades_file.readlines()
grades_file.close()

grades_sum = 0
grades_count = 0

for line in grades_lines:
  grades_float = float(line)
  grades_sum += grades_float
  grades_count += 1

average = grades_sum / grades_count

report_file = open("report_spanish.txt", "w")
report_file.write("Promedio Lenguaje\n" + str(average))

report_file.close()


