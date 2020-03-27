from collections import OrderedDict
from dateutil.parser import parse
import csv
def get_latest(csv_line):
    dates = dict(filter(lambda element: is_date(element[0]), csv_line.items()))
    history = {date: int(amount or 0) for date, amount in dates.items()}
    latest = list(history.values())[-1]
    return latest

def extract_csv_line(csv_line):
    return dict([('country', csv_line["Country/Region"]),('total_hit',get_latest(csv_line))])
def is_date(string):
   try:
      parse(string, fuzzy=False)
      return True
   except ValueError:
      return False
def print_dict(dict_to_print):
   for item in dict_to_print.items(): 
      print("{}{}".format(item,""))
def print_type(v):
   print(type(v))
def get_total(dict_to_iterate):
   total = 0
   for item in dict_to_iterate.items(): 
      total = total + item[1]
   print("Total is {}{}".format(total,""))
CSV_FILE_NAME='/Users/subratamazumder/workspace/covid19/backend-app/data-loader/covid19-data-loader-function/time_series_covid19_confirmed_global-s3.csv'

with open(CSV_FILE_NAME) as csvfile:

   readCSV = csv.DictReader(csvfile)
   print_type(readCSV)
   count = 0
   for row in readCSV:

      # print_type(row)
      # break;
      # print(row)
      if row["Country/Region"] is not None :
         extracted_row = extract_csv_line(row)
         print ("{}-{}".format(extracted_row["country"],extracted_row["total_hit"]))
         count = count + 1
      else :
         count = count + 1
      #   print(row[0],row[1],row[2],)
   print("*******Invalid country count-{}".format(count))
# covid19_india = OrderedDict([('Province/State', ''), ('Country/Region', 'India'), ('Lat', '21.0'), ('Long', '78.0'), ('1/22/20', '0'), ('1/23/20', '0'), ('1/24/20', '0'), ('1/25/20', '0'), ('1/26/20', '0'), ('1/27/20', '0'), ('1/28/20', '0'), ('1/29/20', '0'), ('1/30/20', '1'), ('1/31/20', '1'), ('2/1/20', '1'), ('2/2/20', '2'), ('2/3/20', '3'), ('2/4/20', '3'), ('2/5/20', '3'), ('2/6/20', '3'), ('2/7/20', '3'), ('2/8/20', '3'), ('2/9/20', '3'), ('2/10/20', '3'), ('2/11/20', '3'), ('2/12/20', '3'), ('2/13/20', '3'), ('2/14/20', '3'), ('2/15/20', '3'), ('2/16/20', '3'), ('2/17/20', '3'), ('2/18/20', '3'), ('2/19/20', '3'), ('2/20/20', '3'), ('2/21/20', '3'), ('2/22/20', '3'), ('2/23/20', '3'), ('2/24/20', '3'), ('2/25/20', '3'), ('2/26/20', '3'), ('2/27/20', '3'), ('2/28/20', '3'), ('2/29/20', '3'), ('3/1/20', '3'), ('3/2/20', '5'), ('3/3/20', '5'), ('3/4/20', '28'), ('3/5/20', '30'), ('3/6/20', '31'), ('3/7/20', '34'), ('3/8/20', '39'), ('3/9/20', '43'), ('3/10/20', '56'), ('3/11/20', '62'), ('3/12/20', '73'), ('3/13/20', '82'), ('3/14/20', '102'), ('3/15/20', '113'), ('3/16/20', '119'), ('3/17/20', '142'), ('3/18/20', '156'), ('3/19/20', '194'), ('3/20/20', '244'), ('3/21/20', '330'), ('3/22/20', '396'), ('3/23/20', '499'), ('3/24/20', '536'), ('3/25/20', '657'), ('3/26/20', '727')])
# country = covid19_india["Country/Region"]
# print ("country - "+country)
# print_dict(covid19_india)
# dates = dict(filter(lambda element: is_date(element[0]), covid19_india.items()))
#dates = dict(filter(is_date, covid19_india.items()))


# print_dict(dates)
# print_type(dates)
#dates = dict(filter(lambda element: is_date(element[0]), item.items()))
# history = {date: int(amount or 0) for date, amount in dates.items()}
# latest = list(history.values())[-1]
# print ("latest - ",latest)
# print_type(history)
# get_total(history)
# print_dict(history)