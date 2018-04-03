from flask import Flask, redirect,url_for,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

#初始化
@app.route('/')
def index():
    context = {
        'username':'虚幻',
        'gender':'男',
        'age':18
    }
    # 少量参数的时候
    # return render_template('index.html',username='虚幻',gender='男')
    # 多数参数的时候
    return render_template('index.html',**context)

@app.route('/person')
def get_person():
    class Person(object):
        name = '虚幻'
        age = 18
    p = Person()
    context = {
        'username': '虚幻',
        'gender': '男',
        'age': 18,
        'person':p,
        'websites':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('person.html',**context)


@app.route('/ifdemo/<is_login>')
def ifdemo(is_login):
    if is_login == '1':
        user = {
            'username':'虚幻',
            'age':18
        }
        return render_template('ifdemo.html',user=user)
    else:
        return render_template('ifdemo.html')

#for
@app.route('/for_demo')
def for_demo():
    user = {
        'username': '虚幻',
        'age': 18
    }

    websites = ['www.a.com','www.b.com']

    for k,v in user.items():
        print(k)
        print(v)

    for website in websites:
        print(website)

    return render_template('fordemo.html',user=user,websites=websites)


@app.route('/books')
def books():
    books = [
        {
            'name':'西游记',
            'author':'啊鬼',
            'price':101
        },
        {
            'name': '水浒传',
            'author': '啊水',
            'price': 102
        },
        {
            'name': '红楼梦',
            'author': '啊黄',
            'price': 103
        },
        {
            'name': '三国演义',
            'author': '啊基',
            'price': 104
        }

    ]
    return render_template('books.html',books=books)


@app.route('/demo/<id>')
def demo(id):
    return '您请求的参数是 %s' % id

@app.route('/redirect')
def red_demo():
    cdri = url_for('c_redirect')
    # return redirect('/')
    return redirect(cdri)

@app.route('/c_redirect')
def c_redirect():
    return 'c_redirect'


if __name__ == '__main__':
    app.run()