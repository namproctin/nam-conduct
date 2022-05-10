import csv
import time
import itertools

def loaddb():
  with open("school_data.csv", encoding="utf8", errors='ignore') as f:
    reader = csv.reader(f)

    global total_school
    total_school = 0
    global state_dict
    state_dict = {}
    global metro_dict
    metro_dict = {}
    global city_dict
    city_dict = {}
    global city_code_dict
    city_code_dict= {}

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

      city_code_dict[city_name] = row[5]


def search_schools(str_query):
  start_time = time.time()

  old_str = str_query
  str_query = str_query.upper()
  word_list = str_query.split(" ")

  max_score = 0
  second_max_score = 0
  third_max_score = 0

  best_result_school_name = None
  best_result_city_name = None
  second_best_result_school_name = None
  second_best_result_city_name = None
  third_best_result_school_name = None
  third_best_result_city_name = None

  # score the city name first then score up the school name later

  for city_name in city_dict:
    score = 0
    for word in word_list:
      if word in city_name:
        score += 1

    for school_name in city_dict[city_name]:
      second_score = score
      for word in word_list:
        if word in school_name:
          if word == "SCHOOL":
            second_score = second_score + 1
          else:
            second_score = second_score + 3

      if second_score > max_score:
        max_score = second_score
        best_result_school_name = school_name
        best_result_city_name = city_name
      elif second_score > second_max_score:
        second_max_score = second_score
        second_best_result_school_name = school_name
        second_best_result_city_name = city_name
      elif second_score > third_max_score:
        third_max_score = second_score
        third_best_result_school_name = school_name
        third_best_result_city_name = city_name

  end_time = time.time()
  duration = str(round(end_time,20) - round(start_time,20))
  print("Results for \"" +old_str +"\" (search took: "+ duration[0:5] +"s)")
  print("1. ",best_result_school_name)
  print(best_result_city_name, ",", city_code_dict[best_result_city_name])
  #print("score", max_score)
  if second_max_score > 0:
    print("2. ",second_best_result_school_name)
    print(second_best_result_city_name, ",", city_code_dict[second_best_result_city_name] )
    #print("score", second_max_score)
  if third_max_score > 0:
    print("3. ",third_best_result_school_name)
    print(third_best_result_city_name, ",", city_code_dict[third_best_result_city_name] )
    #print("score", third_max_score)

loaddb()

global start_time
global end_time


search_schools("elementary school highland park")
#search_schools("jefferson belleville")
#search_schools("riverside school 44")
#search_schools("granada charter school")
#search_schools("foley high alabama")
#search_schools("KUSKOKWIM")


