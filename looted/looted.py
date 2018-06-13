from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/redeem')
def login():
    message = 'Your payout has been queued.'
    username = request.form.get('xmradd')  # access the data inside 
    password = request.form.get('token')

    text_file = open("que.txt", "w")
    text_file.write(str(username)+","+str(password)+"\n")
    text_file.close()
	
    return render_template('redeem.html', message=message)

if __name__ == '__main__':
    app.run()
