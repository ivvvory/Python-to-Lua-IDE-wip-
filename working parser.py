##lua parser wrote in python 

class LuaParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = []
        self.pos = 0
    
    def parse(self, code):
        self.tokens = list(self.lexer.tokenize(code))
        self.pos = 0
        return self.program()

    def program(self):
        statements = []
        while self.pos < len(self.tokens):
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return statements

    def statement(self):
        if self.match('KEYWORD', 'local'):
            return self.local_statement()
        elif self.match('ID'):
            return self.assignment()
        elif self.match('KEYWORD', 'return'):
            return self.return_statement()
        else:
            return self.expression_statement()

    def local_statement(self):
        self.consume('KEYWORD', 'local')
        var_name = self.consume('ID')[1]
        self.consume('ASSIGN')
        expr = self.expression()
        return ('local', var_name, expr)

    def assignment(self):
        var_name = self.consume('ID')[1]
        self.consume('ASSIGN')
        expr = self.expression()
        return ('assign', var_name, expr)

    def return_statement(self):
        self.consume('KEYWORD', 'return')
        expr = self.expression()
        return ('return', expr)

    def expression_statement(self):
        expr = self.expression()
        return ('expr', expr)

    def expression(self):
        left = self.term()
        while self.match('OPERATOR', '+', '-'):
            op = self.previous()[1]
            right = self.term()
            left = ('binary', left, op, right)
        return left

    def term(self):
        left = self.factor()
        while self.match('OPERATOR', '*', '/'):
            op = self.previous()[1]
            right = self.factor()
            left = ('binary', left, op, right)
        return left

    def factor(self):
        if self.match('NUMBER'):
            return ('literal', float(self.previous()[1]))
        elif self.match('STRING'):
            return ('literal', self.previous()[1][1:-1])  # Strip quotes
        elif self.match('ID'):
            return ('var', self.previous()[1])
        elif self.match('LPAREN'):
            expr = self.expression()
            self.consume('RPAREN')
            return expr
        else:
            raise SyntaxError("Unexpected token: " + self.current()[1])

    def match(self, *types):
        if self.pos < len(self.tokens) and self.current()[0] in types:
            self.pos += 1
            return True
        return False

    def consume(self, *types):
        if self.match(*types):
            return self.previous()
        raise SyntaxError(f"Expected {'|'.join(types)} but found {self.current()[0]}")

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def previous(self):
        return self.tokens[self.pos - 1] if self.pos > 0 else (None, None)
