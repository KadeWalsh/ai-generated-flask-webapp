from flask import Blueprint, render_template, request

my_blueprint = Blueprint("my_blueprint", __name__)


@my_blueprint.route("/")
def index():
    return render_template("index.html")


@my_blueprint.route("/about")
def about():
    return render_template("about.html")


@my_blueprint.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Send email to admin
        # ...

        return render_template("contact.html",
                               message="Your message has been sent.")
    else:
        return render_template("contact.html")
