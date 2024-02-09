from flask import Flask,render_template, request

app = Flask(__name__)

QUES1="What is the capital of India?"
ANS1 = "Delhi"
QAs = [(QUES1,ANS1)]
CURRENT_QUES=0



@app.route('/')
def hello():
    return 'Hello, !'

@app.route('/mymessage', methods=['GET'])
def my_message(message=None):
    message = request.args.get('message')
    print("message = is ", message)
    return render_template('message.html',message=message)

@app.route('/getques')
def show_question():
    ques_index = CURRENT_QUES
    ques_text = QAs[ques_index][0]
    return render_template('question.html',question=ques_text)

@app.route('/giveanswer', methods=['GET'])
def get_answer(response=None):
    response = request.args.get('response')
    if response==QAs[CURRENT_QUES][1]:
        result=True
    else:
        result=False

    return render_template('answer.html',result=result)




