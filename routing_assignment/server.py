from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    if type(name) == str:
        return "Hi, " + name
    else:
        print("Strings only please.")

@app.route('/repeat/<multiple>/<request>')
def repeater(multiple, request):
    if multiple.isdigit() and type(request) == str:
        return request * int(multiple)

if __name__ == "__main__":
    app.run(debug=True)