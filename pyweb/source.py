from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def main():
    return render_template('signup.html')

@app.route('/signup/chat')
def tochat():
    return render_template('chat.html')

if __name__ == "__main__":
    app.run()
