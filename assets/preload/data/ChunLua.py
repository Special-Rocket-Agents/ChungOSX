import lupa
from lupa import LuaRuntime
from ply import lex, yacc

l = LuaRuntime

tokens = {
    "52554e", #! RUNNER
    "52454144", #! READ
    "4E554C4C" #! NUL
    ""
}