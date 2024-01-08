from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from api.router import api_blueprint 
from api.user_routes import user_api
from api.course_routes import course_api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plannerx.db'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    CORS(app)
    
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(user_api, url_prefix='/api/users')
    app.register_blueprint(course_api, url_prefix='/api/courses')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)

# @app.route('/api/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.username for user in users])

# @app.route('/api/users', methods=['POST'])
# def add_user():
#     username = request.json.get('username')
#     new_user = User(username=username)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User added!", "username": username}), 201


# @app.route('/api/get-data/<semester>', methods=['GET'])
# def api_get_data(semester):
#     baseURL = "https://www.university.edu/courses"
#     data = getData(baseURL, semester)
#     return jsonify(data)
# if __name__ == '__main__':
#     app.run(debug=True)
