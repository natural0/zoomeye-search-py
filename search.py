#coding=utf-8
import requests
import json
access_token = ''
ip = ''
def login():
    user = 'mc2233441@163.com'
    passwd = 'mc2233441'
    data = {
        'username':user,
        'password':passwd
    }
    data_encode = json.dumps(data)
    r = requests.post(url =  'https://api.zoomeye.org/user/login',data = data_encode)
    r_decode = json.loads(r.text)
    global run
    global test
    run = r_decode['access_token']
    print run
login()
def search():
    test = 'Authorization JWT' + run
    headers = {
         'Authorization' : 'JWT ' + run, 
         }
    question = raw_input('question>')
    port = raw_input('port>')
    global header_decode
    header_decode = json.dumps(headers)
    while(True):
        page = raw_input('page>')
        r = requests.get(url = 'https://api.zoomeye.org/host/search?query="' + question + '"port:' + port + '%20city:beijing&page=' + page +'&facet=app,os', headers = headers)
        header_recode = json.loads(r.text)
        for x in header_recode['matches']:
            print x['ip']
search()
