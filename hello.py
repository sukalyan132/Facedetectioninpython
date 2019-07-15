from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]


@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()