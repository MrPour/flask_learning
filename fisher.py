from flask import Flask

app = Flask(__name__)
# config是dict的子类
app.config.from_object('config')


# 基于函数：视图函数，controller；
# 缺点是不能继承和复用
@app.route('/hello')
def hello():
    return 'hello'


# 类视图方式需要此方法注册路由
# app.add_url_rule("/hello",view_func=hello);

# 启动web服务器
# debug=True 调试模式，服务器性能较差，网页会打印错误信息，可以热重启
# if句：当在生产环境时不会使用flask自带的服务器，所以此时不会调用
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
