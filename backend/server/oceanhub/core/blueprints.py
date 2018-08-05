from oceanhub.videos.views import videos_blueprint


def initialize_blueprints(app):
    app.register_blueprint(videos_blueprint, url_prefix='/videos')
