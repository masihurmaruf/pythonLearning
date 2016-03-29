import builtins
import random
import time

#DATA = glossary.CONCEPTS
from time import gmtime, strftime


def pull_request():
    print()

def starts_lowercase_regex(name):
    """return true if starts with lowercase letter"""
   # print('calling regex')
    import re
    return re.match('[a-z]', name)

def starts_lowercase_string(name):
    """return true if starts with lowercase letter"""
   # print('calling string')
    import string
    return any(name.startswith(c) for c in string.ascii_lowercase)

starts_lowercase = starts_lowercase_string

def create_data():
    """return a dictionary of answers: definitions"""
    data_dict = {}
    for name in dir(builtins):
        if starts_lowercase(name):
            builtin_function = getattr(builtins, name)
            doc = builtin_function.__doc__
            if doc is not None:     
                placeholder = '*' * len(name)
                newdoc = placeholder.join(doc.split(name))
                data_dict[name] = newdoc
    return data_dict
DATA = create_data()


def ask_question(definition, answer):
    """takes definition and answer, quizzes userm return success (bool)"""
    time.sleep(.5)
    print ('tell me what name is associated with the followitn definition : ')
    print(definition)
    response = input('> ')
    success = response == answer
    if success:
        print('Correct')
    else :
        print('Incorrect - The correct answer is - ', answer)
    return success

def main():
    attempts = successes = 0
    keys = list(DATA)  #glossary.CONCEPTS)
    random.shuffle(keys)
    for answer in keys :
        definition = DATA[answer]  #glossary.CONCEPTS[answer]
        try:
            success = ask_question(definition, answer)
        except EOFError:
            break
        attempts += 1
        if success:
            successes +=1
    total = len(keys)
    final_message = '{successes}/{total} right! {attempts} attempts'.format(
                   successes=successes, total=total, attempts = attempts)
    print(final_message)
    result_file_name = 'results.log'
    open_file = open(result_file_name,'a')
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    with open_file as file_:
        file_.write(date+'\t->\t'+final_message +'\n')
if __name__ == '__main__':
    main()

