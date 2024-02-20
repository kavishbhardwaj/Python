def foo():
    def bar():
        print('bar is inside foo')
    bar()

foo()

# bar can not be called from outside foo() 
    


def foo():
    pass

'''pass is a keyword in Python. 
When the interpreter comes across a pass statement, 
it doesn't perform any computation and moves on to the next line'''

print(foo())
#None is returned if no return statement is present