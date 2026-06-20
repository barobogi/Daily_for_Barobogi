import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

DAUM_ID    = os.environ.get("DAUM_ID", "")
DAUM_PW    = os.environ.get("DAUM_PW", "")
FROM_EMAIL = f"{DAUM_ID}@daum.net" if DAUM_ID else ""
TO_EMAIL   = "barobogi79@gmail.com"
SMTP_HOST  = "smtp.daum.net"
SMTP_PORT  = 465

SUBJECT = "[Barobogi] Daily_for_Barobogi 3차 개선 고려안"

BODY = """안녕하세요! 오늘 Daily_for_Barobogi 3차 개선 작업 예정일입니다. 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 3차 개선 후보 항목
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 📱 모바일 햄버거 메뉴
   - 작은 화면에서 nav 접기/펼치기
   - 난이도: 낮음

2. 🔍 SEO 최적화
   - meta 태그, og:image, sitemap.xml
   - 난이도: 낮음

3. 📤 소셜 공유 버튼
   - Twitter/X, 카카오 공유
   - 난이도: 중간

4. 💬 댓글 기능 (GitHub Discussions)
   - giscus 라이브러리 연동
   - 난이도: 높음

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 참고
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

사이트: https://barobogi.github.io/Daily_for_Barobogi/
저장소: https://github.com/barobogi/Daily_for_Barobogi
가이드: D:\\AI\\Diary_for_Barobogi\\REF\\POSTING_GUIDE.md

좋은 하루 되세요!
"""


def send_mail():
    if not DAUM_ID or not DAUM_PW:
        print("❌ DAUM_ID / DAUM_PW 환경변수가 설정되지 않았습니다.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"]    = FROM_EMAIL
    msg["To"]      = TO_EMAIL
    msg.attach(MIMEText(BODY, "plain", "utf-8"))

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
            s.login(FROM_EMAIL, DAUM_PW)
            s.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())
        print(f"✅ 메일 발송 완료 → {TO_EMAIL}")
        return True
    except Exception as e:
        print(f"❌ 메일 발송 실패: {e}")
        return False


if __name__ == "__main__":
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] 리마인더 메일 발송 시작")
    send_mail()
