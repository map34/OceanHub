from flask import Blueprint

videos_blueprint = Blueprint('videos', __name__)

@videos_blueprint.route('/')
def index():
    # return a multipart response
    return 'Hello World'
