from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/')  # Home directory
def hello():
    return("<h1> Hello World! This is Amjad Ali.<h1>")

# to run, use run()
if __name__ == '__main__':
    app.run(debug = True)