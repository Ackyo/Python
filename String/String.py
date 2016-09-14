string.split('\n')出现空字符串
solution:
1. 采用不带参split(),会把所有空格、制表符、换行符当分隔符
2. filter(None,s.split(' '))

