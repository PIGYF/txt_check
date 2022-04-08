#!coding=utf-8
# 2018-9-19
import sys
import difflib
import os


# 读取配置文件函数
def read_file(file_name):
    try:
        file_handle = open(file_name, 'r')
        text = file_handle.read().split()  # 读取后以行进行分割
        file_handle.close()
        return text
    except IOError as error:
        print('Read file Error: {0}'.format(error))
        sys.exit()


# 比较两个文件并输出html格式的结果
def compare_file(file1_name, file2_name):
    text1_lines = read_file(file1_name)
    text2_lines = read_file(file2_name)
    diff = difflib.HtmlDiff()  # 创建htmldiff 对象
    result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
    #  将结果保存到result.html文件中并打开
    try:
        with open(r'C:\Users\User\Desktop\result.html', 'w') as result_file:      #同 f = open('result.html', 'w') 打开或创建一个result.html文件
            result_file.write(result)                      #同 f.write(result)
    except IOError as error:
        print( '写入html文件错误：{0}'.format(error))


if __name__ == "__main__":
    compare_file(r'C:\Users\User\Desktop\A.txt', r'C:\Users\User\Desktop\B.txt')          #传入两文件的路径
    os.system("pause")
