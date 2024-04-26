from flask import Flask, render_template, request, jsonify


from chat import get_conversation


# Initializing flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get')
def get_messages():
    userText = request.args.get('msg')
    response = get_conversation(userText)
    #print(response)
    return response

     
# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=True)