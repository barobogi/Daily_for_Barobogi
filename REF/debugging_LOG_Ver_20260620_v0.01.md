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

---

## 참고 링크
- 배포 URL: https://barobogi.github.io/Daily_for_Barobogi/
- Stock Dashboard (GitHub Pages): https://barobogi.github.io/stock_dashboard/stock-dashboard.html
- Stock Dashboard (Netlify, 구): https://barobogi-stock-dashboard.netlify.app/stock-dashboard.html
- Stock repo: https://github.com/barobogi/stock_dashboard
