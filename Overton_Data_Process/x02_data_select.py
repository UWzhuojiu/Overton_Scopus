import os
import numpy

# choose english USA policy document
fi0 = open('y0_overton_scopus_data.csv','r',encoding='utf-8')
#pdf_id,doc_id,language,year,month,day,country,cite_count,cite\n
line_0 = fi0.readline()
print(line_0)
count = 0
count_us = 0
fi = open('y1_cite_eng_usa.csv','w',encoding='utf-8')
#fi.write(line_0)
while True:
    line = fi0.readline()
    if line=='':
        break
    line_list = line[:-1].split(',',8)
    #print(line_list)
    if (line_list[7]!='0') & (line_list[2]=='eng'):
        count = count+1
        if line_list[6]=='USA':
            count_us = count_us+1
            fi.write(line)
fi.close()
print(count)    #128988
print(count_us) #80650
fi0.close()