# import crypt from methods
from flask import (Blueprint, render_template, redirect, request)

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print(request.form)
        return redirect('/facts')

@bp.route('/new')
def new():
    return render_template('facts/facts.html')