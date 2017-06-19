from flask import render_template,request
from webapp_zh import webapp_zh
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
    gender = request.form['gender']
    x = re.sub("\D", "", height)
    y = re.sub("\D", "", weight)
    ha = int(x)
    w = int(y)
    h = ha / 100
    bmia = h * h
    bmi = w / bmia

    return render_template('results.html',
                           the_height=height,
                           the_weight=weight, 
                           the_gender=gender,
                           the_BMI=bmi
                           )
