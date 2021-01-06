from flask import Flask,request,jsonify,render_template, json, redirect
import torch
import pandas as pd
from bert_predict import get_result
# Use torch to load in the pre-trained model

# Initialise the Flask app
app = Flask(__name__, static_url_path='/static')

# Set up the main route
@app.route('/predict',methods=['POST'])
def predict():
    # Extract the input
    para = request.form['para']
    qstn = request.form['question']
    print(para)
    print(qstn)
    ans = get_result(qstn, para)
    print(ans)
    f = open("perturbations.txt", "a")
    f.write("Paragraph: " +para+ "\n")
    f.write("Q: "+ qstn +" , A: "+ ans +"\n")
    f.close()
    return ans


@app.route('/submit',methods=['POST'])
def submit():
    # Extract the input
    print("Submit")
    para = request.form['para']
    qstn = request.form['question']
    ans = get_result(qstn, para)
    f = open("submissions.txt", "a")
    f.write("\nParagraph: " +para+ "\n")
    f.write("\nQ: "+ qstn +" , A: "+ ans +"\n")
    f.close()
    return ans


@app.route('/')
def render_page1():
    return redirect("/0")

@app.route('/<n>')
def render_home(n):
    all_data = json.load(open("./data.json"))
    data = all_data[int(n)]
    return render_template('home.html', data=data)

@app.route('/tutorial')
def render_tutorial():
    return render_template('tutorial.html')

@app.route('/samples')
def render_samples():
    return render_template('samples.html')

@app.route('/adversary_ex')
def render_adversary_ex():
    return render_template('adversary_ex.html')


# @app.route('/next',methods=['GET'])
# def render_next_page():

#     return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)