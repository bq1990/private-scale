import uuid

from flask import abort, Blueprint, render_template, redirect, request, url_for

from ..database import db
from .forms import MeasurementForm, TrackerForm
from .models import Measurement, Tracker

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')


@blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = TrackerForm(obj=request.form)
    if form.validate_on_submit():
        tracker = Tracker()
        tracker.guid = str(uuid.uuid1())
        form.populate_obj(tracker)
        db.session.add(tracker)
        db.session.commit()
        return redirect(url_for('core.tracker', guid=tracker.guid))
    return render_template('new.html', form=form)


@blueprint.route('/tracker/<guid>')
def tracker(guid):
    tracker = Tracker.query.filter_by(guid=guid).first()
    if not tracker:
        abort(404)
    return render_template('tracker.html', tracker=tracker)


@blueprint.route('/tracker/<guid>/new', methods=['GET', 'POST'])
def new_measurement(guid):
    tracker = Tracker.query.filter_by(guid=guid).first()
    if not tracker:
        abort(404)
    form = MeasurementForm(
        obj=request.form,
        measured_on=tracker.next_date(),
        pounds=tracker.last_weight())
    if form.validate_on_submit():
        measurement = Measurement(tracker=tracker)
        form.populate_obj(measurement)
        db.session.add(measurement)
        db.session.commit()
        return redirect(url_for('core.tracker', guid=tracker.guid))
    return render_template('measurement_form.html', form=form, tracker=tracker)


