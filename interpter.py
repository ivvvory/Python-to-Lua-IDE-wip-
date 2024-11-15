##working Lua interpter in python

class LuaInterpreter:
    def __init__(self):
        self.env = {}

    def evaluate(self, ast):
        if isinstance(ast, list):
            result = None
            for stmt in ast:
                result = self.evaluate_statement(stmt)
            return result
        else:
            return self.evaluate_statement(ast)

    def evaluate_statement(self, stmt):
        if stmt[0] == 'local':
            return self.local_statement(stmt)
        elif stmt[0] == 'assign':
            return self.assignment_statement(stmt)
        elif stmt[0] == 'return':
            return self.return_statement(stmt)
        elif stmt[0] == 'expr':
            return self.evaluate_expression(stmt[1])

    def local_statement(self, stmt):
        var_name = stmt[1]
        value = self.evaluate_expression(stmt[2])
        self.env[var_name] = value
        return value

    def assignment_statement(self, stmt):
        var_name = stmt[1]
        value = self.evaluate_expression(stmt[2])
        self.env[var_name] = value
        return value

    def return_statement(self, stmt):
        return self.evaluate_expression(stmt[1])

    def evaluate_expression(self, expr):
        if expr[0] == 'literal':
            return expr[1]
        elif expr[0] == 'var':
            return self.env.get(expr[1], None)
        elif expr[0] == 'binary':
            left = self.evaluate_expression(expr[1])
            right = self.evaluate_expression(expr[3])
            return self.apply_operator(expr[2], left, right)

    def apply_operator(self, operator, left, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        else:
            raise SyntaxError(f"Unknown operator {operator}")
