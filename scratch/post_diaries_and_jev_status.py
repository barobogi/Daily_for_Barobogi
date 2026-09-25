# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, r"D:\AI\43_function_dev\01_realtime_3ai")
from realtime_engine import Realtime3AIEngine

engine = Realtime3AIEngine()
content = """[안티->만복,코니,바로보기님] 밀린 다이어리(9/23, 9/24) 안티 분량 작성 완료 및 JEV 1단계 구현 대기 상태 보고

■ 1. 밀린 일일 다이어리 작성 완료:
   - 20260923_3AI_일일다이어리.md (안티 소회: PLAUD 오염 방지 및 3-Tier 워치독 반영 작성 완료)
   - 20260924_3AI_일일다이어리.md (안티 소회: JEV 5판 정직 반영 및 pobbagi_db.json 3대 헌법 규정 이식 작성 완료)

■ 2. 뽀개기 4건 진행 상황:
   - pobbagi_db.json 4개 항목에 operational_scenario, proof_of_execution, post_management_plan 3개 필드 규격 추가 후 1차 파일 대조 검증 준비 완료 (코니/만복 1차 검토 대기)

■ 3. JEV 1단계 구현 제어 지침 준수:
   - 바로보기님의 실시간 채팅 'JEV 1단계 승인' 메시지가 올 때까지 코드 작성 착수 철저히 보류
   - 승인 후에도 realtime_engine 수정 전 만복이 형 사전 검증 및 백업 수립 절차를 철저히 이행할 예정입니다."""

metadata = {
    "proof_of_execution": {
        "target_type": "file",
        "receipt": {
            "filepath": r"D:\AI\AI_hub\shared\diaries\20260924_3AI_일일다이어리.md"
        }
    }
}

msg_id = engine.send_message(sender="anti", recipient="all", content=content, metadata=metadata)
print(f"Posted real-time chat message: {msg_id}")
