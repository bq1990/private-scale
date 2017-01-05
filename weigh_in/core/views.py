from dateutil.parser import parse
import uuid

from flask import abort, Blueprint, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError

from ..database import db
from .forms import EntryForm, LogForm
from .models import Entry, Log

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    form = LogForm(obj=request.form)
    return render_template('home.html', form=form)


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
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            form.measured_on.errors.append(
                'An entry already exists for that date'
            )
        else:
            return redirect(url_for('core.log_detail', guid=log.guid))
    return render_template('new_entry.html', form=form, log=log)


@blueprint.route('/log/<guid>/<entry_date>/delete', methods=['GET', 'POST'])
def delete_entry(guid, entry_date):
    log = Log.query.filter_by(guid=guid).first()
    if not log:
        abort(404)
    entry_date = parse(entry_date).date()
    entry = next((e for e in log.entries if e.measured_on == entry_date), None)
    if not entry:
        abort(404)
    form = FlaskForm(obj=request.form)
    if form.validate_on_submit():
        db.session.delete(entry)
        db.session.commit()
        return redirect(url_for('core.log_detail', guid=log.guid))
    return render_template('delete_entry.html', form=form, entry=entry)

