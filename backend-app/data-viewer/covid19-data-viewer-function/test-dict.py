from collections import OrderedDict
from dateutil.parser import parse
from collections import ChainMap
import csv
from zipfile import ZipFile, ZIP_DEFLATED
ZIP_FROM_FOLDER='/Users/subratamazumder/workspace/covid19/backend-app/data-loader/covid19-data-loader-function/zip-from'
ZIP_TO_FOLDER='/Users/subratamazumder/workspace/covid19/backend-app/data-loader/covid19-data-loader-function/zip-to'
CSV_FILE_NAME_DEATH='/Users/subratamazumder/workspace/covid19/backend-app/data-loader/covid19-data-loader-function/time_series_covid19_deaths_global.csv'
CSV_FILE_NAME_CONF='/Users/subratamazumder/workspace/covid19/backend-app/data-loader/covid19-data-loader-function/time_series_covid19_confirmed_global-s3.csv'
def get_latest(csv_line):
    dates = dict(filter(lambda element: is_date(element[0]), csv_line.items()))
    history = {date: int(amount or 0) for date, amount in dates.items()}
    latest = list(history.values())[-1]
    return latest

def is_date(string):
   try:
      parse(string, fuzzy=False)
      return True
   except ValueError:
      return False
def print_list_reg(all_rec_list):
   for itm in all_rec_list:
      print(itm)
def print_list(all_rec_list):
   for itm in all_rec_list:
      print_dict(itm)
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

def read_file():
   all_rec_list = []
   with open(CSV_FILE_NAME_CONF) as csvfile:
      readCSV = csv.DictReader(csvfile)
      print_type(readCSV)
      count = 0
      for row in readCSV:

         # print_type(row)
         # break;
         # print(row)
         if row["Country/Region"] is not None :
            extracted_row = extract_csv_line(row)
            all_rec_list.append(extracted_row)
            print ("{}".format(extracted_row))
            count = count + 1
         else :
            count = count + 1
         #   print(row[0],row[1],row[2],)
      print("*******Invalid country count-{}".format(count))
      # print_list(all_rec_list)
def dict_apend():
   db_record = dict()
   print_dict(db_record)
   db_record['a']='b'
   # db_record.update({'a','b'})
   print_dict(db_record)
def dict_chain_map():
   chained_dict = ChainMap()
   print_dict(chained_dict)
   fruit_prices = {'apple': 0.40, 'orange': 0.35}
   vegetable_prices = {'apple': 0.20, 'onion': 0.55}
   chained_dict.new_child()
   # chained_dict = ChainMap(fruit_prices, vegetable_prices)
   print_dict(ChainMap(fruit_prices, vegetable_prices))
def extract_csv_line(csv_line, rec_type):
    if rec_type == 'total_confirmed':
        return dict([('country', csv_line["Country/Region"]), ('total_confirmed', get_latest(csv_line))])
    if rec_type == 'total_deaths':
        return dict([('country', csv_line["Country/Region"]), ('total_deaths', get_latest(csv_line))])
    if rec_type == 'total_recovered':
        return dict([('country', csv_line["Country/Region"]), ('total_recovered', get_latest(csv_line))])
def extract_csv_line_new(csv_line, rec_type):
   pass
def add_to_dict(dict_to_add):
   pass
def prepare_db_record(file_name,rec_type):
    all_db_record = {}
    country_list = []
    count = 0 
    with open(file_name) as csvfile:
        for csv_line in csv.DictReader(csvfile):
            count = count + 1
            country = csv_line["Country/Region"]
            country_list.append(country)
            unique_key = "{}#{}".format(country, rec_type)
            # print("unique_key-{}".format(unique_key))
            if unique_key in all_db_record: #If Same country already counted before then add it up
               curr_latest = all_db_record[unique_key]
               new_latest = curr_latest + get_latest(csv_line)
               # print("curr_latest-{}, new_latest-{}".format(curr_latest,new_latest))
               all_db_record[unique_key] = new_latest
            else:
               all_db_record[unique_key] = get_latest(csv_line)
    print(
        "Toltal number of record prepared is -{}".format(count))
   #  print_list(country_list)
    return all_db_record, country_list
def get_total_deaths(all_db_record):
   unique_deaths_key = "{}#{}".format(country, 'total_deaths')
   if unique_deaths_key in all_db_record:
      return all_db_record[unique_deaths_key]
   else:
      return 0
def get_total_confirmed(all_db_record):
   unique_deaths_key = "{}#{}".format(country, 'total_confirmed')
   if unique_deaths_key in all_db_record:
      return all_db_record[unique_deaths_key]
   else:
      return 0
def prepare_data_rec():
   all_db_record, country_list = prepare_db_record(CSV_FILE_NAME_CONF,'total_confirmed')
# print_dict(all_db_record)
# print_list_reg(country_list)
   print(len(country_list))
   print(len(all_db_record))
   dynamo_rec = []
   for country in country_list:
      dynamo_rec.append(dict([('country', country), 
      ('total_confirmed',get_total_confirmed(all_db_record)),
      ('total_deaths',get_total_deaths(all_db_record))]))
   print(len(dynamo_rec))
   # print_list_reg(dynamo_rec)
   # print_dict(prepare_db_record(CSV_FILE_NAME_DEATH,'total_deaths'))
def zip_file():
   file_paths =[]
   file_paths.append("{}/{}".format(ZIP_FROM_FOLDER,'time_series_covid19_confirmed_global.csv'))
   file_paths.append("{}/{}".format(ZIP_FROM_FOLDER,'time_series_covid19_deaths_global.csv'))
   # writing files to a zipfile 
   with ZipFile("{}/{}".format(ZIP_TO_FOLDER,'covid19.csv'),'w',compression=ZIP_DEFLATED, allowZip64=True) as zip: 
      # writing each file one by one 
      for file in file_paths:
         zip.write(file)
def unzip_file():
   # opening the zip file in READ mode 
   with ZipFile("{}/{}".format(ZIP_TO_FOLDER,'covid19.csv'), 'r') as zip: 
      # printing all the contents of the zip file 
      zip.printdir() 
   
      # extracting all the files 
      print('Extracting all the files now...') 
      zip.extractall(path=ZIP_TO_FOLDER)
      print('Done!') 
"""
Main Code starts here
"""
# zip_file()
unzip_file()
# read_file()
# dict_apend()
# dict_chain_map()


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