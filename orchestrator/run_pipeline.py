import requests

from agents.testcase_generator import generate_testcase
from agents.testcase_reviewer import review
from agents.testcase_refiner import refine
from agents.script_generator import generate_script
from agents.executor import run_test

JIRA_URL = "http://localhost:8080/jira/"

def fetch_jira(jira_id):
    res = requests.get(JIRA_URL + jira_id)
    return res.json()

def run_pipeline(jira_id):
    print("Fetching Jira...")
    jira = fetch_jira(jira_id)

    print("Generating testcase...")
    testcase = generate_testcase(jira)

    print("Reviewing testcase...")
    review_result = review(testcase)

    if review_result["status"] != "APPROVED":
        print("Refining testcase...")
        testcase = refine(testcase)

    print("Generating Playwright script...")
    script_path = generate_script(testcase)

    print("Executing test...")
    passed = run_test(script_path)

    if passed:
        print("TEST PASSED")
    else:
        print("TEST FAILED")

if __name__ == "__main__":
    run_pipeline("PROJ-101")
