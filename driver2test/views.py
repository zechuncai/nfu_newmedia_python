from flask import Flask,render_template,request
from driver2test import app
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                    )

@app.route('/results', methods=['POST'])
def result() -> 'html':
    stepA=request.form['subject']
    stepB=request.form['model']
    
    url_api = "http://v.juhe.cn/jztk/query"
    parameters = {'subject': stepA, 
             'model': stepB,
             'TestType': 'rand',     
             'key':'d42c15b8e42d747c712fd15aa1509f13'}
    
    r = requests.get (url_api, params=parameters)
    r = r.json()
    s = r['result']
    ss = s[0:10]
    s1 =s[0]
    
    
    pho = s1['url']
    qqq = s1['question']
    i1 = s1['item1']
    i2 = s1['item2']
    i3 = s1['item3']
    i4 = s1['item4']
    gg= s1['answer']
    eee = s1['explains']
    photo_1=[]

    if pho == '':
        photo_1='文字题'
    else:
        photo_1=pho
    
        
    if len(i3):
        ottf = ['1','2','3','4']
        abcd = ['A','B','C','D']
        change = dict(zip(ottf,abcd))
        
    else:
        ot = ['1','2']
        dc = ['正确','错误']
        change = dict(zip(ot,dc)) 
    
        
    
    aaa = change[gg]
        
        
        
        
    return render_template('result.html',
                            the_photo_1=photo_1,
                            the_qqq=qqq,
                            the_i1=i1, 
                            the_i2=i2,
                            the_i3=i3,
                            the_i4=i4,
                            the_aaa=aaa, 
                            the_eee=eee
                      )


