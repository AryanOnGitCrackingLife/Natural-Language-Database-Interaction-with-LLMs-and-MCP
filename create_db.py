import sqlite3

# Create local database file in same folder
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Drop tables if re-running (optional for clean setup)
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")
cursor.execute("DROP TABLE IF EXISTS projects")

# Create Departments Table
cursor.execute("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL,
    location TEXT
)
""")

# Create Employees Table
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

# Create Projects Table
cursor.execute("""
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    department TEXT,
    budget INTEGER
)
""")

# Insert Departments Data
departments_data = [
    ("IT", "Mumbai"),
    ("HR", "Delhi"),
    ("Finance", "Bangalore"),
    ("Marketing", "Hyderabad"),
    ("R&D", "Pune")
]
cursor.executemany(
    "INSERT INTO departments (dept_name, location) VALUES (?, ?)",
    departments_data
)

# Insert Employees Data (More Realistic)
employees_data = [
    ("Rahul Sharma", 28, "IT", 60000, 3),
    ("Anita Verma", 32, "HR", 50000, 6),
    ("Aman Gupta", 30, "Finance", 70000, 5),
    ("Neha Singh", 26, "IT", 55000, 2),
    ("Rohit Mehta", 35, "Marketing", 65000, 8),
    ("Priya Nair", 29, "R&D", 72000, 4),
    ("Karan Patel", 31, "IT", 68000, 6),
    ("Sneha Kapoor", 27, "HR", 48000, 3),
    ("Arjun Reddy", 33, "Finance", 75000, 7),
    ("Pooja Das", 25, "Marketing", 45000, 2),
    ("Vikram Joshi", 38, "R&D", 90000, 10),
    ("Simran Kaur", 29, "IT", 62000, 4)
]
cursor.executemany(
    "INSERT INTO employees (name, age, department, salary, experience) VALUES (?, ?, ?, ?, ?)",
    employees_data
)

# Insert Projects Data
projects_data = [
    ("AI Resume Analyzer", "IT", 200000),
    ("Employee Management System", "HR", 120000),
    ("Financial Forecasting", "Finance", 300000),
    ("Digital Marketing Campaign", "Marketing", 150000),
    ("Cloud Automation Tool", "R&D", 400000),
    ("NL2SQL System", "IT", 180000)
]
cursor.executemany(
    "INSERT INTO projects (project_name, department, budget) VALUES (?, ?, ?)",
    projects_data
)

conn.commit()
conn.close()

print("Expanded local database created successfully: database.db")