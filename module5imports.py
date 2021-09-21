import sandwich
sandwich.make_sandwich('shredded lettuce', 'cheese', 'turkey', 'pickles', additional= 'ketchup')

from sandwich import make_sandwich
make_sandwich('shredded lettuce', 'cheese', 'black forest ham', 'pickles', additional= 'mayo')

from sandwich import make_sandwich as sn
sn('shredded lettuce', 'mozarella cheese', 'black forest ham', 'pickles', additional= 'ranch')

import sandwich as mn
mn.make_sandwich('shredded lettuce', 'mozarella cheese', 'black forest ham', 'pickles', additional= 'ranch')

from sandwich import *
make_sandwich('shredded lettuce', 'cheese', 'black forest ham', 'tomato', additional= 'mayo')