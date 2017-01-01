from flask import Blueprint

blueprint = Blueprint('core', __name__, static_folder="../static")


@blueprint.route('/')
def home():
    return 'Home'