#!coding=utf-8
import sys
import difflib
import os

def read_file(file_name):
    try:
        file_handle = open(file_name, 'r')
        text = file_handle.read().split()
        file_handle.close()
        return text
    except IOError as error:
        print('Read file Error: {0}'.format(error))
        sys.exit()

def compare_file(file1_name, file2_name):
    text1_lines = read_file(file1_name)
    text2_lines = read_file(file2_name)
    diff = difflib.HtmlDiff() 
    result = diff.make_file(text1_lines, text2_lines) 
    try:
        with open(r'C:\Users\User\Desktop\result.html', 'w') as result_file:     
            result_file.write(result)                     
    except IOError as error:
        print( '写入html文件错误：{0}'.format(error))


if __name__ == "__main__":
    compare_file(r'C:\Users\User\Desktop\A.txt', r'C:\Users\User\Desktop\B.txt')
    os.system("pause")
