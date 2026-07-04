# 📚 Study Dashboard → AI Study 통합 제안 v0.2

**작성**: 코니 | **작성일**: 2026-07-04 (v0.2: 만복 피드백 반영 — n8n webhook 연계 추가)
**목표**: `Study_Dashboard`(공부방, Firebase 인터랙티브 앱)의 10개 탭을 `Daily_for_Barobogi`의 **AI Study 게시판 하나**로 녹여내기

> **바로보기님 승인 완료** (만복 경유, 2026-07-04)

---

## 1. 현황 비교

### Study Dashboard (barobogi.github.io/Study_Dashboard/)
Firebase 기반 단일 HTML, 10개 탭의 "즉시 캡처 + 추적" 도구:

| 탭 | 역할 | 데이터 흐름 |
|---|---|---|
| 🗺️ 로드맵 | AI 엔지니어 3단계 커리큘럼 체크 | Firebase RTDB, 진도% |
| ⚡ 오늘의 발견 | 즉흥 학습 메모 (카테고리 태그) | Firebase RTDB |
| 📓 학습일지 | 날짜별 학습기록 + 시간 + 기분 | Firebase RTDB |
| 📝 메모장 | 나중에 찾아볼 것 (완료/미완료) | Firebase RTDB |
| 📚 개념노트 | 개념 카드, 이해여부 체크 | Firebase RTDB, CRUD |
| 🏆 프로젝트 | 완료 프로젝트 포트폴리오 | Firebase RTDB |
| 🎯 퀴즈 | Claude가 개념 기반 문제 출제 | Firebase relay → desktop_daemon.py → Claude Haiku |
| 🤖 AI 설명 | 개념 설명 요청 | 위와 동일 daemon relay |
| 📊 통계 | 주간시간/카테고리/로드맵 달성률 | Chart.js, Firebase 집계 |
| 📰 만복이 News | GeekNews 기술 트렌드 큐레이션 | 만복이 매일 분류 |

### AI Study (Daily_for_Barobogi/ai-study.html)
GitHub API 직접 커밋 방식의 **정적 블로그형** 게시판 — 이미 존재하는 폴더:
- 카테고리: AI & Next.js / Machine Learning / Prompt Engineering / Web Dev / Deep Learning / Data Science / Python / Other
- 형식: 긴 호흡의 정리된 기술 포스트 (핵심기술, 함정, 배운점, 성장관점 구조)
- 저장: 브라우저에서 PAT로 GitHub commit (Firebase 없음, daemon 불필요)

**핵심 차이**: Study Dashboard = 매일 즉흥적으로 쌓는 "원재료" 캡처 도구. AI Study = 다듬어서 발행하는 "완제품" 블로그. 지금은 완전히 분리된 두 사이트라 원재료가 완제품으로 자동 연결되지 않음.

---

## 2. 통합 매핑안 — AI Study 게시판 하나로

| Study Dashboard 탭 | 통합 방식 | 비고 |
|---|---|---|
| 📓 학습일지 | **그대로 포스트 흡수** — 짧은 카드 포맷으로 AI Study 리스트에 자동 추가 | 형식이 가장 유사, 우선순위 1위 |
| ⚡ 오늘의 발견 | AI Study 리스트 상단에 **"빠른 기록" 필터** 신설, 짧은 카드로 표시 | 정식 포스트와 구분되는 배지 부여 |
| 📚 개념노트 | 카테고리 필터에 **"개념사전" 뷰** 추가 — 카드형 사전처럼 별도 정렬 | 이해여부 체크 유지 |
| 📝 메모장 | AI Study 페이지 **사이드바 위젯** "궁금한 것" — 완료 시 개념노트로 승격 유도 | 승격 흐름 = 특허3 "검정승격" 컨셉과 유사 재미있는 지점 |
| 🏆 프로젝트 | 기존 포스트에 **프로젝트 태그**로 흡수 (별도 탭 불필요) | 이미 태그 시스템 있음 |
| 🗺️ 로드맵 | 페이지 **상단 진행률 배지** (달성률 %) — read-only 요약만 표시 | 상세 체크는 유지하되 표시만 통합 |
| 📊 통계 | 페이지 상단 **통계 바**(Chart.js) — 주간 작성수/카테고리 분포 | 기존 stats.html과 중복 여부 확인 필요 |
| 🎯 퀴즈 / 🤖 AI 설명 | 각 포스트 하단 **"이 글로 퀴즈 풀기" / "AI에게 물어보기" 버튼** (온디맨드 위젯) | daemon 의존 기능이라 후순위 |
| 📰 만복이 News | **통합 안 함** — 성격이 다름(뉴스 큐레이션). Home 탭 위젯으로 유지 권장 | |

