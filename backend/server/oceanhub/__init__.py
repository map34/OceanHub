from __future__ import absolute_import

from flask import Flask

from oceanhub.core.blueprints import initialize_blueprints

app = Flask(
    __name__,
    template_folder='templates',
    static_folder=None,
    static_url_path='/static_null'
)

initialize_blueprints(app)
