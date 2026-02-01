import re

def simple_use():
    result = re.match("abc", "abcdef")
    if result:
        print(result)
        print(result.group())

def single():

    ret = re.match('.','1234')
    print(ret.group())
    ret = re.match('a.c', 'abcdef')
    print(ret.group())

    print("-"*50)

    # 大小写h都可以的情况
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())
    # 匹配0到9第一种写法
    ret = re.match("[0123456789]Hello Python", "7Hello Python")
    print(ret.group())
    # 匹配0到9第二种写法
    ret = re.match("[0-9]Hello Python", "7Hello Python")
    print(ret.group())
    #35一起写因为是单个字符所以被识别成3和5
    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())
    # 下面这个正则不能够匹配到数字4，因此ret为None
    ret = re.match("[0-35-9]Hello Python", "4Hello Python")
    # print(ret.group())

    print('-'*50)

    # 使用\d进行匹配
    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())

def multialp():
    '''
    多字符
    :return:
    '''
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())

    print("-"*50)

    names = ["name1", "_name", "2_name", "__name__"]
    for name in names:
        ret= re.match(r"[a-zA-Z_]+\w*",name)
        if ret:
            print(f"{name}是正确的")
        else:
            print(f"{name}是错的")

    print("-"*50)

    #?的练习, 0或1次
    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())

    print("-"*50)
    #{m}的练习

    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())

    #默认是贪婪的
    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
    print(ret.group())

def start_end():
    '''
    ^开头
    $结尾
    :return:
    '''
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com" ]
    for email in email_list:
        ret = re.match(r"[\w]{4,20}(@163\.com)$", email)
        if ret:
            print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
        else:
            print("%s 不符合要求" % email)

def match_group():
    '''
    分组匹配
    :return:
    '''

    #要求匹配1-99, |用法
    ret = re.match(r"[1-9][0-9]|[1-9]","11")
    print(ret.group())
    ret = re.match(r"[1-9][0-9]|[1-9]","09")
    # print(ret) 这个匹配失败

    print("*"*50)
    #()的用法
    ret = re.match(r"\w{6,20}@(126|qq|163)\.com$", "1197819910@qq.com")
    print(ret.group())

    print("*"*50)

    #提取分组
    ret = re.match(r"([^-]+)-(\d+)", "010-141242")
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

    print("*"*50)

    #\number可以匹配分组

def use_findier():
    '''
    finditer
    :return:
    '''
    ret = re.finditer(r"\d+", "8888,  9999")
    print(next(ret).group())
    print(next(ret).group())


def add(temp):
    num = int(temp.group()) + 1
    return str(num)
def use_sub():
    ret = re.sub(r"\d+", add, '999')
    print(ret)

def use_sub2():
    long_text = '''
    <div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<
br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，day13-特征工程，sklearn，高性能，大并发。</p>
</div>
    '''
    ret =  re.sub(r"<[^>]*>|&nbsp;|\n|\s", "", long_text)
    print(ret)



if __name__ == '__main__':
    # single()
    # multialp()
    # start_end()
    # match_group()
    # use_findier()
    # use_sub()
    use_sub2()