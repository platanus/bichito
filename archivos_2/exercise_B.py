def get_average(grades_filename):
  grades_file = open(grades_filename, "r")
  grades_lines = grades_file.readlines()
  grades_file.close()

  grades_sum = 0
  grades_count = 0

  for line in grades_lines:
    grades_float = float(line)
    grades_sum += grades_float
    grades_count += 1

  return grades_sum / grades_count

def write_report(report_filename, title, grade):
  report_file = open(report_filename, "w")
  report_file.write(f"{title}\n{average}")
  report_file.close()

average = get_average("grades_spanish.txt")
write_report("report_spanish.txt", "Promedio Lenguaje", average)



