def generate_testcase(jira):
    return {
        "scenario": jira["summary"],
        "steps": [
            "Fetch Jira ID",
            "Retrieve Jira description",
            "Validate text content"
        ],
        "coverage": 75,
        "expected_text": jira["description"]
    }
