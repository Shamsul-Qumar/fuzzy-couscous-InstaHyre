import numpy as np
import pandas as pd
from collections import Counter
from flask import Flask, request, render_template
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("Phase - 2/app/Merged_Data.csv")

arr = []
for i in df['Skills']:
    skills = i.split(',')
    for j in skills:        
        a = j.split(',')[0].strip()
        arr.append(a)
    arr = list(set(arr))
    # arr.sort()


skill_array_for_fuzzy_wuzzy=arr
lst=[]
for i in skill_array_for_fuzzy_wuzzy:
    lst.append(i)


def input_match(x):
    final_keyword = []
    input_variable = []
    input_variable.append(x)
    choices = lst
    for i in input_variable: 
        a = process.extract(i, choices)
        first_match = a[0] 
        convert_list = list(first_match)
        final_keyword.append(convert_list[0])
        final_keyword=final_keyword[0]
   
    return(final_keyword)

def skillinput(x):
    arr = []
    for i in df['Skills']:
        skills = i.split(',')
        for j in skills:        
            a = j.split(',')[0].strip()
            arr.append(a)
    arr = list(set(arr))
    y = []
    skills=arr
    if x in skills:
        y.append(x.lower())
    else:
        x = x + ","
        x=x.lower()
        x=x.strip()
        x=x.split(',')
        for i in range(len(x)):
            x[i]=x[i].strip()
        y=x
        y.remove('')
    return y



def data(x):
    x=skillinput(x)
    y=df.Skills.str.split(',')
    for i in y:
        for g in range(len(i)):
            i[g]=i[g].lower()
            i[g]=i[g].strip()
    df1=pd.DataFrame()
    ind=[]
    for i in x:
        for j in range(len(y)):
            if i in y[j]:
                ind.append(j)

    ind=sorted(list(set(ind)))
    df1=df[df.index.isin(ind)]
    if len(df1)<1:
        return 'No Jobs Found For This Skill'
    else:
        df1['Sr. No.'] = [f"{i})." for i in range(1,len(df1)+1)]
        return df1[['Sr. No.','Job_Designation', 'Experince_level', 'Hr_name', 'Skills', 'CompanyName', 'Company_estab_year', 'Industry', 'Location', 'employees_count','Class', 'Job_url']]
    
def fetch_data(skill):
    s=data(skill)
    if type(s)==str:
        return None
    else:
        df1=data(skill)
        most_common_class=df1['Class'].mode()[0]
        most_common_industry=df1['Industry'].mode()[0]
        most_common_experience_level=df1['Experince_level'].mode()[0]
        job_count=df1['Job_Designation'].count()
        return most_common_experience_level, most_common_industry, most_common_class, job_count



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Predict', methods=['POST'])

    
def predict():
    input_1 = []
    if request.method == 'POST':
        skill = request.form["skill"]
        inp = list(skill.split(','))
        inp = list(inp)
        for i in inp:
            i=i.strip()
            i=input_match(i)
            input_1.append(i)
        skill = ', '.join(input_1)

    
        most_common_experience_level, most_common_industry, most_common_class, job_count = fetch_data(skill)
        return render_template('result.html',
                               skill=skill,
                               experience_level=most_common_experience_level,
                               industry=most_common_industry,
                               job_class=f"Class : {most_common_class}",
                               job_count=job_count)
    
@app.route('/job_details/<s_id>', methods=['GET'])
def job_details(s_id):
    skill = s_id
    job_data = data(skill).to_html(render_links=True, classes='table table-bordered', index=False)  # Filter the data based on the provided skill   
    return render_template('job_details.html', job_data=job_data)

if __name__ == "__main__":
    app.run(debug=True)

