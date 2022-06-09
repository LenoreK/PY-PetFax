# import crypt from methods
from flask import (Blueprint, render_template, redirect, request)

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/')
def new():
    return render_template('facts.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print(request.form)
        return redirect('/facts')