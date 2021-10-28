####### USUAL
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy



###### APP & DB
app = Flask(__name__)



###### HOMEPAGE
# View for link '/' i.e.. home page is defined here
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')



###### RUN 
if __name__ == "__main__":
    app.run(debug=True)
#############################################