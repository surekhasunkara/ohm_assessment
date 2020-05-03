from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    # switch to User.recent() to use ORM
    args = {
            'message': "Recently Created Users",
            'users': User.recent_sql(),

    }
    return render_template("community.html", **args)
