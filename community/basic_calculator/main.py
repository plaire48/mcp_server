# main.py
import os
import logging

# [핵심] 라이브러리 제작자는 '단순한 키'만 사용합니다.
# 충돌 방지는 server_launcher.py가 임시 환경 변수를 주입하여 해결합니다.
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper() 
PRECISION = int(os.getenv("NUMBER_PRECISION", 4))

# 로거도 단순하게 __name__ (이 모듈의 경로) 사용
logger = logging.getLogger(__name__)
# 로거 레벨 설정
try:
    logger.setLevel(LOG_LEVEL)
except ValueError:
    logger.setLevel("INFO")
    logger.warning(f"잘못된 LOG_LEVEL 값: {LOG_LEVEL}. INFO로 설정됩니다.")

def add(a: float, b: float) -> float:
    """두 숫자를 더합니다."""
    logger.info(f"Adding (precision: {PRECISION})")
    return round(a + b, PRECISION)

def multiply(a: float, b: float) -> float:
    """두 숫자를 곱합니다."""
    logger.info(f"Multiplying (precision: {PRECISION})")
    return round(a * b, PRECISION)
