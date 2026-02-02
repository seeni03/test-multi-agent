def generate_script(testcase):
    code = f'''
from mcp_python.playwright_mcp import run_playwright_test

def test_generated():
    url = "https://example.com"
    expected = "{testcase['expected_text']}"
    assert run_playwright_test(url, expected)
'''
    path = "generated_tests/test_generated.py"
    with open(path, "w") as f:
        f.write(code)
    return path
