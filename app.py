from flask import flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)