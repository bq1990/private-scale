from flask import Blueprint, render_template, redirect, request, url_for

from .forms import TrackerForm

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')


@blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = TrackerForm(obj=request.form)
    if form.validate_on_submit():
        return redirect(url_for('core.tracker', guid='123'))
    return render_template('new.html', form=form)


@blueprint.route('/tracker/<guid>')
def tracker(guid):
    return render_template('tracker.html')
