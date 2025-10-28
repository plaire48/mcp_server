import os, logging
from typing import Dict, Any

# [핵심] .env 파일이 없으므로, 코드 내 기본값을 사용
LOG_LEVEL = os.getenv("JSON_LOG_LEVEL", "INFO").upper() # 기본값 INFO
DEFAULT_PREVIEW_LENGTH = int(os.getenv("DEFAULT_PREVIEW_LENGTH", 100)) # 기본값 100

logger = logging.getLogger(__name__)
try: logger.setLevel(LOG_LEVEL)
except ValueError: logger.setLevel("INFO")

def text_to_json(text: str) -> Dict[str, Any]:
    """입력 텍스트를 요약 정보(JSON)로 변환합니다."""
    text = str(text or "")
    logger.info(f"Converting text (length: {len(text)}) to JSON summary.")
    words = text.replace("\n", " ").split(); lines = text.splitlines()
    preview_length = DEFAULT_PREVIEW_LENGTH
    summary = { "len": len(text), "lines": len(lines), "words": len(words), "preview": text[:preview_length] }
    logger.debug(f"Generated JSON: {summary}")
    return summary

def append_to_json(existing_json: Dict[str, Any], new_data: Dict[str, Any], key_name: str) -> Dict[str, Any]:
    """기존 JSON 객체에 새로운 데이터를 지정된 키로 추가합니다."""
    logger.info(f"Appending data to JSON under key '{key_name}'.")
    if not isinstance(existing_json, dict): result = {}
    else: result = existing_json.copy()
    if not isinstance(new_data, dict): logger.warning("'new_data'가 dict 아님.")
    if not isinstance(key_name, str) or not key_name: logger.error("유효한 'key_name' 필요"); return result
    result[key_name] = new_data
    logger.debug(f"Appended result: {result}")
    return result
