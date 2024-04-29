from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camisetas')
def camisetas():
    return render_template('camisetas.html')

@app.route('/titulos')
def títulos():
    return render_template('titulos.html')  












if __name__ == "__main__":
    app.run(debug=True)