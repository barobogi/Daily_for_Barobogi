# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, r"D:\AI\43_function_dev\01_realtime_3ai")
from realtime_engine import Realtime3AIEngine

engine = Realtime3AIEngine()
content = """[안티->전체] 코니 누나 지적 1건(Task Scheduler 절대 경로 및 실행 결과 0 검증) 완수 보고

■ 보완 및 실측 검증 결과 (100% PASS)
1. 경로 수정 및 재등록 완료:
   - 실행 대상 명령어를 'C:\\hb\\python.exe D:\\AI\\Daily_for_Barobogi\\sync_snapshot_to_github.py' 절대 경로로 수정 재등록 완료

2. schtasks 실측 execution 결과 확인 (마지막 결과 = 0):
   - 마지막 실행 시간: 2026-09-25 오전 9:45:00
   - 마지막 결과: 0 (기존 ERROR_FILE_NOT_FOUND -2147024894 해결 및 성공 확인)
   - 다음 실행 예정: 2026-09-25 오전 9:46:00
   - 증거 파일 schtasks_query_poe.txt 갱신 푸시 완료

지적해주신 경로 오류와 마지막 결과 필드 미실측을 정직하게 수용하고 성공(0) 상태를 100% 실측 완료하였습니다."""

metadata = {
    "proof_of_execution": {
        "target_type": "file",
        "receipt": {
            "filepath": r"D:\AI\Daily_for_Barobogi\schtasks_query_poe.txt",
            "sha256": "9a128ded503992573b4bbd54ef51d9d3efe4baadfa25c12b30603efe0d0f2e41"
        }
    }
}

msg_id = engine.send_message(sender="anti", recipient="all", content=content, metadata=metadata)
print(f"Posted real-time chat message: {msg_id}")
