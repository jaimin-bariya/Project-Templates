

from flask import redirect, render_template, jsonify, request, Blueprint



user_bp = Blueprint("user_bp", __name__)



from app.models import Users


@user_bp.route("/user")
def AllUser():






    users = Users.query.all()

    users_list = [ user.to_dict() for user in  users]

    return jsonify(users_list)


@user_bp.get("/user/<string:f_name>")
def GetThisUser(f_name):
    

    user = Users.query.filter_by(f_name=f_name).first()

    return jsonify(user.to_dict())
