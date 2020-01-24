from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#index route defines form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def create_user():
    print("Got user data")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['dojo_location']
    language_from_form = request.form['fav_language']
    comments_from_form = request.form['comment']
    return render_template('result.html', name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comments_on_template=comments_from_form)

if __name__ == "__main__":
    app.run(debug=True)