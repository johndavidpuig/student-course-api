from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

courses = [
    {
        "id": 1,
        "code": "CS 101",
        "name": "Introduction to Computing",
        "description": "Learn the fundamentals of computers."
    },
    {
        "id": 2,
        "code": "IT 102",
        "name": "Web Development",
        "description": "Learn how to build websites."
    },
    {
        "id": 3,
        "code": "CS 103",
        "name": "Database Management",
        "description": "Learn how databases store information."
    },
    {
        "id": 4,
        "code": "IT 104",
        "name": "Networking Fundamentals",
        "description": "Learn the basics of computer networks."
    },
    {
        "id": 5,
        "code": "CS 105",
        "name": "Programming Fundamentals",
        "description": "Learn basic programming concepts."
    },
    {
        "id": 6,
        "code": "IT 106",
        "name": "Systems Integration",
        "description": "Learn how different systems communicate."
    }
]

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Student Course API is running",
        "courses": len(courses)
    })

@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = next(
        (c for c in courses if c["id"] == course_id),
        None
    )

    if course is None:
        return jsonify({
            "error": "Course not found",
            "status": 404
        }), 404

    return jsonify(course)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
