from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/job')
def job():
    return render_template('job.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/future')
def future():
    return render_template('future.html')
if __name__ == "__main__":
    app.run(debug=True)