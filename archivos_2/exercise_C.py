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

def write_report(report_filename, title, grades):
  report_file = open(report_filename, "w")
  report_string = title
  for (subject, grade) in grades:
    report_string += f"\nPromedio {subject}: {grade}"
  report_file.write(report_string)
  report_file.close()

spanish_average = get_average("grades_spanish.txt")
social_studies_average = get_average("grades_social_studies.txt")
biology_average = get_average("grades_biology.txt")
total_average = sum([spanish_average, social_studies_average, biology_average]) / 3

write_report(
  "report.txt",
  "Reporte",
  [
    ("Lenguaje", spanish_average),
    ("Historia", social_studies_average),
    ("Biología", biology_average),
    ("Total", total_average),
  ]
)



