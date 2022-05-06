# 1. 分别写两个样例程序来展现多线程、多进程的优势场景（语言不限）

# 2. 写一个脚本来验证Python的函数参数传递，传的究竟是参数的值，还是引用？
def a(arg1: list):
    arg1.append('new one')
    return arg1


if __name__ == '__main__':
    before_li = ['old_one']
    a(before_li)
    assert before_li == ['old_one', 'new one']
    print('如果是引用，那么列表中将有两个元素；如果是值传递，那么列表只有一个元素：%s' % str(before_li))


# 3. 写一个函数来将一个URL地址解析为协议、地址、端口、路径等部分，比如http://example.com:8080/users/将被解析为http、example.com、8080、/users/这几个部分（语言不限）
def phrase(url: str):
    part_one = url.split('://')[0]
    dic ={}
    li = []
    [1,2,3,4,5,6].insert(3,2)
