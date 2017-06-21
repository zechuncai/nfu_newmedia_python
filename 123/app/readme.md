BMI

英文项目名称BMI

简介

根据输入框输入对应信息并得出BMI指数

输入：

用户输入身高和体重

输出：

用户得到输出结果为：身高体重和根据用户给予的数据所算出的BMI值

从输入到输出，除了flask模块，本组作品还使用了：

模块
render_template,request

数据

本组并未使用数据。
API

本组并未执行其他数据清理工作。
Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 run.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：views.py 中 执行 了@app.route('/') 下的 index 函数，以HTML模版templates/forms.html及《welcome to BMI test!》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)分别为'weight'和‘height’。

前端浏览器web 请求：用户输入对应数据后按提交按钮「submit」，则产生新的web 请求，按照form元素中定义的method='POST' action='/results'，以POST为方法，动作为/rusult的web 请求

後端服务器收到用户web 请求，匹配到@app.route('/results', methods=['POST'])的函数 BMI（）

views.py 中 def BMI() 函数，把用户提交的数据，以flask 模块request.form取到Web 请求中，得出BMI值和对用户BMI值的评价

前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

作者成员：

见team/team.tsv
