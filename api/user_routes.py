from flask import Blueprint, jsonify, request
from .courses_data import user,plan

user_api = Blueprint('user_api', __name__)

@user_api.route('/getUser', methods=['GET'])
def get_users():
    return jsonify(user)

@user_api.route('/<int:userId>/getPlan', methods=['GET'])
def get_plan(userId):
    return jsonify(plan)


@user_api.route('/addplan', methods=['POST'])
def add_plans():
    try:
        # Assuming the frontend sends JSON data with semester and courses
        data = request.get_json()

        # Extract semester and courses from the JSON data
        semester = data.get('semester')
        courses = data.get('courses')

        # Process the data as needed (e.g., save it to a database)
        # Replace this with your actual logic
        # For demonstration purposes, we'll just echo the data back as a response
        response_data = {
            'planId':1,
            'semester': semester,
            'courses': courses,
            'message': 'Plans added successfully',
        }

        return jsonify(response_data), 200

    except Exception as e:
        # Handle any exceptions that may occur during processing
        error_message = str(e)
        return jsonify({'error': error_message}), 500