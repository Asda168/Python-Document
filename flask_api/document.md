# Step created project.
    - Run: 
            * python -m venv venv
            * ./venv/Scripts/activate
            * pip install flask
    - Change env running this command:
            $env:FLASK_ENV="development"
            pip install waitress
            waitress-serve --host=127.0.0.1 --port=5000 app:app
            $env:PYTHONDONTWRITEBYTECODE
    
            