import uuid

from flask import abort, Blueprint, render_template, redirect, request, url_for

from ..database import db
from .forms import EntryForm, LogForm
from .models import Entry, Log

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return render_template('home.html')


@blueprint.route('/new', methods=['GET', 'POST'])
def new_log():
    form = LogForm(obj=request.form)
    if form.validate_on_submit():
        log = Log()
        log.guid = str(uuid.uuid1())
        form.populate_obj(log)
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('core.log_detail', guid=log.guid))
    return render_template('new_log.html', form=form)


@blueprint.route('/log/<guid>')
def log_detail(guid):
    log = Log.query.filter_by(guid=guid).first()
    if not log:
        abort(404)
    return render_template('log_detail.html', log=log)


@blueprint.route('/log/<guid>/new', methods=['GET', 'POST'])
def new_entry(guid):
    log = Log.query.filter_by(guid=guid).first()
    if not log:
        abort(404)
    form = EntryForm(
        obj=request.form,
        measured_on=log.next_date(),
        pounds=log.last_weight())
    if form.validate_on_submit():
        entry = Entry(log=log)
        form.populate_obj(entry)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('core.log_detail', guid=log.guid))
    return render_template('entry_form.html', form=form, log=log)


