# Diary_for_Barobogi — 디버깅 로그
> 프로젝트: Today for Barobogi (GitHub Pages 웹사이트)
> 시작일: 2026-06-20
> 저장소: https://github.com/barobogi/Daily_for_Barobogi

---

## v0.01 — 2026-06-20 | Phase 1 초기 구축

### 작업 내용
| 파일 | 변경 사항 |
|------|-----------|
| `index.html` | Stock 탭 추가 (nav) |
| `logs.html` | Stock 탭 추가 (nav) |
| `ai-study.html` | Stock 탭 추가 (nav) |
| `stock-dashboard.html` | 신규 생성 — Stock 탭 페이지 |

### 주요 결정 및 이슈

#### ✅ [해결] Stock 탭 iframe URL — Netlify → GitHub Pages 변경
- **증상**: Cowork 1차 안에서 Netlify URL(`https://barobogi-stock-dashboard.netlify.app/stock-dashboard.html`) 사용
- **원인**: Netlify 무료 플랜 유효 업데이트 횟수 초과 이슈 (stock_dashboard 프로젝트에서 이미 GitHub Pages 전환 진행 중)
- **해결**: iframe src를 GitHub Pages URL로 교체
  - Before: `https://barobogi-stock-dashboard.netlify.app/stock-dashboard.html`
  - After: `https://barobogi.github.io/stock_dashboard/stock-dashboard.html`
- **효과**: stock_dashboard repo에 push할 때마다 자동 반영 (업데이트 횟수 제한 없음)

#### ℹ️ [확인 필요] stock_dashboard GitHub Pages 활성화 여부
- `https://github.com/barobogi/stock_dashboard` 레포에서 Settings → Pages → Source = `main` 브랜치로 설정되어 있어야 함
- GitHub Pages가 비활성 상태면 iframe 빈 화면 표시됨
- **Action**: 배포 후 stock 탭에서 정상 렌더링 확인 필요

#### ✅ [완료] Cowork 추가 기능 — stock-dashboard.html 다크모드
- Cowork가 stock-dashboard.html에 다크모드 토글(🌙/☀️) 추가
- CSS 변수 기반(`--bg-primary`, `--accent` 등) 라이트/다크 전환
- `localStorage`에 테마 저장 → 새로고침 후에도 유지
- 시스템 다크모드 자동 감지(`prefers-color-scheme`) 지원

---

## ⚠️ 미해결 / 향후 과제

### 구조적 이슈
1. **다크모드 미통일**: `stock-dashboard.html`만 다크모드 적용, 나머지 3페이지(index, logs, ai-study)는 미적용
   - Cowork 2차 제안 후 통일 예정

2. **Stock 탭 iframe X-Frame-Options 차단 가능성**
   - 일부 사이트는 iframe 임베딩 차단 헤더를 설정함
   - GitHub Pages는 기본적으로 허용이나, 배포 후 실제 렌더링 확인 필요

3. **Stock 페이지 header max-w-7xl vs 타 페이지 max-w-4xl 불일치**
   - stock 페이지는 대시보드 특성상 더 넓은 레이아웃 사용 (의도적)
   - 향후 통일 여부는 2차 디자인 개선 시 결정

### 기능 공백 (Phase 2 예정)
- [ ] 다크모드 전체 페이지 통일
- [ ] Logs / AI Study 페이지 태그 필터 기능
- [ ] 홈 페이지 Stats 위젯 (총 로그 수, AI 학습 수 등)
- [ ] FIRE 진행 현황 미니 카드 (stock 대시보드 연동)

---

## 배포 이력

| 날짜 | 버전 | 커밋 메시지 | 비고 |
|------|------|-------------|------|
| 2026-06-20 | v0.01 | feat: Phase 1 - Add Stock Dashboard tab | 초기 4탭 구조 완성, GitHub Pages 배포 |
| 2026-06-20 | v0.02 | fix: Phase 2 dark mode + 버그 수정 | 다크모드/검색필터/애니메이션 전체 적용, 버그 3건 수정 |
| 2026-06-20 | v0.03 | feat: Phase 2b - Stats & Goals 추가 + 버그 수정 | stats.html/goals.html 신규, Goals 탭 누락 4개 페이지 추가, 중복 class 2건 수정 |

---

## v0.02 — 2026-06-20 | Phase 2a (Task #5~7)

### Cowork 작업 내용 (Task #5, 6, 7)
| Task | 내용 | 파일 |
|------|------|------|
| #5 다크모드 | CSS 변수 기반 라이트/다크 전환, localStorage 저장, 시스템 감지 | 전체 4페이지 |
| #6 검색 & 필터 | 실시간 검색 + 태그/카테고리 필터 | logs.html, ai-study.html |
| #7 카드 애니메이션 | slideUp (logs), fadeIn+translateX (ai-study), translateY (cards) | 전체 |

### CLI 검토 후 수정한 버그 3건

