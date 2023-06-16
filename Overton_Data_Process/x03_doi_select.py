import os
import pandas as pd
import numpy as np
import collections
import csv

#fi0 = open('overton_2017_2022_cite_eng.csv','r',encoding='utf-8')
fi0 = open('y1_cite_eng_usa.csv','r',encoding='utf-8')
#pdf_id,doc_id,language,year,month,day,country,cite_count,cite\n

doi_dict = {}

while True:
    line = fi0.readline()
    if line=='':
        break
    line_list = line[:-1].split(',',8)
    #print(line_list[4])
    doi_line = line_list[8]
    year = line_list[3]
    doi_list = doi_line[2:-2].split("', '")
    if doi_list[0]!='':
        #print(doi_list)
        for x in doi_list:
            # process wrong doi (but can only address these obvious issues)
            if '?' in x:
                x_list = x.split('?')
                x = x_list[0]
            elif "reportseries:" in x:
                x_list = x.split('reportseries:')
                x = x_list[0]
            if x not in doi_dict:
                doi_dict[x] = {'2017':0,'2018':0,'2019':0,'2020':0,'2021':0,'2022':0,'total':0}
            doi_dict[x]['total'] = doi_dict[x]['total']+1
            doi_dict[x][year] = doi_dict[x][year]+1
#fi1 = open('y21_doi_cited_usa.csv','w',encoding='utf-8')


fi3 = open('y23_doi_year_count_usa.csv','w',encoding='utf-8',newline='')
# number of the citations of doi each year 
header_3 =['doi',2017,2018,2019,2020,2021,2022,'total']
csv_writer_3 = csv.writer(fi3)
csv_writer_3.writerow(header_3)

fi2 = open('y22_doi_list_usa.csv','w',encoding='utf-8',newline='')
header_2 =['doi']
csv_writer_2 = csv.writer(fi2)
csv_writer_2.writerow(header_2)

for x in doi_dict:
    line_2 = [x]
    csv_writer_2.writerow(line_2)
    line_3 = [x,doi_dict[x]['2017'],doi_dict[x]['2018'],doi_dict[x]['2019'],doi_dict[x]['2020'],doi_dict[x]['2021'],doi_dict[x]['2022'],doi_dict[x]['total']]
    csv_writer_3.writerow(line_3)

    #fi1.write(str(doi_dict[x])+','+str(x)+'\n')

fi0.close()