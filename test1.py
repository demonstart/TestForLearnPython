#!./usr/bin/env.python
#.-*-.coding:utf-8
#.__author__:."liulifeng"
#.Date:.2018-11-23

i = 0
while i < 3:
    name = input('enter your name : ')
    pwd = input('enter your password : ')
    if name == '1' and pwd == '2':
        print('ok')
        break
    else:
        print('error')
    i += 1

print('test')


