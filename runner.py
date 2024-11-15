##working python Lua runner 

def run_lua_code(code):
    lexer = LuaLexer()
    parser = LuaParser(lexer)
    interpreter = LuaInterpreter()
    
    ast = parser.parse(code)
    result = interpreter.evaluate(ast)
    return result

# Test the Lua-like interpreter
lua_code = """
local x = 10
local y = 20
x + y
"""

result = run_lua_code(lua_code)
print(f"Result: {result}")
