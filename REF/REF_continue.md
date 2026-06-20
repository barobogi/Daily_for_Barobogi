# REF_continue — Diary_for_Barobogi
> 마지막 업데이트: 2026-06-20
> 다음 세션 시작 시 이 파일부터 읽을 것

---

## 현재 상태 (1차 완료)

**배포 URL**: https://barobogi.github.io/Daily_for_Barobogi/
**저장소**: https://github.com/barobogi/Daily_for_Barobogi
**브랜치**: main

### 탭 구성
| 탭 | 파일 | 상태 |
|----|------|------|
| Home | `index.html` | ✅ 동적 fetch로 Logs/AI Study 최신 항목 표시 |
| Logs | `logs.html` | ✅ 카드 추가/편집/GitHub 직접 저장 |
| AI Study | `ai-study.html` | ✅ 카드 추가/편집/미리보기/상세 모달/GitHub 직접 저장 |
| Stock | `stock-dashboard.html` | ✅ iframe 연동 (stock_dashboard repo) |
| Stats | `stats.html` | ✅ 통계 대시보드 |
| Goals | `goals.html` | ✅ 목표 추적 |

---

## 핵심 구현 내용

### GitHub API 브라우저 직접 저장
- PAT를 브라우저 localStorage에 저장 (⚙️ 버튼으로 1회 설정)
- GET sha → PUT commit 방식
- 한국어: `TextEncoder` 기반 `encodeUtf8Base64()` 사용 (atob/btoa 한국어 불가)
- 카드 식별: `data-id="YYYYMMDD-N"` + `replaceCardInHtml()` depth 추적 파싱

### AI Study 탭 카드 구조
- 카드 클릭 → `openStudyDetailModal()` 전체 내용 모달 (88vh, 스크롤)
- 미리보기: `max-height: 4.8em` + `mask-image` 페이드아웃 (pre-wrap 서식 유지)
- ✏️ 수정 버튼: hover 시 표시, `event.stopPropagation()` 으로 카드 클릭과 분리
- 카테고리 필터: All / AI & Next.js / Machine Learning / Prompt Engineering / Web Dev

### Home 탭 동적 로딩
- `fetch('./logs.html')` + `DOMParser`로 최신 2개 로그 표시
- `fetch('./ai-study.html')`로 최신 3개 학습 표시 (제목+카테고리+날짜만)
- 선택자: title=`p.font-semibold`, meta=`allPs[last]`, content=`.content-preview`
- edit-btn은 `.edit-btn { display: none !important }` 로 Home에서 숨김

---

## 현재 AI Study 카드 목록 (최신순)
| data-id | 제목 | 카테고리 |
|---------|------|----------|
| 20260620-2 | Barobogi 일상 기록 웹사이트 1차 개선 | Web Dev |
| 20260620-1 | Claude Cowork와 CLI 100% 자동화 적용 | AI & Next.js |
| (기존 3개) | Prompt Engineering, Machine Learning, AI & Next.js | 각각 |

---

## 다음 세션 시 참고

### 콘텐츠 추가 방법
→ `REF/POSTING_GUIDE.md` 참고 (어느 프로젝트에서도 "AI Study에 올려줘" 가능)

### git push 주의
- `master_watch.py`가 12초 debounce로 자동 push → 충돌 가능
- 항상: `git pull --rebase origin main` → `git push origin main`

### PAT 관련
- 브라우저 localStorage에만 저장, 절대 코드/채팅에 포함 금지
- 만료/노출 시 GitHub Settings → Developer settings → Personal access tokens → Revoke

---

## 2차 개선 후보 (미결)
- [ ] Stats / Goals 탭 GitHub API 편집 기능 추가
- [ ] Logs 탭도 카드 클릭 시 상세 모달 (AI Study와 동일하게)
- [ ] 태그 필터 — Logs 탭에도 적용 (현재는 AI Study에만)
- [ ] 새 카드 추가 시 Home 탭 자동 반영 확인 절차 간소화
