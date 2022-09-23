# 实现批量修改文件名_by XiaoWang
# 现有代码：批量修改简悦导出的文件名

import os

Files_Path = r"E:\Study\Programing\Python\Note - Copy - Copy"  # 文件路径

File_List = os.listdir(Files_Path)  # 列出路径下的所有文件

PrefixName = "SR_"

for i_File in File_List:
    SplitedName = i_File.split('-', 1)
    if SplitedName[0] == "simpread":
        oldname = Files_Path + "\\" + i_File
        New_Name = "%s\\%s%s" % (Files_Path, PrefixName, SplitedName[1])  # 等价于下一行
        # New_Name = Files_Path + "\\" + PrefixName + SplitedName[1]
        os.rename(oldname, New_Name)

        # # 或者如下：
        # newname = PrefixName + SplitedName[1]
        # os.chdir(Files_Path)   # 改变当前工作目录
        # os.rename(i_File, newname)
        # print(os.path.basename(i_File) + ' -> ' + os.path.basename(newname)) # os.path.basename(path) 返回文件名


# portion = os.path.splitext(filename)  # 分离文件名字和后缀，这里不需要用

