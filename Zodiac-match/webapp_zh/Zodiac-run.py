 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request
from Zodiac import get_shengxiao

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    shengxiao1 = request.form['shengxiao1']
    shengxiao2 = request.form['shengxiao2']
    results = get_shengxiao(shengxiao)
    return render_template('C_results.html',
                           the_results=results,
                           the_shengxiao = shengxiao,
                           the_shengxiao1 = results[1],
                           the_shengxiao2 = results[2],
                           the_title = results[3],
                           the_content1 = results[4],
                           the_content2 = results[5],
                           the_reason = results[6])



@app.route('/')
@app.route('/C_entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('C_entry.html',
                           the_title='欢迎来到一C组生肖匹配屋！')



if __name__ == '__main__':
    app.run(debug=True)