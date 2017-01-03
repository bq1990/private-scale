import uuid

from flask import Blueprint, render_template, redirect, request, url_for

from ..database import db
from .forms import TrackerForm
from .models import Tracker

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')


@blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = TrackerForm(obj=request.form)
    if form.validate_on_submit():
        tracker = Tracker()
        tracker.guid = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'anon weight'))
        form.populate_obj(tracker)
        db.session.add(tracker)
        db.session.commit()
        return redirect(url_for('core.tracker', guid=tracker.guid))
    return render_template('new.html', form=form)


@blueprint.route('/tracker/<guid>')
def tracker(guid):
    return render_template('tracker.html')
