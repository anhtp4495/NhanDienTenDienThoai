import sys
sys.dont_write_bytecode = True
import flask
#import predict
#import predict_symbol
import NERresult
app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("index.html")

'''
@app.route("/get")
def get_bot_response():
    user_input = flask.request.args.get('msg')
    return predict.response(user_input)
'''
@app.route("/get")
def get_bot_response():
    user_input = flask.request.args.get('msg')
    return NERresult.response(user_input)
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)

