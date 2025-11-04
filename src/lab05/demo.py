from json_csv import csv_to_json,json_to_csv
from csv_xlsx import csv_to_xlsx

json_to_csv('data/samples/people.json','data/out/people_from_json.csv')
csv_to_json('data/samples/people.csv','data/out/people_from_csv.json')

json_to_csv('data/samples/students.json','data/out/students_from_json.csv')
csv_to_json('data/samples/recipes.csv','data/out/recipes_from_csv.json')

csv_to_xlsx('data/samples/cities.csv','data/out/cities.xlsx')
csv_to_xlsx('data/samples/weather.csv','data/out/weather.xlsx')