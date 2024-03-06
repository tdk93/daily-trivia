from flask import Flask,render_template, request
import question_processor
import random 

app = Flask(__name__)

QAs = question_processor.GetQAs()

current_index = random.randint(0,len(QAs)-1)

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
    ques_index = current_index 
    ques_text = QAs[ques_index][0]
    return render_template('question.html',question=ques_text)

@app.route('/giveanswer', methods=['POST'])
def get_answer(response=None):
    response = request.form['answer']
    if response==QAs[current_index][1]: 
        result=True
    else:
        result=False

    return render_template('answer.html',result=result)
