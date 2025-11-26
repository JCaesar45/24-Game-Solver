import itertools

def solve24(digits_str):
    digits = list(digits_str)
    target = 24
    
    # All possible operators
    operators = ['+', '-', '*', '/']
    
    # Helper function to evaluate an expression safely
    def safe_eval(expr):
        try:
            return abs(eval(expr) - target) < 1e-6
        except ZeroDivisionError:
            return False
    
    # Generate all permutations of the digits
    for perm in itertools.permutations(digits):
        # Generate all possible operator combinations (3 operators needed for 4 numbers)
        for ops in itertools.product(operators, repeat=3):
            a, b, c, d = perm
            op1, op2, op3 = ops
            
            # Generate all parenthesized expressions
            expressions = []
            # (a op1 b) op2 (c op3 d)
            expressions.append(f"(({a}{op1}{b}){op2}({c}{op3}{d}))")
            # (a op1 (b op2 c)) op3 d
            expressions.append(f"({a}{op1}({b}{op2}{c})){op3}{d}")
            # a op1 ((b op2 c) op3 d)
            expressions.append(f"{a}{op1}(({b}{op2}{c}){op3}{d})")
            # a op1 (b op2 (c op3 d))
            expressions.append(f"{a}{op1}({b}{op2}({c}{op3}{d}))")
            # (a op1 b) op2 c op3 d (left to right)
            expressions.append(f"(({a}{op1}{b}){op2}{c}){op3}{d}")
            
            for expr in expressions:
                if safe_eval(expr):
                    return expr
    return "no solution exists"