---

## 3. 기술적 쟁점 (반드시 먼저 결정할 것)

1. **백엔드 이원화 문제**: AI Study는 GitHub API 직접 커밋(정적, PAT 필요), Study Dashboard는 Firebase RTDB(실시간, daemon 필요). 하나로 합치면 한 페이지에서 두 저장소를 동시에 다뤄야 함.
   - 안 A: 텍스트 콘텐츠(학습일지/발견/개념)는 GitHub 커밋으로 통일, 인터랙티브 기능(퀴즈/AI설명/체크박스 진도)만 Firebase 유지 → 하이브리드
   - 안 B: 전부 Firebase로 통일하고 AI Study도 Firebase 기반으로 재작성 (기존 GitHub 커밋 포스트 마이그레이션 필요, 공수 큼)
   - **권장**: 안 A (하이브리드) — 기존 자산 재사용 극대화

2. **daemon 의존성 → n8n으로 대체 (v0.2, 만복 피드백 반영)**: 기존 daemon(desktop_daemon.py) 방식은 PC가 꺼져있으면 실패하고 API 크레딧도 소모함. n8n 설치 완료 후 아래 파이프라인으로 대체:

```
Study Dashboard Firebase에 학습일지/발견 저장
    → n8n webhook trigger (Firebase onWrite 감지)
    → Claude CLI subprocess 호출 (claude.ai 구독 기반, API 크레딧 불필요)
    → AI Study GitHub 자동 커밋
```

장점: daemon 상주 불필요(n8n이 트리거 수신 시점에만 동작), API 크레딧 불필요. 퀴즈/AI설명 기능도 동일 패턴으로 대체 가능(Firebase 요청쓰기 → n8n → Claude CLI → Firebase 응답쓰기) — 이러면 §4 우선순위표의 "daemon 의존성 High 난이도" 문제도 함께 해소됨.

3. **중복 통계**: Daily_for_Barobogi에 이미 `stats.html`이 별도로 존재 — Study Dashboard 통계와 병합할지, 그대로 둘지 확인 필요.

4. **n8n 착수 조건**: 위 파이프라인은 n8n 설치/안정화가 선행되어야 함(현재 Node.js 버전 문제로 진행 중, 2026-07-04 기준 미완료). n8n 완료 전까지는 기존 daemon 방식으로 우선 프로토타입하고, n8n 완료 즉시 교체하는 순서 권장.

---

## 4. 우선순위 (구현 순서 제안)

| 우선순위 | 항목 | 난이도 | 이유 |
|---|---|---|---|
| ⭐⭐⭐ | 학습일지 → 포스트 자동 흡수 | Low | 형식 가장 유사, 즉시 가치 |
| ⭐⭐⭐ | 오늘의 발견 → 빠른기록 필터 | Low | 캡처 습관 안 끊기게 하는 게 핵심 |
| ⭐⭐ | 개념노트 → 개념사전 뷰 | Medium | Firebase CRUD 유지 필요 |
| ⭐⭐ | 로드맵/통계 → 상단 요약 배지 | Medium | Chart.js 재사용 |
| ⭐ | 메모장 → 사이드바 위젯 | Low | |
| ⭐ (n8n 완료 시 Medium으로 하향) | 퀴즈/AI설명 → 온디맨드 버튼 | High → n8n 완료 후 Medium | n8n webhook으로 daemon 의존성 해소 가능 |
| — | 만복이 News | 통합 제외 | 별도 유지 |

**1단계(반나절)**: 학습일지 + 오늘의 발견만 우선 흡수 → 데모로 확인 후 나머지 진행

---

## 5. 다음 단계

- 이 제안서 바로보기님 검토/승인
- 승인 시 만복에게 실행 위임 (AI_hub messages 채널로 전달 예정, PHASE2_PROPOSAL.md 패턴처럼 단계별 진행)
- 1단계 완료 후 데모 → 2단계 진행 여부 결정

*본 문서는 코니가 두 사이트를 직접 fetch하여 구조 분석 후 작성한 초안이며, 실제 코드 구현 전 바로보기님 확인 필요.*
