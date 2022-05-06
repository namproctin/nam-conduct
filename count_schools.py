import csv
import time
import itertools

def print_counts():
  with open("school_data.csv", encoding="utf8", errors='ignore') as f:
    reader = csv.reader(f)

    total_school = 0
    state_dict = {}
    metro_dict = {}
    city_dict = {}
    headings = next(reader)

    for row in reader:
      total_school += 1
      state_code = row[5]
      metro_code = row[8]
      city_name =  row[4]
      if state_code in state_dict:
        state_dict[state_code].append(row[3])
      else:
        state_dict[state_code] = [row[3]]

      if metro_code in metro_dict:
        metro_dict[metro_code].append(row[3])
      else:
        metro_dict[metro_code] = [row[3]]

      if city_name in city_dict:
        city_dict[city_name].append(row[3])
      else:
        city_dict[city_name] = [row[3]]

    print("Total Schools: ", total_school)

    print("Schools by State: ")
    for code in state_dict:
      print(code, ": ", len(state_dict[code]))

    print("Schools by Metro-centric locale:")
    for code in metro_dict:
      print(code, ": ", len(metro_dict[code]))

    max_school_of_city = 0
    city_name_with_max_school = None
    city_with_at_least_one_school = 0
    for city in city_dict:
      if len(city_dict[city]) > max_school_of_city:
        max_school_of_city = len(city_dict[city])
        city_name_with_max_school = city
      if len(city_dict[city]) > 0:
        city_with_at_least_one_school += 1

    print("City with most schools: ", city_name_with_max_school, "(", max_school_of_city, "schools)")

    print("Unique cities with at least one school: ", city_with_at_least_one_school)
