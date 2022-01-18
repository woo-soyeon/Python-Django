# 실습문제 6.1.1
# 날짜 형식 검사하기

# YYYY/MM/DD 형식으로 표현된 날짜를 검사하는 정규표현식 만들기

# 1. 연도는 4자리 숫자로 제한한다 (1000~9999)
# 2. 월은 1월~12월, 일은 1일~31일 까지 가능하다.

# ^\d{4}/(0[1-9]|1[0-2])/(0[1-9][12][0-9]|3[01])$

from distutils.command.config import LANG_EXT
import re

datas = [
  '2022/08/08',
  '1000/01/01',
  '9999/12/31',
  '900/02/02',
  '12000/10/26',
  '2021/13/01',
  '2023/2/02',
  '2024/06/3',
  '2023/06/35',
]

regex = '^\d{4}/(0[1-9]|1[0-2])/(0[1-9][12][0-9]|3[01])$'

for data in datas:
  matchObj = re.match(regex, data)
  result = (lambda x : True if x != None else False)(matchObj)
  print(f'{data} {result}')