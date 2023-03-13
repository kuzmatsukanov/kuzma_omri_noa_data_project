from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/get_recommendation')
def get_recommendation():
    # Get the parameters from the query string
    user_image = request.args.get('user_image', type=float)

    # Returns the model prediction
    return str('hello')


if __name__ == '__main__':
    app.run()
