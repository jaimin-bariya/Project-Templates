
from flask import render_template, request, Blueprint

from app.database import db


from sqlalchemy.exc import SQLAlchemyError




home_bp = Blueprint("home_bp", __name__)


# @home_bp.context_processor
# def inject_request():
#     return dict(request=request)


@home_bp.get("/")
def Home():
    return render_template('Home.html')



@home_bp.get('/about')
def About():
    return render_template('about.html')


@home_bp.get('/query')
def Query():
    return render_template('query.html')


@home_bp.post("/submit")
def Submit_User():

    from app.models import Users

    
    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")
    password = request.form.get("password")
    city = request.form.get("city")
    state = request.form.get("state")
    zip_code = request.form.get("zip")

    
    try:
        # Create new instance 
        new_user = Users(f_name=f_name, l_name=l_name, password=password, city=city, state=state, zip=zip_code)


        # Add the user to the DB
        db.session.add(new_user)

        # Commit to the DB
        db.session.commit()

        print("User created")
        return "User created successfully"

    except SQLAlchemyError as e:

        db.session.rollback() # 🔥 Rollback in case of failure
        print(f"Database Error: {str(e)} ❌")

    finally:
        db.session.close() # 🔥 Always close the sessio



     

    return "None"
