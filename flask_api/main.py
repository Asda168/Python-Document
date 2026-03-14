from app import app
from controllers import auth_bp, product_bp

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)

if __name__ == '__main__':
    app.run(debug=True)