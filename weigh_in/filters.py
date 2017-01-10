import flask
import jinja2

blueprint = flask.Blueprint('filters', __name__)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@jinja2.contextfilter
@blueprint.app_template_filter()
def format_round2(context, value):
    if value is None:
        return '0.00'
    elif not is_number(value):
        return value
    return '{0:.2f}'.format(value)
