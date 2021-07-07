# OpenDART

[![](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org)
[![](https://img.shields.io/badge/opendart-0.1.0--alpha-yellow)](https://github.com/JehunYoo/opendart)

대한민국 전자공시시스템 [DART](http://dart.fss.or.kr)에서 제공하는 API를 활용한 재무제표 및 재무제표 항목 추출 라이브러리

## Features
### API
* 공시정보 - 고유번호
* 상장기업 재무정보 - 단일회사 전체 재무제표

### Others
* 고유번호 검색
* 재무제표 항목 검색 및 추출

## Usage
### Dart API Key
API Key는 [OpenDART](https://opendart.fss.or.kr)에서 신청

### Quickstart
``` python
import opendart as dart

dart.DartAPI().api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
kakao = dart.Corporation('카카오') # 카카오 (035720) 객체 생성
kakao.load_fs(2020, 4) # 2020년 4분기 연결재무제표 불러오기
operating_income = kakao.fs['2020+4'].find('영업이익', 0) # 2020년 4분기 연결재무제표 당기 영업이익 추출

print(kakao.fs['2020+4']) # Consolidated Financial Statement of 00258801@2020-4
print(operating_income.v) # 455855515211
print(operating_income.n) # 포괄손익계산서:영업이익
```

## API Limit
* 개인 기준 일 10000회로 API 요청 제한
* 분당 1000회 이상 API 요청시 IP 차단

## License
[MIT License](LICENSE)