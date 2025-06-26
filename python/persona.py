import re

import json

def process_archetype_data(string, offset = 0):
    items = re.split("Q\\d\\.",string) #get section title
    title = re.sub(r'\d+:* *','',items[0].strip()) #remove initial characters
    items = items[1:] # go to the remaining data
    items = list(map(lambda x:  x.split('\n'),items)) # split to list
    items = list(map(lambda x: {'id':x[0] + offset,'prompt':x[1][0].strip(), 'responses':x[1][1:]},enumerate(items))) #set questions and remaining responses
    for m in items:
        m['responses'] = list(filter(lambda x: not(x==''),m['responses'])) #filter empty content
        m['responses']= list(map(lambda x: (x,re.search(r"- *\[(\w+)\].*",x).group(1)),m['responses'])) #split answer and id
        m['responses'] = list(map(lambda x: {'id':x[0], 'category':x[1][1], 'val':re.sub('- *\\[\\w+\\] *','',x[1][0]) },enumerate(m['responses']))) #map answer and id

    
    results = {'title':title,'items':items}

    return results

def process_mode_data(string, offset = 0):
    items = list(filter(lambda x: not(x==''),string.split('\n'))) #get section title
    title = re.sub(r'\d+:* *','',items[0].strip())# clean title
    items = items[1:] #get remaining data
    items = list(map(lambda x: re.sub(r'Q\d+\. *','',x), items)) #clean initial elements
    items = list(map(lambda x: x.split('|'), items)) #separate questions from mode
    items = list(map(lambda x: {'id':x[0], 'category':x[1][1], 'val':x[1][0]}, enumerate(items)))
    prompt = 'Given the recent occurences in your life, what statement resonates with you the strongest?'
    items = [{'id':0 + offset, 'prompt': prompt, 'responses': items}]

    results = {'title':title,'items':items}
    
    return results

def write_json(data, filename, ext = '.json', path = '../res/json/'):
    with open(path+filename+ext, 'w') as f:
        f.write(json.dumps(data))

def get_data(path = '../res/extracts/extended-test.txt'):
    data = ''

    with open(path,'r') as f:
        data = f.read()

    data = data.split("PHASE")[1:]
    return data