from app import create_app
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os


app = create_app()
CORS(app)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure, random key
jwt = JWTManager(app)


if __name__ == '__main__':
    port = int(os.environ.get("PORT",4000))
    app.run(host="0.0.0.0", port=port)

