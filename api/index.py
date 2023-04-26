from flask import Flask, render_template
from random import randint

app = Flask(__name__)
canning = [
            '南大米', '北大米', '顺溜', '牛蛙', '饺子', '陈香贵', '干锅', '麻辣烫', '肯德基', '老乡鸡', '再抽一次',
            '陕老顺', '那个绿色的店'
        ]


@app.route('/index')
def index():
    return 'hhhh'
    # return render_template('index.html', canning=canning)

