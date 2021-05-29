from flask import render_template, Blueprint


page_bp = Blueprint('page', __name__, url_prefix='/page')


@page_bp.route('/login')
def login():
    return render_template('login/login.html')

