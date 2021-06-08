<h1 align="center"> Commit Bot </h1> <br>

<p align="center">
  <a href="https://gitpoint.co/">
    <img alt="GitPoint" title="GitPoint" src="https://user-images.githubusercontent.com/48384692/121125373-6e216f80-c861-11eb-92aa-90f5a8bdd83d.png" width="300">
  </a>
</p>

## Introduction
Slack 채널에서 Bot에게 커밋 알림을 받을 수 있다.
다른 사용자와 비교하여 오늘 하루 커밋을 확인하고
일일커밋 챌린지를 지속할 수 있는 동거부여 서비스

## Features
### 완료
1. 오늘 커밋 개수 알려줘!  
커밋봇이 오늘 커밋 개수를 알려줍니다! 

2. 오늘 커밋 랭킹 알려줘!  
서비스에 속한 사용자들의 커밋 개수를 비교하고 1등을 알려줍니다!

3. 로그인  
모든 기능은 Github ID와 Slack name을 입력해 로그인 한 후 이용할 수 있습니다.

### 계획
- 랭킹 성능 개선
- 커밋이 0개면 일정시간마다 알림

## Stack
- Python 3.8
- Flask
- Sqlalchemy

## Developing Log

#### 목표
- [x] Slack Bot 만들어보기
- [x] poetry로 패키지 관리하기
- [ ] 테스트 코드 작성하기
- [ ] 서버리스 서비스로 배포하기
