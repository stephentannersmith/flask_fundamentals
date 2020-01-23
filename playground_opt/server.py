from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<times>/<color>')
def index(times, color):
    return render_template('index.html', box_number=int(times), box_color=color)

if __name__ == "__main__":
    app.run(debug=True)
