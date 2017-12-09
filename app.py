from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'this is home page'


@app.route('/profile/<username>')
def profile(username):
    return "<h1>hello %s<h1>" % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h1>post ID is %s<h1>" % post_id


@app.route('/beacon', methods=['GET', 'POST'])
def beacon():
    if request.method == 'POST':
        return 'you are using POST'
    else:
        return 'you are using GET'


if __name__ == "__main__":
    app.run(debug=True)
