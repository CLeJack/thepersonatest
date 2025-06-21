import re

import json

def process_archetype_data(string, filename, ext = '.json', path = '../res/json/'):
    items = re.split("Q\\d\\.",string) #get section title
    title = re.sub(r'\d+:* *','',items[0].strip()) #remove initial characters
    items = items[1:] # go to the remaining data
    items = list(map(lambda x:  x.split('\n'),items)) # split to list
    items = list(map(lambda x: {'id':x[0],'question':x[1][0].strip(), 'answers':x[1][1:]},enumerate(items))) #set questions and remaining answers
    for m in items:
        m['answers'] = list(filter(lambda x: not(x==''),m['answers'])) #filter empty content
        m['answers']= list(map(lambda x: (x,re.search(r"- *\[(\w+)\].*",x).group(1)),m['answers'])) #split answer and id
        m['answers'] = list(map(lambda x: {'id':x[0], 'category':x[1][1], 'val':re.sub('- *\\[\\w+\\] *','',x[1][0]) },enumerate(m['answers']))) #map answer and id

    
    results = {'title':title,'items':items}
    with open(path+filename+ext, 'w') as f:
        f.write(json.dumps(results))
    return results

def process_mode_data(string, filename, ext = '.json', path = '../res/json/'):
    items = list(filter(lambda x: not(x==''),string.split('\n'))) #get section title
    title = re.sub(r'\d+:* *','',items[0].strip())# clean title
    items = items[1:] #get remaining data
    items = list(map(lambda x: re.sub(r'Q\d+\. *','',x), items)) #clean initial elements
    items = list(map(lambda x: x.split('|'), items)) #separate questions from mode
    items = list(map(lambda x: {'id':x[0], 'category':x[1][1], 'question':x[1][0]}, enumerate(items)))

    results = {'title':title,'items':items}
    with open(path+filename+ext, 'w') as f:
        f.write(json.dumps(results))
    return results

def get_data(path = '../res/extracts/extended-test.txt'):
    data = ''

    with open(path,'r') as f:
        data = f.read()

    data = data.split("PHASE")[1:]
    return data