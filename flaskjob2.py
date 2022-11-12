from flask import Flask, redirect, render_template, url_for, request

app = Flask("__name__")

@app.route("/name/")
def home(name):
    return render_template(index.html)

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = reques.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)