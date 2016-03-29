"""this is a reusable Python module
intended to accumulate my python lerning"""


from pprint import pprint

CONCEPTS = dict(
  kewywords = 'reserved words in Python you cannot use as variable names',
  variables=r'names in Python that point to objects - [A-za-z_][\w]*',
  arity='number of arguments a function takes: nullary, unary, binary, ternary',
  docstrings='strings at the top of a module, class or function definition that document the code',
  comments=' # (the octothorpe)- amd anything that follows it',
  naming="name your objects so well that you don't need comments",
)

def main():
    """Pretty prints the data in this module"""
    pprint(CONCEPTS)

if __name__ == '__main__':
    main()
