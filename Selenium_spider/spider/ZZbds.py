#正则表达式学习
import re

a = '1234567890!@#$%^&*()qwertyuiop{}<>GHJ>dsa<?dsada123'

b = re.findall(r'[A-Za-z0-9_]',a)

print(b)