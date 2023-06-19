#for one Error
#for value error
try:
    num1 = int(input("number: "))
    num2 = int(input("number: "))
    num3 #Doesn't count
    print(num1 + num2)
except ValueError():
    print("The value is not int")
#for name error
try:
    num1 = int(input("number: "))
    num2 = int(input("number: "))
    print(num1 + num2)
except NameError():
    print("The value is not int")

#for all Error
try:
    num1 = int(input("number: "))
    num2 = int(input("number: "))
    print(num1 + num2)
except:
    print("The value is not int")
    exit()
print("hello")
#Description	Exception
#Raised when the assert statement fails	AssertionError
#Raised on the attribute assignment or reference fails	AttributeError
#Raised when the input() function hits the end-of-file condition	EOFError
#Raised when a generator’s close() method is called	GeneratorExit
#Raised when the imported module is not found	ImportError
#Raised when the index of a sequence is out of range	IndexError
#Raised when a key is not found in a dictionary	KeyError
#Raised when the user hits the interrupt key (Ctrl+c or delete)	KeyboardInterrupt
#Raised when an operation runs out of memory	MemoryError
#Raised when a variable is not found in the local or global scope	NameError
#Raised by abstract methods	NotImplementedError
#Raised when a system operation causes a system-related error	OSError
#Raised when the result of an arithmetic operation is too large to be represented	OverflowError
#Raised when a weak reference proxy is used to access a garbage collected referent	ReferenceError
#Raised when an error does not fall under any other category	RuntimeError
#Raised by the next() function to indicate that there is no further item to be returned by the iterator	StopIteration
#Raised by the parser when a syntax error is encountered	SyntaxError
#Raised when there is an incorrect indentation	IndentationError
#Raised when the indentation consists of inconsistent tabs and spaces	TabError
#Raised when the interpreter detects internal error	SystemError
#Raised by the sys.exit() function	SystemExit
#Raised when a function or operation is applied to an object of an incorrect type	TypeError
#Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable	UnboundLocalError
#Raised when a Unicode-related encoding or decoding error occurs	UnicodeError
#Raised when a Unicode-related error occurs during encoding	UnicodeEncodeError
#Raised when a Unicode-related error occurs during decoding	UnicodeDecodeError
#Raised when a Unicode-related error occurs during translation	UnicodeTranslateError
#Raised when a function gets an argument of correct type but improper value	ValueError
#Raised when the second operand of a division or module operation is zero	ZeroDivisionErrorstatement fails	AssertionError
#Raised on the attribute assignment or reference fails	AttributeError
#Raised when the input() function hits the end-of-file condition	EOFError
#Raised when a generator’s close() method is called	GeneratorExit
#Raised when the imported module is not found	ImportError
#Raised when the index of a sequence is out of range	IndexError
#Raised when a key is not found in a dictionary	KeyError
#Raised when the user hits the interrupt key (Ctrl+c or delete)	KeyboardInterrupt
#Raised when an operation runs out of memory	MemoryError
#raised when a variable is not found in the local or global scope	NameError
#Raised by abstract methods	NotImplementedError
#Rased when a system operation causes a system-related error	OSError
#Raised when the result of an arithmetic operation is too large to be represented	OverflowError
#Raised when a weak reference proxy is used to access a garbage collected referent	ReferenceError
#Raised when an error does not fall under any other category	RuntimeError
#Raised by the next() function to indicate that there is no further item to be returned by the iterator	StopIteration
#Raised by the parser when a syntax error is encountered	SyntaxError
#Raised when there is an incorrect indentation	IndentationError
#Raised when the indentation consists of inconsistent tabs and spaces	TabError
#Raised when the interpreter detects internal error	SystemError
#Raised by the sys.exit() function	SystemExit
#Raised when a function or operation is applied to an object of an incorrect type	TypeError
#Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable	UnboundLocalError
#Raised when a Unicode-related encoding or decoding error occurs	UnicodeError
#Raised when a Unicode-related error occurs during encoding	UnicodeEncodeError
#Raised when a Unicode-related error occurs during decoding	UnicodeDecodeError
#Raised when a Unicode-related error occurs during translation	UnicodeTranslateError
#Raised when a function gets an argument of correct type but improper value	ValueError
#Raised when the second operand of a division or module operation is zero	ZeroDivisionError