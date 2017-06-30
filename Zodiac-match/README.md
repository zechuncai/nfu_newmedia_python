#Zodiac Match House
英文项目：Zodiac Match House，Zodiac的中文是十二宫位，在外国对应的是十二星座，而在中国则对应的是十二生肖。Match是匹配的意思，本项目则是中国的十二生肖男女匹配信息。
-------------------

		
## 简介： 
> **通过生肖匹配平台，帮助用户查询匹配信息。**</br>
> **输入方面用户可输入想查询生肖（如“虎”和“牛”），输出方面则是查询的两个测试者的生肖是否配对及其评价信息，分别输出生肖男生肖女的交叉匹配资料，共144种匹配资料。**</br>
> **数据来源为[DT阿凡达数据](http://api.avatardata.cn/ShengXiaoPeiDui/Lookup?key=b27767d0aecb4ed7b70333b213a24464&shengxiao1={name}&shengxiao2={name})取得的的api数据库和手动添加的生肖类型的tsv档。**</br>
> **可供选择以下生肖：**</br>
> - 鼠
> - 牛
> - 虎
> - 兔
> - 龙
> - 蛇
> - 马
> - 羊
> - 猴
> - 鸡
> - 狗
> - 猪

### 输入：
> **用户选择两个匹配者的生肖，交互界面使用到[HTML之select元素]，显示的是生肖，其对应值是生肖。所以代码文件可以找到所需要的生肖。**

#### 输出：
> **两个生肖的男女交叉匹配资料**</br>
> **两个测试者的生肖**</br>
> **是否配对及其评价信息资料**</br>

##### 从输入到输出，本组作品使用了：
###### 数据
> **由于api无匹配者的生肖资料档，所以手动生成生肖类型的tsv档，在文件中读入，并做成字典读出相对应的内容**</br>

###### 模块
> - [json](http://www.json.org/json-zh.html)</br>
> - [requests](http://cn.python-requests.org/zh_CN/latest/)</br>
> - [urllib](https://baijiahao.baidu.com/po/feed/share?wfr=spider&for=pc&context=%7B"sourceFrom"%3A"bjh"%2C"nid"%3A"news_3437549851525350677"%7D)</br>
> - [flask](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832805619b3e68a9cf16c4d0398d8af8f6d50e740000)</br>

###### API
> - 来源： [DT阿凡达数据](http://api.avatardata.cn/ShengXiaoPeiDui/Lookup?key=b27767d0aecb4ed7b70333b213a24464&shengxiao1={name}&shengxiao2={name})


#### Web APP动作描述

> - 以下按web 请求（web request） - web 响应 时序说明

> - 後端伺服器启动：执行 Zodiac_run.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

> - 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

> - 後端伺服器web 响应：Zodiac_run.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/C_entry.html及一个含指标代码及名称的字典（见代码entry_shenxiao_list=r_list ）产出的产生《欢迎来到欢迎来到一C组生肖匹配屋！》的HTML页面

> - 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 select元素 变数名称(name) 为"text"，变数名称(name)为'shengxiao1'，'shengxiao2'使用了HTML5的select元素,详见HTML模版templates/C_entry.html

> - 前端浏览器web 请求：用户选取指标後按了提交钮「开始匹配！」，则产生新的web 请求，按照form元素中定义的method='POST' action='/search4'，以POST为方法，动作为/search4'的web 请求

> - 後端服务器收到用户web 请求，匹配到@app.route('/search4', methods=['POST'])的函数 do_search()

> - Zodiac_run.py 中 def do_search() 函数，把用户提交的数据，以flask 模块request.form['shengxiao1'],['shengxiao2']	取到Web 请求中，HTML表单变数名称shengxiao1,shengxiao2的值，存放在shengxiao_1,shengxiao_2这Python变数下，再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中results_001,results_002,results_003,results_004的值，用the_shengxiao1,the_shengxiao2,the_content1,the_content2这变数之值，其他4项值如此类推。

> - 前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。


### 作者成员：
> ** 见[_team_.tsv](webapp_zh/_team_/_team_.tsv)

> - Gwenshiga</br>
> - CherryLichan</br>
> - HuangJiaLi</br>
> - q3466141541</br>
> - JiawenLai</br>
> - ChanJuanLai</br>



