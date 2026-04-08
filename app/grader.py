import ast

def safe_exec(code, func_name, test_input):
    try:
        local_env = {}
        exec(code, {}, local_env)
        func = local_env.get(func_name)
        if func is None:
            return None
        if isinstance(test_input, tuple):
            return func(*test_input)
        return func(test_input)
    except:
        return None

def extract_function_name(code):
    try:
        tree = ast.parse(code)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                return node.name
    except:
        return None

def compute_complexity(code):
    try:
        tree = ast.parse(code)
        return sum(1 for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While, ast.If)))
    except:
        return 999

def grade(task_id, code, task):
    score = 0.0
    try:
        ast.parse(code)
        score += 0.2
    except:
        return 0.0

    if "test_input" in task:
        fname = extract_function_name(code)
        out = safe_exec(code, fname, task["test_input"])
        if out == task["expected_output"]:
            score += 0.5

    if task_id == "hard" and compute_complexity(code) <= 1:
        score += 0.3

    return min(score, 1.0)
