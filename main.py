from flask import Flask, request, Response,render_template
app = Flask(__name__)
import pickle as pk
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

data=pd.read_csv('C:\\Users\\Adii\\Desktop\\CROP_RECOMM\\Crop_recommendation (1).csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)
st=StandardScaler()
x_train=st.fit_transform(x_train)
x_test=st.fit_transform(x_test)

myarray=['apple.html', 'banana.html', 'blackgram.html', 'chickpea.html', 'coconut.html', 'coffee.html',
       'cotton.html', 'grapes.html', 'jute.html', 'kidneybeans.html', 'lentil.html', 'maize.html',
       'mango.html', 'mothbeans.html', 'mungbean.html', 'muskmelon.html', 'orange.html', 'papaya.html',
       'pigeonpeas.html', 'pomegranate.html', 'rice.html', 'watermelon.html']


model=pk.load(open('model.pkl','rb'))
@app.route('/',methods=['GET','POST'])
def index():
    return render_template("page.html")
@app.route('/org',methods=['GET','POST'])
def organi():
    return render_template("organic.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        nitrogen=float(request.form.get('nitrogen'))
        phosphorus=float(request.form.get('phosphorus'))
        Potassium=float(request.form.get('Potassium'))
        temperature=float(request.form.get('temperature'))
        humidity=float(request.form.get('humidity'))
        pH=float(request.form.get('pH'))
        rainfall=float(request.form.get('rainfall'))
    
    m=st.transform(np.array([[nitrogen ,	phosphorus,	Potassium,	temperature,	humidity	,pH ,	rainfall]]))
    
    pred=int(model.predict(m))


    
    return render_template(myarray[pred],nitrogen=nitrogen,phosphorus=phosphorus,Potassium=Potassium,temperature=temperature,humidity=humidity,pH=pH,rainfall=rainfall)


if __name__ == '__main__':
    app.run(debug=True)