from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = "banana"

#handles first request
@app.route('/')
def visits():
    if 'count' in session:
        session['count'] += 1
        print("count exists")
    else:
        session['count'] = 1
        print("key 'count does NOT exist")
    return render_template("visits.html")

#adds two visits to the page
@app.route('/add_two')
def add():
    session['count'] += 1
    return redirect('/')

#this clears the count
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)