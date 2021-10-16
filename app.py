from flask import Flask, request

app = Flask(__name__)

@app.route('/json-example', methods=['GET', 'POST'])
def json_example():
    request_data = request.get_json()
    age = request_data['age'] +10
    request_data['age']=age
    return request_data
           

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000) 