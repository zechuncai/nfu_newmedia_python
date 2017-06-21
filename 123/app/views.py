from flask import render_template,request
from app import app
import re

@app.route('/')
@app.route('/index')
def index():
    return render_template("forms.html",
        )

@app.route('/results', methods=['POST'])
def BMI() -> 'html':
    height = request.form['height']
    weight = request.form['weight']
    x = re.sub("\D", "", height)
    y = re.sub("\D", "", weight)
    ha = int(x)
    w = int(y)
    h = ha / 100
    bmia = h * h
    bmi = w / bmia
    result = []
    if bmi <24:
        if bmi <18.5:
            result.append("你的体重过轻")
        else:result.append("恭喜你你的BMI指数在正常范围，保持好你的体重吧！")    
    elif 24 < bmi <27:
        result.append("你的BMI指数告诉你你可算是过重了哦")
    elif 27 < bmi <32:
        result.append("你现在是属于肥胖了，不是“微胖”哦")
        
    else: result.append("哎呀，你一定是非常胖了，是个大胖子了吧")
 
    
    
        
    return render_template('results.html',
                           the_height=height,
                           the_weight=weight, 
                           the_BMI=bmi,
                           the_result=result
                           )
