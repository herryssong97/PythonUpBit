# PythonUpBit

Python으로 업비트 자동매매프로그램 제작
2024.05.28 ~ 2024.06
-- 비트코인의 현재가격조회, 매수금액 입력 후 구매, 매도금액 입력 후 매도가 가능한 프로그램 제작 --
    ㅇ 이외 기능 : 매수/매도 최소금액 알림팝업, 에러처리 팝업

05.28
pip instal pyupbit, pip install pyqt5
Upbit : Open Api 자산조회, 주문조회, 주문하기, 출금조회, 입금조회 체크
특정 IP에서만 주문 가능하도록 IP 주소 등록까지
Access key와 Secret key 받아 따로 적어두기



pyqt5 패키지 속 class 객체 사용
현재가격(text) : label 위젯 사용
가격조회 창(text) : Text Edit 위젯 사용 (직접 타이핑 하는 부분)
조회버튼(button) : Push Button 위젯 사용
