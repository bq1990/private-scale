from weigh_in import app
from weigh_in.settings import prod


application = app.create_app(prod)