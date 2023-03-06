import csv
import pandas as pd
from flask import Flask, render_template,request
from predict import model,x,le

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    job_post = request.form.getlist('job_post')
    required_skills = request.form.getlist('required_skills')
    exp_required = request.form.getlist('exp_required')
    salary_offered = request.form.getlist('salary_offered')
    job_location = request.form.getlist('job_location')
    company_rating = request.form.getlist('company_rating')
    company_review = request.form.getlist('company_review')
    info = [job_post,company_rating,company_review,exp_required,salary_offered,job_location,required_skills]
    dict1 = {}
    for i in range(len(info)):
        dict1[x.columns[i]] = info[i]
    res = pd.DataFrame(dict1, index=[0])
    for i in res.columns:
        if i != "company_rating" and i != "company_review":
            res[i] = le.fit_transform(res[i])
    company_name = model.predict(res)
    return render_template("result.html", company = company_name)


app.run(debug =  True)