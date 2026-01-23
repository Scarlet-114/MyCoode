import copy
def no_use_copy():
    '''
    a发生改变
    :return:
    '''
    a = [1, 2, 3]
    b = a
    b[0] = 10
    print(a)



def use_list_copy():
    '''
    这是浅拷贝
    a不发生改变
    :return:
    '''
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 10
    print(a)

def use_copy():
    '''
    用copy包里的copy
    :return:
    '''
    c = [1, 2, 3]
    d = c
    e = copy.copy(c)
    print(id(c))
    print(id(d))
    print(id(e))

def use_copy2():
    '''
    copy也是浅拷贝
    这里a变化, c和d里的 a, b都会变化
    :return:
    '''
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    a[0] = 10
    print(f"c - {c}")
    print(f"d - {d}")

def use_deep_copy():
    '''
    深拷贝
    d里面的两个元素地址都与a.b不同
    :return:
    '''
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    a[0] = 10
    print(f"c - {c}")
    print(f"d - {d}")

if __name__ == '__main__':
    no_use_copy()
    print('-'*50)
    use_list_copy()
    print('-'*50)
    use_copy()
    print('-'*50)
    use_copy2()
    print('-'*50)
    use_deep_copy()