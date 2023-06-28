
from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

import pickle

model = pickle.load(open(r'model.pkl','rb'))

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/home')
def homePage():
    return render_template('index.html')

@app.route('/form')
def formPage():
    return render_template('formPage.html')

@app.route('/profile')
def profile():
    return render_template('spacexAnalysis.html')

@app.route('/predict',methods=['POST'])
def predictPage():
    booster_version = int(request.form['booster_version'])
    launch_site = int(request.form['launch_site'])
    orbit = int(request.form['orbit'])
    payload_mass = int(request.form['payload_mass'])
    customer = int(request.form['customer'])
    misson_outcome = int(request.form['misson_outcome'])
   
    dfT = pd.DataFrame(columns = ['Booster_Version', 'Launch_Site', 'PAYLOAD_MASS__KG_', 'Orbit', 'Customer','Mission_Outcome'], data = [[booster_version,launch_site,payload_mass,orbit,customer,misson_outcome]])
    print(dfT)
    prediction = model.predict(dfT)
    if prediction[0] == 0:
        statement = "Failure"
    else:
        statement = "Successfull"
    return render_template('result.html',y=statement)




if __name__ == '__main__':
    app.run(debug=True, port = 5000)

