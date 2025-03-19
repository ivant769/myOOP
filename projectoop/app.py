from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Api
import error_handlers
from projectoop.resource.route.routes import human_routes_initialize


app = Flask(__name__)
api = Api(app)
app.json.sort_keys = False
app.config['PROPAGATE_EXCEPTIONS'] = True

url = '/swagger'
api_url = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    url,
    api_url,
    config={
        'app_name': "Swagger | OpenApi Service"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=url)
app.register_blueprint(error_handlers.blueprint)  # добавление исключений

human_routes_initialize(api)  # вызываются маршруты с типом Human


if __name__ == '__main__':
    app.run(debug=True)
