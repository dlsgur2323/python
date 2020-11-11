from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    print(value)
    return render_template('default.html',
                           mytitle=value,
                           mylist=[ x + 1 for x in range(30)]
                        )



if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
    
