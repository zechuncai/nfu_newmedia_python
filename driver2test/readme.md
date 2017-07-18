driver2test

英文项目名称driver2test


简介


运行本app，输入选择所要考的科目，和驾照类型，两个输入位下拉选单，输出方面则是输出你所想要的对应的科目考题，题目，图片，选项，答案和解释。题目所有内容来自网络上的平台：聚合数据平台


输入：


选择的是科目和类别，交互页面使用到HTML之body标签。详情请看templates/index.html模板。


输出：


用户得到输出结果为：题目及图片，选项，答案解释。见templates/results.html模板中body标签所包含的数据。


从输入到输出，除了flask模块，本组作品还使用了：


模块


requests，json，render_requests


数据


数据来源为在发送请求到api后返回的一组大数据。


API


聚合数据平台驾照题库。



Web App动作描述



以下按web 请求（web request） - web 响应 时序说明



後端伺服器启动：执行 run.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求



後端伺服器web 响应：views.py 中 执行 了@app.route('/') 下的 index()函数，以HTML模版templates/index.html产出的产生《welcome to test for driver!》的HTML页面



前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"select"，变数名称(name)为'subject'，input 类型(type) 为"select"，变数名称(name)为'model'的两个下拉选单，详见HTML模版templates/index.html



前端浏览器web 请求：用户选取指标後按了提交钮「开始做题」，则产生新的web 请求，按照form元素中定义的method='POST' action='/results'，以POST为方法，动作为/results的web 请求



後端服务器收到用户web 请求，匹配到@app.route('/results', methods=['POST'])的函数 index()



views.py 中 index() 函数，把用户提交的数据，以flask 模块request.form['subject'],request.form['model']取到Web 请求中，结合并整理后发送请求给聚合数据的api街口，返回一个含有题库的大数据，对大数据进行一定的处理后，提取出题目，图形，选项，答案和解释。再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中对应的的数据来自从大数据中提取出的变数pho，qqq，i1，i2，i3，i4，eee，gg等等



前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。



作者成员：



见team/team.tsv
