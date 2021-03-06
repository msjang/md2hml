---
title: 마크다운 - 아래아한글 변환기, md2hml
author: 장민석 (msjang@kisti.re.kr)
date: 2018-02-06
---

# 1. 취지
정출연/정부기관/공공기관에서 HWP 없이는 업무가 불가능하다. 때문에 자주 사용하는 마크다운 파일을 HWP로 변환하여 사용하고자 한다.


# 2. 문법
공공기관에서 자주 이용하는 HWP 문서의 규칙은 다음과 같다.

* 대통령 보고서 작성규칙, 2007
    - http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=127916953)
* 행안부 문서작성 개선안, 2017.10.31

공공기관에서는 대부분 개조식으로 문서를 작성한다. 즉 indent로 여러 레벨을 나누어 목록 형태로 작성한다. 이는 마크다운 문법의 목록 기능을 활용하면 충분히 가능하다.


# 3. HWP 호환 방법
크게 2가지 방법이 있으나, 두번째 방법을 선택함

* 방법 1 : HTML 파일 출력
    - CSS를 제외한 HTML 기본문법으로 문서를 작성하고 확장자를 HWP로 변경하면 윈도우용 HWP에서 HTML을 자동으로 인식/변환하여 열린다
    - 은행 계좌거래내역을 엑셀파일로 export 하는 기능도 대부분 이렇게 구현되어 있다
* 방법 2 : HML 문법 준수
    - (주)한글과컴퓨터에서는 HWP와 호환되는 XML포멧인 HML을 공개하였다.
    - 이미지는 base64 인코딩을 통해 포함한다


# 4. 사용법
`python md2hml.py README.md readme.hml`


# A. 기타 메모

## A.1. HWP와 SW 전환 계획
이전 회사에서 PPT 대신에 reveal.js를 활용하여 발표자료를 작성한 적이 있다. 발표 이후에 팀장님께서 다음부터는 PPT를 이용하는 것이 좋겠다고 말했다. 회사에서 널리 사용하는 포멧을 활용해야 해당 문서의 재활용성이 증가한다. 그렇지 않으면 그 문서는 사장된다.

정출연/정부기관/공공기관은 HWP에 너무나 익숙하다. 연구자로써 그리고 IT인으로써 HWP를 걷어내는 것에는 동의한다. 하지만 소원처럼 빠르게 바꿀 수는 없다. 새로운 도구의 도입은 조직의 생산성과 관련되어 있고, 새로운 도구를 학습하는데는 상당한 시간이 소요된다. 때문에, 점진적인 SW 전환 계획이 필요하다.


## A.2. 하고 싶은 것
소속된 조직에 위키(컨플루언스)를 도입할 예정이다. 컨플루언스는 웹으로 작성한 페이지를 PDF/DOC로 다운로드 하는 기능이 있다. 컨플루언스 페이지를 HWP로 다운로드 받는 기능을 추가하고 싶다.

그리고, 평상시에 markdown, pandoc, jekyll 등을 활용하여 자료를 정리하고 있다. 이를 HWP로 출판하는 기능을 구현하고 싶다.

서브라임/ATOM 플러그인으로 만들어도 좋을 것 같다.


## A.3. 아직 구현하지 못한 기능

* 마크다운 기본 문법
    - 표
    - 링크
    - 이미지
    - 굵게, 기울임
    - 코드영역
    - 각주/미주
    - 페이지 분리; 하이픈 여러개, hr태그
* 템플릿 적용
    - pandoc의 reference-doc 기능
* XML 특수문자 처리
    - and, 꺽쇄괄호 등


## A.4. 1차 시도
일단은 정규식을 통해 일부분을 구현함; 수고스러운 일이 많았음


# B. 테스트

## B.1. 가
### B.1.1. 가나
#### B.1.1.1. 가나다
##### B.1.1.1.1 가나다라
###### B.1.1.1.1.1 가나다라마

가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라

* 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
    - 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
        + 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
* 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
    - 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
        + 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
            * 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
                - 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
* 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
    - 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
        + 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
            * 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
                - 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
                    + 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라 가나다라
