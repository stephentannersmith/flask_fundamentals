from flask import Flask, request, redirect, session, render_template
import random
app = Flask(__name__)
app.secret_key = "coding dojo"

@app.route('/')
def index():
    if "random_number" not in session:
        session['random_number'] = random.randint(1, 100)
    if "num_guesses" not in session:
        session['num_guesses'] = 0

    game_info = {
        "message": None,
        "css_class": None
    }
    if "guess" not in session:
        game_info['message'] = "Take a guess!"
    elif session["guess"] > session["random_number"]:
        game_info["message"] = "Too high!"
    elif session["guess"] < session["random_number"]:
        game_info["message"] = "Too low!"
    else:
        game_info["message"] = f"{session['random_number']} was the number!"
        game_info['css_class'] = "green"
    return render_template('index.html', info=game_info)

@app.route('/guess', methods=["POST"])
def process():
    session['guess'] = int(request.form['guess'])
    session["num_guesses"] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)