#### 🐛 Bug #1: index.html 카드 다크모드 미적용
- **증상**: 헤더/푸터는 다크모드 적용되나 GRID 카드 내부가 흰색 그대로
- **원인**: Cowork가 헤더/푸터/body는 CSS 변수로 전환했으나 카드 HTML에 Tailwind 하드코딩 색상(`bg-white`, `text-[#111827]`, `bg-[#EBF0FF]` 등) 잔존
- **해결**: 카드 내 하드코딩 색상 전체를 CSS 변수(`var(--bg-primary)`, `var(--text-primary)`, `var(--accent-light)` 등)로 교체

#### 🐛 Bug #2: logs.html:119 — HTML `class` 속성 중복
- **증상**: 섹션 타이틀 하단 구분선(border-b)이 렌더링되지 않음
- **원인**: `<section class="py-12" style="..." class="border-b">` — HTML은 동일 요소에 `class` 속성이 2개 있으면 첫 번째만 파싱
- **해결**: `class="py-12 border-b"` 로 병합, `style="border-color: var(--border);"` 유지

#### 🐛 Bug #3: ai-study.html:117 — 동일한 중복 class 속성
- **증상**: 위와 동일 (border-b 미적용)
- **해결**: Bug #2와 동일한 방식으로 수정

---

## v0.04 — 2026-06-20 | GitHub API 편집 기능 구현 중 발생한 이슈

#### 🔴 [보안] PAT 채팅창 노출
- **증상**: 사용자가 실제 PAT를 채팅에 직접 입력
- **조치**: 즉시 GitHub에서 Revoke 후 재발급
- **재발 방지**: PAT는 반드시 브라우저 ⚙️ UI에서만 입력

#### 🐛 [해결] git push rejected — master_watch.py 충돌
- **증상**: `master_watch.py`가 12초 debounce로 자동 push한 사이 CLI도 push → `fetch first` 오류
- **해결**: `git pull --rebase origin main` → `git push` 순서 표준화

#### 🐛 [해결] 한국어 git commit 메시지 인코딩 오류
- **증상**: PowerShell `@'...'@` heredoc에 한국어 포함 시 `pathspec` 오류
- **해결**: commit 메시지를 ASCII 영어로만 작성

#### 🐛 [해결] `<!-- content -->` 주석이 카드 `<p>` 안에 삽입
- **증상**: ai-study.html 카드 Edit 중 `<!-- content -->` 텍스트가 본문에 삽입
- **원인**: old_string이 실제 파일 내용과 미세하게 달라 잘못된 위치에 삽입
- **해결**: Read로 정확한 내용 확인 후 재Edit

---

## v0.05 — 2026-06-20 | AI Study 미리보기 & Home 동적 로딩 버그

#### 🐛 [해결] AI Study 카드 미리보기 서식 뭉개짐
- **증상**: 트리 구조 텍스트(`├──`, `└──` 등)와 줄바꿈이 모두 공백으로 합쳐져 표시됨
- **원인**: `-webkit-line-clamp` 사용 시 `white-space: normal !important` 적용 → `pre-wrap` 무효화
- **해결**: `max-height: 4.8em` + `mask-image: linear-gradient(to bottom, black 30%, transparent 100%)` 로 교체 → `white-space: pre-wrap` 유지

#### 🐛 [해결] Home 탭 — AI Study 전체 내용이 그대로 노출
- **증상**: Home "Recent AI Study"에 제목·날짜 대신 전체 본문이 표시됨
- **원인**: ai-study.html 카드 제목이 `<a>` → `<p>`로 변경됐으나 index.html의 `loadLatestEntries()`는 `querySelector('a')` 그대로 → `title = ''`, `querySelectorAll('p')[1]`이 날짜 대신 전체 본문 `<p>`를 가리킴 → `meta` 변수에 전체 내용 할당 → 화면에 출력
- **해결**:
  - title: `querySelector('p.font-semibold')`
  - meta: `allPs[allPs.length - 1]` (마지막 p = 날짜·태그)
  - content: `querySelector('.content-preview')`

#### 🐛 [해결] AI Study 상세 모달 — 내용이 잘리고 스크롤 안 됨
- **증상**: 긴 내용 카드 클릭 시 모달이 화면 높이를 초과하면 잘린 채로 스크롤 불가
- **원인**: ai-study.html `.modal-box`에 `max-height` / `overflow-y: auto` 누락 (index.html에는 있었으나 ai-study.html에 미적용)
- **해결**: `#studyDetailModal .modal-box { max-height: 88vh; overflow-y: auto; max-width: 680px; }`

---

## 참고 링크
- 배포 URL: https://barobogi.github.io/Daily_for_Barobogi/
- Stock Dashboard (GitHub Pages): https://barobogi.github.io/stock_dashboard/stock-dashboard.html
- Stock Dashboard (Netlify, 구): https://barobogi-stock-dashboard.netlify.app/stock-dashboard.html
- Stock repo: https://github.com/barobogi/stock_dashboard
