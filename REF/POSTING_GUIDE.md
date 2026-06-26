# Posting Guide — Diary_for_Barobogi
> 다른 프로젝트 작업 중에도 "AI Study에 올려줘" / "Logs에 올려줘" 라고 하면
> Claude가 이 가이드를 읽고 → 포맷에 맞게 초안 작성 → 사용자 확인 → commit

---

## 워크플로우

```
사용자: "{프로젝트 내용} AI Study에 올려줘"
    ↓
Claude: POSTING_GUIDE.md 읽기 → 해당 탭 포맷으로 초안 작성 → 사용자에게 보여주기
    ↓
사용자: confirm ("그래" / 수정 요청)
    ↓
Claude: 파일 수정 → git commit → git pull --rebase → git push
    ↓
GitHub Pages 자동 배포 (2~3분)
```

---

## 1. AI Study 탭

**파일**: `d:\AI\Diary_for_Barobogi\ai-study.html`
**삽입 위치**: `<div id="studyList">` 바로 아래 첫 번째 카드로 삽입

### data-id 규칙
- 형식: `YYYYMMDD-N`
- 당일 기존 카드 번호 확인 후 다음 번호 사용 (예: 기존에 -1, -2 있으면 -3)

### 카테고리 목록
| 카테고리명 | 용도 |
|-----------|------|
| `AI & Next.js` | LLM, Claude API, Next.js 관련 |
| `Machine Learning` | ML/DL 이론 및 실습 |
| `Prompt Engineering` | 프롬프트 설계, Claude 활용법 |
| `Web Dev` | 웹 개발, GitHub Pages, 정적 사이트 |

> 새 카테고리 추가 시 필터 버튼도 함께 추가 (208번째 줄 근처 `.flex.flex-wrap.gap-2` 블록)

### 카드 HTML 포맷
```html
<div class="post-hover py-6 px-2 -mx-2 rounded-lg study-card"
     data-category="{CATEGORY}"
     data-id="{YYYYMMDD-N}"
     style="border-top: 1px solid var(--border);"
     onclick="openStudyDetailModal(this)">
  <div class="flex justify-between items-center mb-1">
    <span class="text-[10px] font-semibold tracking-wider uppercase" style="color: var(--accent);">{CATEGORY}</span>
    <button class="edit-btn" onclick="event.stopPropagation(); openEditModal(this.closest('.study-card'), event)">✏️ 수정</button>
  </div>
  <p class="text-sm font-semibold mt-1 mb-2" style="color: var(--text-primary);">{TITLE}</p>
  <p class="text-xs leading-relaxed mb-2 content-preview" style="color: var(--text-secondary);">{CONTENT}</p>
  <p class="text-xs" style="color: var(--text-tertiary);">{DATE} · {TAGS}</p>
</div>
```

### 콘텐츠 작성 스타일 (표준 포맷)
```
{제목} — 핵심 정리

한 줄 요약
{한 문장으로 이 학습의 핵심}

🗂️ 전체 구조 / 아키텍처
(트리 구조나 다이어그램으로 전체 그림 먼저)

🔑 핵심 기술 1 — {소제목}
(설명 + 코드 예시)

🔑 핵심 기술 2 — {소제목}
...

⚠️ 주의사항 / 함정
(삽질한 것, 놓치기 쉬운 것)

💡 배운 점 / 교훈
1. ...
2. ...
```

### 🌱 성장 관점 코멘트 (항상 고민할 것)

포스팅 작성 시 아래 질문을 항상 스스로 던질 것:

> "이 기술/학습이 주식 자동화 외에 만복이와의 성장, AI 시스템 발전에 어떻게 연결되는가?"

- 기술적 내용만 정리하지 말고 **"왜 이게 중요한가" + "어디로 확장되는가"** 를 한 단락 이상 포함
- 성장과 직접 관련 없는 주제면 → 생략 가능 (단, 생략 이유를 잠깐 고민할 것)
- 예시 표현:
  - "이 기술을 알면 지금 이런 한계가 뚫린다"
  - "주식 외에 ___에도 바로 적용 가능하다"
  - "다음 단계로 이어지는 연결고리는 ___이다"

**포맷 예시:**
```
🌱 성장 관점
MCP를 이해하면 만복이가 세상을 볼 수 있게 된다.
지금은 파일만 읽지만, MCP 연결 후엔 Firebase · 카카오 API · 트레이딩뷰를
직접 조회할 수 있다 → 어떤 외부 도구든 Claude의 감각기관이 됨.
```

### HTML 이스케이프 규칙
| 원문 | HTML 내 표기 |
|------|-------------|
| `<tag>` | `&lt;tag&gt;` |
| `=>` (JS 화살표) | `=&gt;` |
| `→` (방향 화살표) | 그대로 사용 |
| `"` (따옴표, 속성 밖) | 그대로 사용 |

---

## 2. Logs 탭

**파일**: `d:\AI\Diary_for_Barobogi\logs.html`
**삽입 위치**: `<div class="space-y-4" id="logList">` 바로 아래 첫 번째 카드로 삽입

### data-id 규칙
- 형식: `YYYYMMDD-N` (AI Study와 동일)

### 카드 HTML 포맷
```html
<div class="card-hover border rounded-lg p-4 log-card"
     data-tags="{TAG1},{TAG2}"
     data-id="{YYYYMMDD-N}"
     style="background-color: var(--bg-primary); border-color: var(--border); box-shadow: var(--shadow-sm);">
  <div class="flex justify-between items-center">
    <span class="text-xs" style="color: var(--text-tertiary);">{YYYY.MM.DD}</span>
    <button class="edit-btn" onclick="openEditLogModal(this.closest('.log-card'), event)">✏️ 수정</button>
  </div>
  <h3 class="text-sm font-semibold mt-1 mb-2" style="color: var(--text-primary);">{TITLE}</h3>
  <p class="text-xs leading-relaxed" style="color: var(--text-secondary); white-space: pre-wrap;">{CONTENT}</p>
  <div class="mt-3 flex gap-2 flex-wrap">
    <span class="text-[10px] px-2 py-0.5 rounded font-medium" style="background-color: var(--accent-light); color: var(--accent);">#{TAG1}</span>
    <span class="text-[10px] px-2 py-0.5 rounded font-medium" style="background-color: var(--accent-light); color: var(--accent);">#{TAG2}</span>
  </div>
</div>
```

### 콘텐츠 작성 스타일
- 제목: 오늘 한 일을 한 줄로 (예: "오늘의 학습", "Daily Webpage UI 개선")
- 내용: 번호 목록으로 오늘 한 일 3~5개
- 태그: #프로젝트명 #기술명 형태

---

## 커밋 방법

```powershell
git add {파일명}
git commit -m "{영어로 간단한 메시지}

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git pull --rebase origin main
git push origin main
```

> ⚠️ master_watch.py가 자동 push하는 경우가 있으므로 항상 `pull --rebase` 후 push

---

## 다른 프로젝트에서 사용하는 법

다른 프로젝트 세션에서 작업 중 "Diary에 올려줘" / "AI Study에 올려줘" 라고 하면:

1. Claude가 전역 CLAUDE.md의 POSTING_GUIDE 섹션을 확인
2. `d:\AI\Diary_for_Barobogi\REF\POSTING_GUIDE.md` 읽기
3. 대상 탭 포맷으로 초안 작성 → 사용자 확인
4. confirm 후 Diary_for_Barobogi 프로젝트 파일 직접 수정 → commit
