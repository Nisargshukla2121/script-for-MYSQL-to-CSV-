import pandas
import csv

colnames = ['extra_details']
data = pandas.read_csv('/home/nisarg/Scrapper/output.csv', names=colnames, usecols=[2])

field_names = []
dict_list = []
with open('/home/nisarg/Scrapper/latest.csv', 'w') as csvfile:
    for column in data:
        for row in data[column]:
            string = ""
            if row != "extra_details":
                string = str(row)
                string.replace("u'", "'")
                dict = eval(string)
                dict_list.append(dict)

    for key, value in dict.items():
        if key not in field_names:
            field_names.append(key)
    
writer = csv.DictWriter(csvfile, fieldnames = field_names)
writer.writeheader()
writer.writerows(dict_list)