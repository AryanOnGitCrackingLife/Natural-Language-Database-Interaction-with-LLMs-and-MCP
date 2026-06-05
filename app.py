from flask import Flask, render_template, request, jsonify
import sqlite3
import ollama  # since you said you have Ollama locally

app = Flask(__name__)

# Function to connect to local database file
def get_db_connection():
    conn = sqlite3.connect("database.db")  # local file in same folder
    conn.row_factory = sqlite3.Row
    return conn

# Convert Natural Language → SQL using local LLM
def generate_sql(user_query):
    prompt = f"""
    Convert the natural language query into SQLite SQL.
    Table: employees(id, name, department, salary)

    User Query: {user_query}

    Only return the SQL query.
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    user_query = request.form["query"]

    # Generate SQL from LLM
    sql_query = generate_sql(user_query)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()

        # Convert rows to list
        data = [dict(row) for row in results]

        return jsonify({
            "generated_sql": sql_query,
            "results": data
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "generated_sql": sql_query
        })

if __name__ == "__main__":
    app.run(debug=True)