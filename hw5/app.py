from flask import Flask, render_template, request, redirect, send_from_directory
from query_processor import QueryProcessor
import os

app = Flask(__name__)

# Configure paths to your index files
INDEX_DIRECTORY = "./outfiles"
DOCUMENT_DIRECTORY = "./documents"

# Initialize QueryProcessor
qp = QueryProcessor(
    os.path.join(INDEX_DIRECTORY, "dict"),
    os.path.join(INDEX_DIRECTORY, "post"),
    os.path.join(INDEX_DIRECTORY, "map")
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("query")
    results = qp.process_query(query)
    return render_template("results.html", query=query, results=results)

@app.route("/document/<path:filename>")
def document(filename):
    return send_from_directory(DOCUMENT_DIRECTORY, filename)

if __name__ == "__main__":
    app.run(debug=True)
