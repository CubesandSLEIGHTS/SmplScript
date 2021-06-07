from SmplScript.Lexer.lexer import Lexer
from SmplScript.Symbol_Table.symbol_table import SymbolTable
from SmplScript.Values.values import Number
from SmplScript.Interpreter.interpreter import Interpreter
from SmplScript.Context.context import Context
from SmplScript.Parser.Parser import Parser
from SmplScript.Values.values import BuiltInFunction

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("False", Number.false)
global_symbol_table.set("True", Number.true)
global_symbol_table.set("pi", Number.math_PI)
global_symbol_table.set("print", BuiltInFunction.print)
#global_symbol_table.set('colored_print', BuiltInFunction.cprint)
global_symbol_table.set("print_ret", BuiltInFunction.print_ret)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("int_input", BuiltInFunction.input_int)
global_symbol_table.set("cleat", BuiltInFunction.clear)
global_symbol_table.set("cls", BuiltInFunction.clear)
global_symbol_table.set("is_num", BuiltInFunction.is_number)
global_symbol_table.set("is_str", BuiltInFunction.is_string)
global_symbol_table.set("is_list", BuiltInFunction.is_list)
global_symbol_table.set("is_function", BuiltInFunction.is_function)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("length", BuiltInFunction.len)
global_symbol_table.set("run", BuiltInFunction.run)

def run(fn, text):
  # Generate tokens
  lexer = Lexer(fn, text)
  tokens, error = lexer.make_tokens()
  if error: return None, error
  
  # Generate AST
  parser = Parser(tokens)
  ast = parser.parse()
  if ast.error: return None, ast.error

  # Run program
  interpreter = Interpreter()
  context = Context('<program>')
  context.symbol_table = global_symbol_table
  result = interpreter.visit(ast.node, context)

  return result.value, result.error