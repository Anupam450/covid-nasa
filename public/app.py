from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/icon.ico')
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/developer")
def dev():
    return render_template("developer.html")

@app.route("/live")
def live():
    return render_template("live.html")

@app.route('/stats')
def stats():
    return render_template("statistics.html")


@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html") 