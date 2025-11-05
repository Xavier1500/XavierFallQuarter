from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug=True)
    def GreenPage(name):
        return render_template("index.html", name = name)
    
    if __name__ == '__main__':
        app.run(debug=True)
                                        