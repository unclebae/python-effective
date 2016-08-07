# _*_ coding: utf-8 _*_

# 메모리를 많이 먹는다. 매우 큰 파일이면 문제가 될 수 있음...
value = [len(x) for x in open('my_file.txt')]
print(value)

#제너레이션의 사용. 
it = (len(x) for x in open('my_file.txt'))
print(it)
print(next(it))
print(next(it))

roots = ((x, x**0.5) for x in it)
print(next(roots))
