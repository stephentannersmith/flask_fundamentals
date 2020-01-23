from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/')
def index():
    return render_template('index.html', box_number=3)

@app.route('/play/<times>')
def play(times):
    return render_template('index.html', box_number=int(times))

@app.route('/play/<times>/<color>')
def color(times, color):
    return render_template('index.html', box_number=int(times), box_color=color)

if __name__ == "__main__":
    app.run(debug=True)
