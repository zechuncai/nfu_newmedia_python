driver2test

英文项目名称driver2test，driver意思为："司机"，在这里是指（司机、驾考者）驾照类型；2在英语中念"two",同音"to";test意思为"测试"，为了取得驾照而需要做的题目，都是会在驾照考试中能够碰到的题目，本项目就是方便驾照考测试者进行日常试题训练。


# 简介:
运行本app，输入方面用户可以选择考试科目类型和驾照类型，两个输入皆为下拉选单；输出方面则是输出你所选择的考试科目类型和驾照类型对应匹配的科目考题、题目、图片、选项、答案以及解释；数据来源：题目中的所有内容来自聚合数据平台里的[驾照题库](https://www.juhe.cn/docs/api/id/183)。


## 输入：
用户选择考试科目和驾照类别，科目(select name = subject)选单和类别(select name = model)选单，交互界面使用到[HTML之select 表单元素](http://www.w3school.com.cn/tags/tag_select.asp)。详情请看[templates/index.html](templates/index.html)。


## 输出：
用户得到输出结果为：题目及图片、选项、答案解释。见[templates/results.html](templates/results.html)模板中body标签所包含的数据。


## 从输入到输出，除了flask模块，本组作品还使用了：

### 模块
* [requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
* [json](https://docs.python.org/2/library/json.html)

### 数据
数据来源为在发送请求到聚合数据平台里的[驾照题库](https://www.juhe.cn/docs/api/id/183)API后返回的一组大字典数据；
数据包含了题目，题目图，选项，答案和解析。


### API
* 聚合数据平台里的[驾照题库](https://www.juhe.cn/docs/api/id/183)。
* 此API需要发送的请求参数为subject（确定考试科目类型（科目一，科目四）），
  model（确定驾照类型（a1，a2，b1，b2，c1，c2））和测试类型（rand：随机测试（随机100个题目），
  order：顺序测试（所选科目全部题目）），在专题中测试类型默认为rand：随机测试。
* 发送请求后将返回请求情况（判断请求是否成功）和一组组含有题目，题目图url，选项，答案和解析的字典组。
* API请求地址：http://v.juhe.cn/jztk/query
* API请求参数：subject=++++&model=++++&testType=rand&=&key=d42c15b8e42d747c712fd15aa1509f13
* 请求方式：GET


## Web App动作描述

 以下按web 请求（web request） - web 响应 时序说明

1.後端伺服器启动：执行 run.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求



2.後端伺服器web 响应：[views.py](views.py) 中 执行 了@app.route('/') 下的 index()函数，以HTML模版[templates/results.html](templates/results.html)产出的产生《welcome to test for driver!》的HTML页面



3.前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"select"，变数名称(name)为'subject'，input 类型(type) 为"select"，变数名称(name)为'model'的两个下拉选单，详见HTML模版[templates/index.html](templates/index.html)



4.前端浏览器web 请求：用户选取指标後按了提交钮「开始做题」，则产生新的web 请求，按照form元素中定义的method='POST' action='/results'，以POST为方法，动作为/results的web 请求



5.後端服务器收到用户web 请求，匹配到@app.route('/results', methods=['POST'])的函数 index()



6.[views.py](views.py) 中 index() 函数，把用户提交的数据，以flask 模块request.form['subject'],request.form['model']取到Web 请求中，结合并整理后发送请求给聚合数据的api接口，返回一个含有题库的大数据，对大数据进行一定的处理后，提取出题目，图形，选项，答案和解释。再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出），其中模版中对应的的数据来自从大数据中提取出的变数pho，qqq，i1，i2，i3，i4，eee，gg等等



7.前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到题目的相关数据。



## 作者成员：


见[_team_.tsv](_team_/_team_.tsv)
