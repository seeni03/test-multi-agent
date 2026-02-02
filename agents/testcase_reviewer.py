def review(testcase):
    score = testcase["coverage"]
    status = "APPROVED" if score >= 80 else "NEEDS_REFINEMENT"
    return {"status": status, "score": score, "testcase": testcase}
