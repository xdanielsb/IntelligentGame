from flask import Flask, render_template,request, flash,  url_for, redirect, session

app=Flask(__name__)
app.secret_key = '15%&*^&^GJHYTDT24623/*@!@#G@JH$%+9'

if __name__ == "__main__":
    app.run(debug= True)

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return "Error in the method index"


@app.route("/onePlayer/")
def onePlayer():
    try:
        return render_template("index.html")
    except Exception as e:
        return "Error in the method one Player"


@app.route("/twoPlayers/")
def twoPlayers():
    try:
        return render_template("index.html")
    except Exception as e:
        return "Error in the method two G"

