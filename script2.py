import pymysql
import pandas
import csv
import pandas as pd

conn = pymysql.connect(host='localhost', port=3306, user='phpmyadmin', password='root', database='easypay')

cursor = conn.cursor()
query = 'select * from guest_student_gueststudent '

results = pandas.read_sql_query(query, conn)
results.to_csv("output.csv", index=False)



colnames = ['extra_details']
data = pandas.read_csv('/home/nisarg/Scrapper/output.csv', names=colnames, usecols=[2])


field_names = []
dict_list = []
for column in data:
    for row in data[column]:
        string = ""
        if row != "extra_details":
            string = str(row)
            string.replace("u'", "'")
            dict = eval(string)
            dict_list.append(dict)

with open('/home/nisarg/Scrapper/latest.csv', 'w') as csvfile:
    for dicto in dict_list:
        for key, value in dicto.items():
            if key not in field_names:
                field_names.append(key)
        
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(dict_list)


r1 = pd.read_csv('output.csv')
r2 = pd.read_csv('latest.csv')
result = pd.concat([r1, r2], axis=1, join='inner')
result.to_csv('result.csv')  
  
result = pd.read_csv('result.csv')
  
print("Original 'result.csv' CSV Data: \n")
# print(result)


result.drop('extra_details', inplace=True, axis=1)
result.to_csv('final.csv')    
  
