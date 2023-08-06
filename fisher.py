from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
# config是dict的子类
app.config.from_object('config')


# 基于函数：视图函数，controller；
# 缺点是不能继承和复用
@app.route('/hello')
def hello():
    return 'hello'


# 重定向测试，手动创建response对象
@app.route('/redirect')
def redirect_test():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


# response对象以元组的形式自动封装返回前端
@app.route('/response')
def response_test():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }

    return '<html></html>', 301, headers


# response对象以元组的形式自动封装返回前端
@app.route('/book/search/<q>/<page>')
def book_search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    pass


# 类视图方式需要此方法注册路由
# app.add_url_rule("/hello",view_func=hello);

# 启动web服务器
# debug=True 调试模式，服务器性能较差，网页会打印错误信息，可以热重启
# if句：当在生产环境时不会使用flask自带的服务器，所以此时不会调用
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
