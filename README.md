# Lua Interpreter Project

This project provides a basic Lua interpreter written in Python. The interpreter supports running Lua scripts, as well as interactive coding through a terminal interface. The system consists of multiple Python files that handle different aspects of the Lua interpreter, including tokenization, parsing, and evaluation.

Additionally, an interactive terminal mode allows users to run Lua code dynamically in a terminal window.

## Table of Contents
1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Dependencies](#dependencies)
4. [Files Overview](#files-overview)
5. [How to Use](#how-to-use)
   - [Running Lua Files](#running-lua-files)
   - [Interactive Mode](#interactive-mode)
   - [Opening the Interactive Terminal](#opening-the-interactive-terminal)
6. [Credits](#credits)

## Overview
This project simulates a Lua interpreter by parsing and evaluating Lua code using Python. It includes the following features:
- **Run Lua scripts**: Allows users to run `.lua` files and get evaluated results.
- **Interactive mode**: Lets users type Lua code directly into the terminal and immediately execute it.
- **Interactive Terminal Window**: Opens a new terminal window where users can code interactively in Lua.

The project is composed of several Python files:
1. **`tokenizer.py`**: Responsible for breaking Lua code into tokens.
2. **`parser.py`**: Converts tokens into an Abstract Syntax Tree (AST).
3. **`interpreter.py`**: Evaluates the AST and runs the Lua code.
4. **`runner.py`**: The main entry point, used for running files or starting the interactive mode.
5. **`interactive_terminal.py`**: Opens a new terminal window to allow users to code in an interactive Lua prompt.

## File Structure

lua_interpreter_project 
│ 

   ├── runner.py # Main entry point for running scripts and interactive mode. 

   ├── tokenizer.py # Tokenizer for breaking Lua code into tokens. 

   ├── parser.py # Parses tokens into an Abstract Syntax Tree (AST). 

   ├── interpreter.py # Interpreter that evaluates the AST. 

   ├── interactive_terminal.py # Opens a new terminal window for interactive coding. 


## Dependencies
This project relies on Python 3.x. No additional libraries are required, as all functionality is implemented using built-in Python modules such as `re`, `subprocess`, and `os`.

### Running the Interpreter

Make sure you have Python 3.10 installed on your machine.

## Files Overview

### 1. **`tokenizer.py`**: Tokenizer
The `LuaLexer` class in `tokenizer.py` is responsible for converting Lua source code into tokens that the parser can work with. Tokens include keywords, numbers, operators, and variables.

```
import re

class LuaLexer:
    def __init__(self):
        self.token_specification = [
            ('NUMBER',    r'\b\d+(\.\d*)?\b'),     # Integer or decimal number
            ('STRING',    r'"([^"\\]|\\.)*"'),      # Double-quoted string
            ('ID',        r'[A-Za-z_][A-Za-z0-9_]*'),  # Identifier (variable or function name)
            ('KEYWORD',   r'\b(if|then|else|end|while|for|do|return|function|local)\b'),
            ('OPERATOR',  r'[\+\-\*/=<>!]'),        # Operators
            ('ASSIGN',     r'='),                    # Assignment
            ('LPAREN',    r'\('),                    # Left Parenthesis
            ('RPAREN',    r'\)'),                    # Right Parenthesis
            ('LBRACE',    r'\{'),                    # Left brace
            ('RBRACE',    r'\}'),                    # Right brace
            ('COMMA',     r','),                     # Comma
            ('SEMI',      r';'),                     # Semicolon
            ('WHITESPACE', r'\s+'),                  # Skip over whitespace
            ('MISMATCH',  r'.'),                     # Any other character
        ]
        self.regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)
        self.re = re.compile(self.regex)

    def tokenize(self, code):
        for match in self.re.finditer(code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'WHITESPACE':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character: {value}')
            yield kind, value
2. parser.py: Parser
The LuaParser class converts tokens into an Abstract Syntax Tree (AST). It handles parsing statements, expressions, and other parts of Lua code.

class LuaParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = []
        self.pos = 0

    def parse(self, code):
        self.tokens = list(self.lexer.tokenize(code))
        self.pos = 0
        return self.program()
    
    # Parse the program, statement, expressions, and more...
3. interpreter.py: Interpreter
The LuaInterpreter class evaluates the AST. It handles variable assignments, mathematical operations, and the Lua return statement.

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

    # Evaluate statements and expressions...
4. runner.py: Main Program
runner.py is the entry point of the Lua interpreter. It allows you to either:

##Run a Lua file.
##Enter an interactive mode where you can type and run Lua code directly in the console.

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
        print("2. Start Interactive Lua Interpreter")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            filename = input("Enter the name of the Lua file (e.g., example.lua): ")
            code = load_lua_file(filename)
            if code:
                result = run_lua_code(code)
                print(f"Result: {result}")
        elif choice == '2':
            interactive_mode()
        elif choice == '3':
            print("Exiting Lua Interpreter.")
            sys.exit(0)
5. interactive_terminal.py: Interactive Terminal
##The interactive_terminal.py script opens a new terminal window where the user can input Lua code interactively.

import subprocess
import sys

def open_terminal():
    if sys.platform == 'win32':
        subprocess.run(['start', 'cmd', '/K', 'python', 'runner.py'], shell=True)
    elif sys.platform == 'darwin' or sys.platform.startswith('linux'):
        subprocess.run(['gnome-terminal', '--', 'python3', 'runner.py'])

Choose the option to run a Lua file (Option 1).
Enter the name of the Lua file (e.g., example.lua).
The script will be parsed and evaluated, and the result will be displayed in the terminal.
2. Interactive Mode
You can run Lua code interactively by choosing Option 2 in the menu after running runner.py. This will start a prompt where you can type Lua code, and the interpreter will execute it immediately:

bash
Copy code
lua> local a = 10
lua> local b = 20
lua> a + b
Result: 30
Type exit to quit the interactive mode.

3. Opening the Interactive Terminal
If you prefer to code in a new terminal window, you can use interactive_terminal.py:

Run python interactive_terminal.py from the command line.
This will open a new terminal window where you can type and execute Lua code interactively.
Example Lua File
Here is an example Lua script (example.lua) that you can use to test the interpreter:


local a = 10
local b = 20
return a + b
How to Test
Create a Lua file (e.g., example.lua).
Run python runner.py and choose Option 1 to load and run the Lua file.
To test interactive mode, run python runner.py and choose Option 2 to start coding interactively.
Credits
This Lua interpreter project was created by ivvvory.
