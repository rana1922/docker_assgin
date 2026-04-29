from flask import Flask , request, jsonify

app = Flask(__name__)

@app.route('/')
def form():
    return jsonify({'message': "Hello to my 1st project"})


@app.route('/register', methods = ['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)

    return jsonify({
    "message": "Registration successful",
    "username": username
})


if __name__ == '__main__':
    app.run(port = 8000 , host = '0.0.0.0' , debug=True)