from flask import Blueprint, render_template

from .forms import TrackerForm

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')


@blueprint.route('/new')
def new():
    form = TrackerForm()
    return render_template('new.html', form=form)


@blueprint.route('/tracker/<guid>')
def tracker(guid):
    return render_template('tracker.html')
