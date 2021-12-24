# 튜플
# : 읽기 전용 리스트
a = (3, 4, 5)
b = 3, 4, 5

c = (3,)
d = 3,

e = tuple([3, 4, 5])
f = list(range(10))
g = tuple(f)

h = 3, 4, 5
i = list(h)

# 튜플 관련 함수
x = 5, 6, 7, 8
print(max(x)) # 최댓값
print(min(x)) # 최솟값
print(sum(x)) # 합
print(x.count(6)) # 6의 개수
print(x.index(7)) # 7의 인덱스
