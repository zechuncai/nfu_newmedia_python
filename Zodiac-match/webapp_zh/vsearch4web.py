 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from vsearch import get_shengxiao

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def show_search4() -> 'html':
    shengxiao = request.form['shengxiao']
    results = get_shengxiao(shengxiao)
    return render_template('C_results.html',
                           the_results=results,
                           the_shengxiao = shengxiao,
                           the_sex1 = sex1
                           the_sex2 = sex2
                           the_shengxiao1 = results[1],
                           the_shengxiao2 = results[2],
                           the_title = results[3],
                           the_content1 = results[4],
                           the_content2 = results[5],
                           the_error_code = results[6],
                           the_reason = results[7],
                           )


@app.route('/')
@app.route('/C_entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('C_entry.html',
                           the_title='欢迎来到一C组生肖匹配屋！')


@app.route('/C_viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('C_viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
