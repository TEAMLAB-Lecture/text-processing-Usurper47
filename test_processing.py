#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


# 뭐, 숫자까지 제거해줄지 말지에 대한 조건이 확실하지 않음.

def normalize(input_string:str) -> str:
  return ' '.join(input_string.lower().split())


def no_vowels(input_string:str) -> str:
  set_ = {'a','e','i','o','u'}
  res = ''
  
  for i in input_string:
    if i.lower() in set_:
      continue
    res += i
  
  return res