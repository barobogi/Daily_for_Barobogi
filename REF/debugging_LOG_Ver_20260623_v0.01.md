# Debugging Log — Diary_for_Barobogi 2026-06-23 v0.01

---

## 이슈 #1: multimedia.json — 영상 항목 소실 (2개만 남음)

### 증상
- Multimedia 탭에 동영상이 2개밖에 표시 안 됨
- 실제 처리한 영상은 7개 (5개 소실)

### 원인 분석

```
[두 시스템이 같은 파일을 독립적으로 수정]

시스템 A: Render 백엔드 (github_service.py)
  → GitHub API로 _data/multimedia.json에 새 항목 추가 (직접 GitHub 수정)
  → 마크다운 요약도 Multimedia/ 폴더에 저장

시스템 B: 로컬 master_watch.py (자동 동기화)
  → 로컬 파일 변경 감지 → git add → commit → push

충돌 발생 순서:
  1. Render가 GitHub API로 영상 항목 추가 (remote에만 반영, local pull 없음)
  2. 로컬에서 multimedia.json BOM 제거 작업 (88e3668, 2026-06-22 06:34)
  3. git pull 없이 push → remote의 최신 항목들을 2개짜리 로컬 버전으로 덮어씀

소실된 영상 (5개):
  - (주간시황) 주가가 너무 오를때는 단기고점인지 고민하자!!!
  - 엔비디아 GPU 조립 개발 모두 로봇이 하는 시대 온다..
  - (DRAM) 지금시장의 주도ETF는 여전히 상승 가능성 많다
  - (스페이스X) 심리는 매수, 펀더멘탈은 매도, 쉬는 것도 투자다
  - 앞으로 10년의 부를 좌우할, 시대를 담은 포트폴리오
```

### BOM이란?

UTF-8 BOM(Byte Order Mark) = 파일 맨 앞의 보이지 않는 3바이트(`EF BB BF`).
메모장/PowerShell이 자동으로 붙임. 브라우저 JSON 파싱 오류 원인.
BOM 제거 커밋 자체는 옳았지만, `git pull` 없이 push한 것이 문제.

### 복구 방법

Multimedia/ 폴더 마크다운 파일 + git blob(주간시황)에서 내용 재구성.
`_data/multimedia.json`에 5개 항목 추가 → 커밋 `ab64474` (워처 자동 push).

### 재발 방지

**근본 원인**: Render 백엔드와 로컬 master_watch.py가 같은 파일을 독립적으로 수정.

**해결 방향**:
```
Option 1 (단기): Render 백엔드의 multimedia.json 쓰기를 중단하고
  마크다운 파일만 저장 → 로컬에서 스크립트로 JSON 재생성 (단일 소스)

Option 2 (장기): multimedia.json을 Firebase에 저장 →
  Render 백엔드도 Firebase에 쓰고, 페이지도 Firebase에서 읽음 (충돌 없음)

임시 조치: multimedia.json 수정 시 항상 git pull 먼저 실행
```

### 교훈

> **두 시스템이 같은 파일을 수정하는 구조는 언젠가 충돌한다.**
> GitHub API 수정 = remote만 변경됨. 로컬 push 전 반드시 git pull.
> 특히 master_watch.py는 로컬 변경을 자동 push하므로 remote 변경을 모름.

---

*기록자: Claude Sonnet 4.6 / 2026-06-23*
