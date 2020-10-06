from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meetingroom')
def meetingroom():
    return render_template('meetingroom.html')

@app.route('/meetingroom_m1')
def meetingroom_m1():
    return render_template('meetingroom_m1.html')

@app.route('/meetingroom_sm1')
def meetingroom_sm1():
    return render_template('meetingroom_sm1.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/reservation2')
def reservation2():
    return render_template('reservation2.html')

@app.route('/sig_lounge')
def sig_lounge():
    return render_template('sig_lounge.html')

@app.route('/sig_storage')
def sig_storage():
    return render_template('sig_storage.html')

if __name__ == '__main__':
    app.run(debug=True)