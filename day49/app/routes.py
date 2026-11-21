from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from config import GYM_USERNAME, GYM_PASSWORD

main = Blueprint("main", __name__)


# Login route
@main.route("/", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if (
            username == GYM_USERNAME
            and password == GYM_PASSWORD
        ):

            session["logged_in"] = True
            session["username"] = username

            return redirect(url_for("main.classes"))

        else:

            error = "Invalid username or password!"

    return render_template(
        "login.html",
        error=error
    )


# Classes dashboard
@main.route("/classes")
def classes():

    if not session.get("logged_in"):
        return redirect(url_for("main.login"))

    return render_template(
        "classes.html",
        username=session.get("username")
    )


# Logout route
@main.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("main.login"))