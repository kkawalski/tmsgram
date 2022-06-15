from functools import wraps
from flask import Flask, request, render_template, make_response, redirect, url_for
from forms import LoginForm
from utils import access_token_request, users_list_request

app = Flask(__name__)
app.config["SECRET_KEY"] = "SUPERSECRETKEY"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.cookies.get("access"):
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        tokens = access_token_request(
            username=form.username.data,
            password=form.password.data,
        )
        response = make_response(redirect(url_for("users_list")))
        response.set_cookie("access", tokens["access"])
        return response
    return render_template("login.html", form=form)


@app.route("/users", methods=["GET"])
@login_required
def users_list():
    users = users_list_request(request.cookies.get("access"))
    return render_template("users_list.html", users=users)
