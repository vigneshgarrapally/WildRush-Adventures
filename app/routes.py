"""
This module contains the routes for the Flask application.
"""
from flask import render_template, request, redirect, url_for
from app import app, bcrypt
from app.models import User, db, Lead
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import SQLAlchemyError


@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
        str: The rendered HTML template.
    """
    return render_template("index.html", active_page="index")


@app.errorhandler(401)
def unauthorized(error):
    print(error)
    return render_template("login.html", unauthorized=True, next_url=request.url)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Renders the login page and handles the login form submission.

    Returns:
        str: The rendered HTML template.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(email=username).first()
        if user:
            print(user.password_hash)
            if bcrypt.check_password_hash(user.password_hash, password):
                login_user(user)
                next_page = request.form["next"]
                if not next_page:
                    next_page = url_for("index")
                print(next_page)
                return redirect(next_page)
        return render_template("login.html", error=True)

    return render_template("login.html", error=False)


@app.route("/signUp", methods=["GET", "POST"])
def sign_up():
    """
    Renders the sign up page and handles the sign up form submission.

    Returns:
        str: The rendered HTML template.
    """
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check if the passwords match and have a minimum length (you can add more criteria here)
        if password == confirm_password:
            # Check if the email is not already registered in the database
            if not User.query.filter_by(email=email).first():
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password_hash=bcrypt.generate_password_hash(password).decode("utf-8"),
                )
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("login"))
            return render_template("signUp.html", error="Email already registered.")
        return render_template("signUp.html", error="Passwords do not match.")
    return render_template("signUp.html")


@app.route("/adventures")
def adventures():
    return render_template("adventures.html", active_page="adventures")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html", active_page="reviews")


@app.route("/requestquote")
@login_required
def requestquote():
    return render_template("quote.html", active_page="requestquote")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        consent = request.form["checkbox"] == "on"
        # create a record in the database
        new_lead = Lead(name=name, email=email, message=message, consent=consent)
        db.session.add(new_lead)
        db.session.commit()
        return render_template("contact.html", success=True)
    return render_template("contact.html", active_page="contact")


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """
    Renders the profile page and handles the profile form submission.

    Returns:
        str: The rendered HTML template.
    """
    if request.method == "POST":
        # check if the details are changed
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        if (
            first_name == current_user.first_name
            and last_name == current_user.last_name
            and email == current_user.email
        ):
            return render_template("profile.html", active_page="profile")
        else:
            try:
                user = User.query.filter_by(email=current_user.email).first()
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                db.session.commit()
                return render_template("profile.html", success=True)
            except SQLAlchemyError as exception:
                print(exception)
                db.session.rollback()
                return render_template("profile.html", error=True)
    return render_template("profile.html", active_page="profile")


# add logout route
@app.route("/logout")
@login_required
def logout():
    """
    Returns:
        _type_: _description_
    """
    logout_user()
    return redirect(url_for("index"))


@app.route("/delete_account")
@login_required
def delete_account():
    """
    Deletes the user's account from the database.
    """
    user = User.query.get(current_user.email)
    logout_user()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/<activity_type>")
def activity(activity_type):
    valid_activity_types = ["hiking", "white_water", "skydiving", "mountaineering", "rock_climbing", "zip_lining"]

    if activity_type in valid_activity_types:
        return render_template(f"{activity_type}.html")
    else:
        return render_template("404.html")
