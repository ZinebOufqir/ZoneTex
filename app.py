from flask import Flask, render_template,request,redirect,url_for,flash,session,Response
import pickle
import folium 
import numpy as np
from flask_material import Material
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
import matplotlib.pyplot as plt 
model = keras.models.load_model('./static/model3.h5')


app=Flask(__name__)
Material(app)
@app.route('/')
@app.route('/login.html',methods=["POST","GET"])
def login():
        return render_template('login.html')
@app.route('/validation',methods=["POST","GET"])
def validation():
    email=request.form.get("login")
    passw=request.form.get("password")
    if email=="admin" and passw=="admin123":
        return render_template('form.html')
@app.route('/predict.html',methods=['POST','GET'])
def pr():
    return render_template('predict.html')
@app.route('/takeval',methods=['POST','GET'])
def takeval():
    L=[]
    for i in range(1,36):
        L.append(int(request.form.get(("post{}").format(i))))
    P=[1,2,3,4,5,1,5,7,8,4,2,1,2,4,2,3,4,5,2,1,3,2,4,5,1,2,3,2,1,4,2,3,5,3,2]
    prediction=model.predict(np.array([L]))
    print(prediction)
    global zone
    zone=["Nouacer","Bouskora ","Moulay Rachid","Ain Sebaa","Tit Mellil","Mohammedia","Martil","Sidi Ghanem","beni mellal","Technopolis","Bouknadel"]
    datanum=list(prediction[0])
    
    #datanum=["{:.2f}".format(item*100) for item in datanum]
    #print(datanum)
    #print(datanum)
    data=list(zip(zone,datanum))
    data.sort(key = lambda x: x[1], reverse=True)
    print(data)

    print(datanum)
    global z
    z=zone[list(prediction[0]).index(max(list(prediction[0])))]
    return render_template('predict.html',data=data)

@app.route('/form.html',methods=['POST','GET'])
def fr():
    return render_template('form.html')
@app.route('/test.html')
def test():
    return render_template('test.html')
@app.route('/map',methods=['POST','GET'])
def map():
    geo=[[33.33738030362776, -7.594510286989891],[33.44041998790594, -7.649805370928761],[33.564306780081374, -7.52437612782747],[33.63012482457402, -7.504562929601083],[33.53776381323252, -7.491694070678882],[33.662361976777255, -7.407177710163049],[35.60724260657122, -5.310280272402154],[31.67479816342163, -8.048540057131845],[32.30593936715627, -6.417246475294174],[34.0357722260949, -6.772147404089168],[34.108839219424134, -6.697959400411176]]
    zone=["Nouacer","Bouskora ","Moulay Rachid","Ain Sebaa","Tit Mellil","Mohammedia","Martil","Sidi Ghanem","beni mellal","Technopolis","Bouknadel"]
    index=zone.index(z)

    m3=folium.Map(location=geo[index],zoom_start=20)
    folium.Marker(location=geo[index],popup='Default popup Marker1',tooltip='Click here to see Popup').add_to(m3)
    m3.save('templates/map.html')
    
    return render_template('map.html')

if __name__=="__main__":
    app.run(debug=True)