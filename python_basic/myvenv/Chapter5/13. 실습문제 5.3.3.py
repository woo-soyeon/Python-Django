# 실습문제 5.3.3
# Learning Korean

# 한국어 리스트
word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

print("Let's Learning Korean")
for word in word_list:
  print(word)
  data = input()
  if data != word:
    break