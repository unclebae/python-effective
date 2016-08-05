# _*_ coding: utf-8 _*_

# list[start:end] 형식으로 사용
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four : ', a[:4])
print('Last four : ', a[-4:])
print('Middle two : ', a[3:-3])

# 슬라이싱 결과는 새로운 리스트가 된다. 
b = a[4:]
print('Before : ', b)
b[1] = 99
print('After : ', b)
print('origin : ', a)

# 길이가 다른 슬라이스 값 할당. 
print('Before : ', a)
a[2:7] = [99, 22, 14]
print('After : ', a)

# 시작과 끝 모두 생략하면 원본의 복제본을 얻는다. 
b = a[:]
assert b == a and b is not a

# 슬라이스에서 시작, 끝 인덱스를 지정하지 않고 할당하는경우
# 새로운 복사본의 참조로 대체된다. 
b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b
print('After a :', a)
print('After b :', b)
