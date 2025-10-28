# main.py
import os
import logging
from typing import Dict, Any

# 이 라이브러리만의 설정을 .env에서 읽어옴 (예시)
LOG_LEVEL = os.getenv("JSON_LOG_LEVEL", "INFO").upper()
DEFAULT_PREVIEW_LENGTH = int(os.getenv("DEFAULT_PREVIEW_LENGTH", 120))

logger = logging.getLogger(__name__)
try:
    logger.setLevel(LOG_LEVEL)
except ValueError:
    logger.setLevel("INFO")
    logger.warning(f"잘못된 JSON_LOG_LEVEL 값 '{LOG_LEVEL}'이 감지되어 INFO로 설정됩니다.")

def text_to_json(text: str) -> Dict[str, Any]:
    """입력 텍스트를 요약 정보(JSON)로 변환합니다."""
    text = str(text or "")
    logger.info(f"Converting text (length: {len(text)}) to JSON summary.")
    words = text.replace("\n", " ").split()
    lines = text.splitlines()
    preview_length = DEFAULT_PREVIEW_LENGTH
    
    summary = {
        "original_length": len(text),
        "num_lines": len(lines),
        "num_words": len(words),
        "preview": text[:preview_length],
    }
    logger.debug(f"Generated JSON summary: {summary}")
    return summary

def append_to_json(existing_json: Dict[str, Any], new_data: Dict[str, Any], key_name: str) -> Dict[str, Any]:
    """기존 JSON 객체에 새로운 데이터를 지정된 키로 추가합니다."""
    logger.info(f"Appending data to JSON under key '{key_name}'.")
    if not isinstance(existing_json, dict):
        logger.warning("'existing_json'이 딕셔너리가 아닙니다. 빈 딕셔너리로 시작합니다.")
        result = {}
    else:
        result = existing_json.copy() # 원본 수정을 피하기 위해 복사
        
    if not isinstance(new_data, dict):
         logger.warning("'new_data'가 딕셔너리가 아닙니다.")
         
    if not isinstance(key_name, str) or not key_name:
         logger.error("유효한 문자열 'key_name'이 필요합니다.")
         # 오류 처리 또는 기본 키 사용 등 가능
         return result # 또는 오류 반환

    result[key_name] = new_data
    logger.debug(f"Appended data result: {result}")
    return result
