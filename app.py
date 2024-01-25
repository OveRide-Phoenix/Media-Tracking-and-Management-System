from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Simulated database connection (replace with your actual database connection details)
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="media"
)
db_cursor = db_connection.cursor()


def perform_search(query):
    # Modify this function to search for files in your MySQL database
    search_results = []

    # Example: Search for files with a specific file type extension using tags
    search_query = """
        SELECT m.filename, m.file_path, t.tag_name, t.edited
        FROM media m
        LEFT JOIN tags t ON m.tag_id = t.id
        WHERE
            m.filename LIKE %s OR
            t.tag_name LIKE %s OR
            t.edited = %s
    """

    # Provide the parameters as a tuple
    params = (f"%{query}%", f"%{query}%", query)

    # Execute the query with the parameters
    db_cursor.execute(search_query, params)
    rows = db_cursor.fetchall()

    for row in rows:
        search_results.append(row)

    return search_results


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    query = request.args.get('query', '')
    search_results = perform_search(query)
    return render_template('search_results.html', query=query, results=search_results)


if __name__ == '__main__':
    app.run(debug=True)
