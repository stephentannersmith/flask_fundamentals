from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruit_total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    fruits = {
        'strawberry': request.form['strawberry'],
        'raspberry': request.form['raspberry'],
        'apple': request.form['apple'],
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'student_id': request.form['student_id'],
        'total_count': fruit_total,
        'order_date': datetime.today().strftime('%B %d' + ' at ' + ' %I:%M:%S %p')
    }
    print("Charging {} {} for {} fruits".format(request.form['first_name'], request.form['last_name'], fruit_total))
    return render_template("checkout.html", fruits=fruits)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    