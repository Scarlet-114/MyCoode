import sys

# sys.path.append('my_module')
#下面这个可以提高优先级
sys.path.insert(0, "my_module")
print(sys.path)

import module1

if __name__ == '__main__':
    module1.test1()