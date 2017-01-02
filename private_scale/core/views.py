from flask import Blueprint, render_template

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')


@blueprint.route('/new')
def new():
    return render_template('new.html')


@blueprint.route('/tracker/<guid>')
def tracker(guid):
    return render_template('tracker.html')
