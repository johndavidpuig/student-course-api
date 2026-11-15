# Student Course API

## Project Description

The Student Course API is a simple backend application developed for Laboratory Activity 3. It provides course information through REST API endpoints using JSON responses.

The API contains six fictional courses and allows users or applications to retrieve course information.

## Technologies Used

- Node.js
- Express.js
- CORS
- GitHub
- Render (Cloud Hosting)

## API Endpoints

The application provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Checks if the API is running. |
| GET | `/api/courses` | Retrieves all six courses. |
| GET | `/api/courses/1` | Retrieves a specific course using its ID. |
| GET | `/api/courses/9999` | Demonstrates the 404 response for a course that does not exist. |

## Installation and Setup

1. Install Node.js.
2. Clone this repository.
3. Open the project folder in a terminal.
4. Install the required dependencies:

```bash
npm install
```

5. Start the application:

```bash
npm start
```

The API will run on the configured port, or port 3000 when no environment port is provided.

## Testing the API

Open the following URLs in a browser:

- Health Check: https://student-course-api-j9ik.onrender.com/api/health
- All Courses: https://student-course-api-j9ik.onrender.com/api/courses
- Specific Course: https://student-course-api-j9ik.onrender.com/api/courses/1
- Invalid Course: https://student-course-api-j9ik.onrender.com/api/courses/9999

The API returns JSON responses. A successful request returns HTTP 200, while a course that does not exist returns HTTP 404.

## Deployment

The application is deployed using Render as a Web Service.

**Live API URL:**

https://student-course-api-j9ik.onrender.com

The application is connected to its GitHub repository for deployment.

## Project Limitations

This project uses fictional sample data stored directly in the application. It does not use a database, user authentication, or a frontend interface.

It is a basic API prototype intended for educational purposes.

## Developer

Created as part of Laboratory Activity 3: Backend Development, REST APIs, and Deployment.
