# 실습문제 2.4.1
# word_list에 들어 있는 문자열 중 첫 글자가
# a 인 것만 뽑아서 리스트로 만드세요.

word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

# 리스트 내포 사용하기 전 
# result = []
# for word in word_list:
#   if word[0] == 'a':
#     result.append(word)
# print(result)

# 리스트 내포를 사용한 수
result = [i for i in word_list if i[0] == 'a']
print(result)