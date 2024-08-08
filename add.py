from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def time():
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('time.html', date_time=date_time)

if __name__ == '__main__':
    app.run(debug=True)