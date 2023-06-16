import json
import os

# read overton json data
json_list = os.listdir('overton_json')
#print(json_list[0])

# some of the meta data in the json
data_txt = 'pdf_id,doc_id,language,year,month,day,country,cite_count,cite\n'

pdf_list = []
doc_list = []
count = 0
count_0_count = 0
cite_total = 0
eng_count = 0

file0 = open('y0_overton_scopus_data.csv','w',encoding='utf-8')
for x in json_list:
    print(x)
    fi = open('overton_json/'+x,'r',encoding='utf-8')
    while True:
        line = fi.readline()
        if line=='':
            break

        policy_dict = json.loads(line)
        count = count+1
        line_txt = ''
        #print(policy_dict)
        pdf_id = policy_dict['pdf_document_id']
        '''
        if pdf_id not in pdf_list:
            pdf_list.append(pdf_id)
        '''
        line_txt = line_txt+pdf_id+','

        doc_id = policy_dict['policy_document_id']
        '''
        if doc_id not in doc_list:
            doc_list.append(doc_id)
        '''
        line_txt = line_txt+doc_id+','

        language = policy_dict['language']
        '''
        if language=='eng':
            eng_count = eng_count+1
        '''
        line_txt = line_txt+language+','

        year = policy_dict['published_on'][0:4]
        line_txt = line_txt+year+','

        month = policy_dict['published_on'][5:7]
        line_txt = line_txt+month+','

        day = policy_dict['published_on'][8:]
        line_txt = line_txt+day+','

        country = policy_dict['policy_source_country'][0]
        line_txt = line_txt+country+','

        cite = policy_dict['dois_cited']
        cite_count = len(cite)
        cite_total = cite_total+cite_count
        if cite_count==0:
            count_0_count = count_0_count+1
        line_txt = line_txt+str(cite_count)+','+str(cite)+'\n'

        file0.write(line_txt)
    fi.close()

# some statistics for overton data
print(count)   #1480181
#print(len(pdf_list))   #1480181
#print(len(doc_list))   #1409557
#print(eng_count)   #1358467
print(cite_total)   #2872781, here the cite means policy documents cite academic papers
print(count_0_count)    #1338972
print(cite_total/count) #1.94083

#file0.write(data_txt)
file0.close()