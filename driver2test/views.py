from flask import Flask,render_template,request
app = Flask(__name__)
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
    
        
    _text_ = '''
     大型客车 A1 可以开 大型载客汽车 和B1,B2,C1,C2,C3,C4,M 车型
     牵引车 A2 可以开 重型、中型全挂、半挂汽车列车 和B1,B2,C1,C2,C3,C4 ,M 车型
     城市公交车 A3 可以开 核载10人以上的城市公共汽车和C1,C2,C3,C4 车型
     中型客车 B1 可以开 中型载客汽车(含核载10人以上、19人以下的城市公共汽车)和 C1、C2、C3、C4、M 车型
     大型货车 B2 可以开 重型、中型载货汽车和C1,C2,C3,C4 车型
     小型汽车 C1 可以开 小型 、微型载客汽车和C2,C3,C4 车型
     小型自动挡汽车 C2 可以开 小型、微型自动挡载客汽车以及轻型、微型自动挡载货汽车
     低速载货汽车 C3 可以开 低速载货汽车(原四轮农用运输车) 和C4车型
     三轮汽车 C4 可以开 三轮汽车(原三轮农用运输车)
     '''

    lines = [x.strip() for x in _text_.splitlines() if x.strip()!='']
    items = [x.split(' ') for x in lines]
    code_2_name = { i[1]:i[0] for i in items }
    code_2_description = { i[1]:"".join(i[2:]) for i in items }
    code_2_api_code = {'a1': 'A1',
                 'a2': 'A2',
                 'b1': 'B1',
                 'b2': 'B2',
                 'c1': 'C1',
                 'c2': 'C2'}
    
    mmodel = code_2_api_code[stepB]
    mmodel_name = code_2_name[mmodel]
    mmodel_description = code_2_description[mmodel]
    
    
    
        
        
    return render_template('result.html',
                            the_photo_1=photo_1,
                            the_qqq=qqq,
                            the_i1=i1, 
                            the_i2=i2,
                            the_i3=i3,
                            the_i4=i4,
                            the_aaa=aaa, 
                            the_eee=eee,
                            the_mmodel_name=mmodel_name,
                            the_mmodel_description=mmodel_description
                      )
if __name__ == '__main__':
    app.run(debug=True)

