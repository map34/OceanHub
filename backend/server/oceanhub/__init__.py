from __future__ import absolute_import

from flask import Flask
from oceanhub.videos.views import videos_blueprint

app = Flask(
    __name__,
    template_folder='templates',
    static_folder=None,
    static_url_path='/static_null'
)

app.register_blueprint(videos_blueprint, url_prefix='/videos')
