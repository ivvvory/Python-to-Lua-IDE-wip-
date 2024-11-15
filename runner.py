##working python Lua runner 

# runner.py

# runner.py

import os
import sys
from tokenizer import LuaLexer
from parser import LuaParser
from interpreter import LuaInterpreter

def load_lua_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return None
    with open(file_path, 'r') as file:
        return file.read()

def run_lua_code(code):
    lexer = LuaLexer()
    parser = LuaParser(lexer)
    interpreter = LuaInterpreter()
    
    ast = parser.parse(code)
    result = interpreter.evaluate(ast)
    return result

def main():
    print("Welcome to the Lua Interpreter!")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Run a Lua file")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            filename = input("Enter the name of the Lua file (e.g., example.lua): ")
            code = load_lua_file(filename)
            if code:
                result = run_lua_code(code)
                print(f"Result: {result}")
        elif choice == '2':
            print("Exiting Lua Interpreter.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()
