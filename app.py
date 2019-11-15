from flask import Flask, url_for, request, json, jsonify
import stringsim

s = stringsim.StringSim()
app = Flask(__name__)
stored_data = "Data Engineer Coding Challenge"

@app.route('/')
def api_root():
    return 'Welcome'
        
@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
        
@app.route('/challenge', methods = ['GET', 'POST'])
def api_message():
    if request.method=='POST':
        if request.headers['Content-Type'] == 'application/json':
            str1 = request.json['sample1']
            str2 = request.json['sample2']
            score = round(s.run(str1, str2)['Score'][0],3)
            global stored_data
            stored_data = json.dumps({"sample1":str1, 
                                      "sample2":str2, 
                                      "similarity":score})
            return stored_data

        else:
            return "415 Unsupported Media Type ;)"
    else:
        return stored_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)