import re

with open('../chemistry_func.py','r',encoding='utf-8') as f:
    count=0
    for line in f:
        pattern=re.compile('class (.*?)\\(Func\\):')
        func_match = pattern.search(line)
        if func_match:
            name=func_match.group(1)
            count+=1
            print('               {},'.format(name))


    print('\n\n{}'.format(count))