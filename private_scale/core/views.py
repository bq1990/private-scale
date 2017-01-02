from flask import Blueprint, render_template

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')
