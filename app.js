const express = require("express");
const app = express();

const courses = [
  {
    id: 1,
    code: "CS 101",
    name: "Introduction to Computing",
    description: "Learn the fundamentals of computers."
  },
  {
    id: 2,
    code: "IT 102",
    name: "Web Development",
    description: "Learn how to build websites."
  },
  {
    id: 3,
    code: "CS 103",
    name: "Database Management",
    description: "Learn how databases store information."
  },
  {
    id: 4,
    code: "IT 104",
    name: "Networking Fundamentals",
    description: "Learn the basics of computer networks."
  },
  {
    id: 5,
    code: "CS 105",
    name: "Programming Fundamentals",
    description: "Learn basic programming concepts."
  },
  {
    id: 6,
    code: "IT 106",
    name: "Systems Integration",
    description: "Learn how different systems communicate."
  }
];

app.get("/api/health", (req, res) => {
  res.json({
    status: "ok",
    message: "Student Course API is running",
    courses: courses.length
  });
});

app.get("/api/courses", (req, res) => {
  res.json(courses);
});

app.get("/api/courses/:id", (req, res) => {
  const course = courses.find(
    c => c.id === Number(req.params.id)
  );

  if (!course) {
    return res.status(404).json({
      error: "Course not found",
      status: 404
    });
  }

  res.json(course);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Student Course API running on port ${PORT}`);
});
