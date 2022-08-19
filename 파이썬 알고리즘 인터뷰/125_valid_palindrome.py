import re

# 입력
str_data = str(input())

# 데이터 전처리 : 특수문자 제거 -> 공백 제거 -> 소문자로 치환
pattern_punctuation = re.compile(r'[^\w\s]')
str_data = pattern_punctuation.sub('', str_data)
str_data = str_data.replace(" ", "")
str_data = str_data.lower()

# 문자열 reversed
reversed_str = str_data[::-1]

if str_data == reversed_str:
    print(True)
else:
    print(False)