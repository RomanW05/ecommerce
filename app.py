# Ecommerce store

import os
from flask import Flask

from routes.cache_file import cache
from routes.ecommerce import ecommerce


app = Flask(__name__)
cache.init_app(app)


# Add routes
app.register_blueprint(ecommerce)


# Initiate
if __name__ == "__main__":
    if 'ecommerce_localhost' in os.path.dirname(os.path.abspath(__file__)):
        app.run(host="localhost", port=8080, debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080, threaded=True)