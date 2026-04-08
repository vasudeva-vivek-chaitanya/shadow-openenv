TASKS = {
    "easy": {
        "description": "Fix syntax error",
        "initial_code": "def add(a,b)\n return a+b",
    },
    "medium": {
        "description": "Fix division by zero",
        "initial_code": "def div(a,b): return a/0",
        "test_input": (10, 2),
        "expected_output": 5
    },
    "hard": {
        "description": "Optimize inefficient loop",
        "initial_code": '''
def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total
''',
        "test_input": [1,2,3,4],
        "expected_output": 10
    }
}
