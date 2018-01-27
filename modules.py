# 이름공간: 이름(변수)이 저장되는 공

# 모듈의 전역공간
globals()
# 모듈의 지역공간
locals()

import os
# os에 정의된 각종 속성 이름
dir(os)
# 속성에 정의된 값 확인
os.__dict__
os.__dict__.keys()

# 파이썬이 검색하는 디렉토리 경로
import sys
sys.path
sys.path.append('~/mypythonlib')

