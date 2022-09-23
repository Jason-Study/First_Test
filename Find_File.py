# 查找文件小程序
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017623135437088#0

import os
import sys


def findfile(path, name):
    nodes = os.listdir(path)

    for f in nodes:

        full = os.path.join(path, f)

        if f.startswith(name) and os.path.isfile(full):
            print('find file %s' % os.path.join(path, f))

        if os.path.isdir(full):
            findfile(full, name)  # 递归查找子文件夹


if __name__ == '__main__':

    # abspath = os.path.abspath('.')
    abspath = 'E:\\Study\\Programing\\Python\\Test'

    args = sys.argv[1:]

    if args:

        findfile(abspath, args[0])

    else:

        findfile(abspath, 'README')  # 查找README文件
