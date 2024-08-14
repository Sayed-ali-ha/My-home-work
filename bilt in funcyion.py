a = 4
print(abs(a))
4
a = [1,2,3]
print(all(a))
True
a = [1,2,3]
print(any(a))
True
b=90
print(bin(b))
0b1011010
print(bool(89))
True

a = b
print(callabel(a))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(callabel(a))
NameError: name 'callabel' is not defined. Did you mean: 'callable'?
a = b
print(callable(a))
False
print(chr(a))
Z
print(compile(9))
print(complex(2))
(2+0j)


Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

print(divmod(2,8))
(0, 2)
print(enumerate(2))

print(eval(2))
print(float(2))
2.0
print(format(90))
90
print(frozenset(9))
print(frozenset("d"))
frozenset({'d'})



print(hash(900))
900
print(help())
Welcome to Python 3.12's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
None
print(hex(2))
0x2
print(id(2))
140709503973848
