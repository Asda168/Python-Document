# main.py
import sys
import os

# Point to the PARENT of flask_api/, so "flask_api" becomes a importable package
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask_api.app import app
from flask_api.controllers import auth_bp
from flask_api.migrations import migrate

migrate()

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)  # ← also fixed the missing closing parenthesis