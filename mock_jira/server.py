from flask import Flask, jsonify

app = Flask(__name__)

MOCK_DB = {
    "PROJ-101": {
        "summary": "Fetch Jira description by ID",
        "description": "System should retrieve Jira issue description and validate text."
    }
}

@app.route("/jira/<jira_id>")
def jira(jira_id):
    if jira_id not in MOCK_DB:
        return jsonify({"error": "Not Found"}), 404
    
    return jsonify(MOCK_DB[jira_id])

if __name__ == "__main__":
    app.run(port=8080)
