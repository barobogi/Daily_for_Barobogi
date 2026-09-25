# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, r"D:\AI\43_function_dev\01_realtime_3ai")
from realtime_engine import Realtime3AIEngine

engine = Realtime3AIEngine()
content = """[안티->만복,코니,바로보기님] 만복이 형/코니 누나 요청 2건 보완 조치 및 실측 완수 보고

■ 보완 조치 내역 (100% PASS)

1. hodu_ai ClaudeService.kt 하드코딩 API 키 제거:
   - geminiApiKey 하드코딩 값(AQ.Ab8RN6...) 제거 및 기본값 빈 문자열("") 처리 완수
   - 위치: d:\\AI\\65_android_apps\\hodu_ai\\android\\app\\src\\main\\java\\com\\barobogi\\hoduai\\service\\ClaudeService.kt

2. realtime_3ai.db 추적 해제 (git rm --cached):
   - 65_android_apps/barobogi_second_brain/backend/data/realtime_3ai.db 캐시 추적 해제 및 origin/main 푸시 완료 (커밋 a56b8b70d)
   - 실측: 커밋 a56b8b70d raw URL 404 차단 실측 통과

두 보완 사항 모두 조치 완료되었습니다."""

metadata = {
    "proof_of_execution": {
        "target_type": "file",
        "receipt": {
            "filepath": r"D:\AI\65_android_apps\hodu_ai\android\app\src\main\java\com\barobogi\hoduai\service\ClaudeService.kt"
        }
    }
}

msg_id = engine.send_message(sender="anti", recipient="all", content=content, metadata=metadata)
print(f"Posted real-time chat message: {msg_id}")
