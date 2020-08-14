from flask import Flask , render_template, request
#from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pickle


app = Flask(__name__)





file=open('mk.pkl' , 'rb')
model= pickle.load(file)
file.close()

@app.route('/' , methods=[ "GET","POST"])
def index():
        if request.method == "POST" :
                
                my = request.form
                dd = int(my["hrs"])
                feature=[dd]
                inf = model.predict([feature])
                return render_template('sh.html' , inf=inf)
        return render_template('ss.html' )
        
if __name__ == '__main__':
    app.run(debug=True)