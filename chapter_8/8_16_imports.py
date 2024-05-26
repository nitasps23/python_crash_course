# Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import shirt_function

shirt_function.make_shirt('M', 'Awesome!')
shirt_function.make_shirt(text='Awesome!', size='M')

from shirt_function import make_shirt

make_shirt('M', 'Awesome!')
make_shirt(text='Awesome!', size='M')

from shirt_function import make_shirt as mf

mf('M', 'Awesome!')
mf(text='Awesome!', size='M')

import shirt_function as sf

sf.make_shirt('M', 'Awesome!')
sf.make_shirt(text='Awesome!', size='M')

from shirt_function import *

make_shirt('M', 'Awesome!')
make_shirt(text='Awesome!', size='M')