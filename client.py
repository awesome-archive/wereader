from wereader import get_bookshelf, get_chapters, \
    get_bookmarklist, get_bestbookmarks


'''
TODO:
    1. rewrite the main process to make it more user friendly
    2. provide a commandline interface for more convenience
'''

FLAG = True
TEST = False
CURRENT = None
INFO = '''
    -----------------------------------------------------
    -             请选择您想要执行的操作：
    -             1. 查看书架
    -             2. 搜索书架书籍
    -             3. 选择当前书籍
    -             4. 查看（导出）当前书籍目录
    -             5. 查看（导出）当前书籍热门划线
    -             6. 查看（导出）当前书籍笔记
    -             0. 退出
    -             help. 打印提示信息
    -----------------------------------------------------
'''


def show_shelf():
    print('您的书架如下:')
    for b in books:
        print(b.bookId, b.title, b.author)


def search_book():
    pass


def choose_current():
    global CURRENT

    bid = input("请输入当前选书籍的ID：")
    choosed_list = [x for x in books if x.bookId == bid]
    CURRENT = choosed_list.pop() if choosed_list else None

    if not CURRENT:
        print("没有找到书籍的ID，请确认后重试。")
        return

    print(f"已选择书籍《{CURRENT.title}》作为当前书籍。")


def see_content():
    global CURRENT

    bid = CURRENT.bookId
    for c in get_chapters(int(bid)):
        print('#'*c[0], c[1])


def see_popular():
    global CURRENT


def leave():
    global FLAG
    FLAG = False


def help_info():
    print(INFO)


func_map = {
    '1': show_shelf,
    '3': choose_current,
    '4': see_content,
    '0': leave,
    'help': help_info,
}


def test():
    global CURRENT
    CURRENT = [x for x in books if x.bookId == '907606'].pop()
    see_content()


def main():
    print('欢迎使用微信读书爬虫')

    try:
        global books
        books = get_bookshelf()  # get a list of namedtuple book
    except:
        print('请检查您的Cookie设置')
        return

    if TEST:
        test()
        return

    print(INFO)

    while FLAG:
        operation = input("您的选择是：").lower()
        func_map.get(operation, lambda: print("非法的选择"))()


def old_main():
    print('欢迎使用微信读书爬虫')
    try:
        books = get_bookshelf()
    except:
        print('请检查您的Cookie设置')
        return
    print('您的书架如下:')
    for b in books:
        print(b.bookId, b.title, b.author)

    while True:
        bid = input('想看哪本书的目录，请输入对应书籍id:')
        current_book = [x for x in books if x.bookId == bid][0]

        for c in get_chapters(int(bid)):
            print('#'*c[0], c[1])

        y = input('是否需要查看该书的热门划线，y/n?')
        if y.lower() == 'y':
            bb = get_bestbookmarks(bid)
            print(bb)

        y = input('是否需要查看你的笔记，y/n?')
        if y.lower() == 'y':
            bb = get_bookmarklist(bid)
            print(bb)

        y = input('是否需要保存你的笔记，y/n?')
        if y.lower() == 'y':
            bb = get_bookmarklist(bid)
            with open(f'{current_book.title}-{current_book.bookId}.txt', 'w') as f:
                f.write(bb)

        y = input('是否需要查看其他书，y/n?')

        if y.lower() == 'y':
            continue
        else:
            print('bye~')
            break


if __name__ == "__main__":
    # old_main()
    main()
