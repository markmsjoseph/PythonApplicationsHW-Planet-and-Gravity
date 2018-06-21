
def debug(old_f):#takes in minumin as an argument
    #this new_f will print the arguments and return what the minimum function returns
    def new_f(*args):
        res = old_f(*args)
        for i in range(len(args)):
            print("Argument " + str(i + 1)+ ": " + str(args[i])+ ", " + str(type(args[i])))
        print("Returns " + str(res) + ', ' + str(type(res)))
        return res
    return new_f

#above the function that you want modified you place the @FunctionThatDoesModification
@debug
def minimum(*args):
    return min(*args)

debugMin = minimum(1,-9,3)




def limit_one_call(func):
   def new_func(*args):
     nonlocal x
     if not x:
       try:
         return func(*args)
       finally:
         x = True
   x = False
   return new_func


@limit_one_call
def func(res):
   return res

# limited_print = limit_one_call(print)
# limited_print('hello')
# limited_print('howdy')
# limited_print('hola')


def count(func):
   x = 1
   def new_func(*args):
     nonlocal x
     if x:
       try:
         return func(*args)
       finally:
         x = x + 1
         print("Function called " + str(x - 1) + " times")
   return new_func


@count
def func(res):
   return res

# limited_print = count(print)
# limited_print('hello')
# limited_print('howdy')
# limited_print('hola')
# limited_print('hola')