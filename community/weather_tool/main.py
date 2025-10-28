# community/weather_tool/main.py
import os
import logging
import random # 가상 데이터 생성용
from typing import Dict, Any

# [핵심] .env 또는 UI 설정값을 단순 키로 읽어옴 (기본값 설정 포함)
API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_DEFAULT_API_KEY")
API_ENDPOINT = os.getenv("WEATHER_API_ENDPOINT", "https://api.example-weather.com")
DEFAULT_UNITS = os.getenv("DEFAULT_UNITS", "metric") # 'metric' 또는 'imperial'
LOG_LEVEL = os.getenv("WEATHER_LOG_LEVEL", "INFO").upper()

logger = logging.getLogger(__name__)
try:
    logger.setLevel(LOG_LEVEL)
except ValueError:
    logger.setLevel("INFO")
    logger.warning(f"잘못된 WEATHER_LOG_LEVEL 값 '{LOG_LEVEL}'이 감지되어 INFO로 설정됩니다.")

def get_weather(city: str, units: str = None) -> Dict[str, Any]:
    """
    지정된 도시의 현재 날씨 정보를 (가상으로) 가져옵니다.

    Args:
        city: 날씨를 조회할 도시 이름.
        units: 온도를 표시할 단위 ('metric' 또는 'imperial'). 기본값은 설정에 따름.

    Returns:
        날씨 정보가 담긴 JSON 객체. API 키가 없으면 에러 메시지 반환.
    """
    logger.info(f"'{city}' 도시의 현재 날씨 조회 요청 (API Endpoint: {API_ENDPOINT})")
    
    # API 키 확인 (예시)
    if not API_KEY or API_KEY == "YOUR_DEFAULT_API_KEY":
        logger.error("날씨 API 키가 설정되지 않았습니다.")
        return {"error": "날씨 API 키가 .env 또는 UI 설정에서 구성되지 않았습니다."}

    used_units = units if units in ['metric', 'imperial'] else DEFAULT_UNITS
    logger.debug(f"사용 단위: {used_units}")

    # --- 가상 API 호출 시뮬레이션 ---
    # 실제로는 여기서 requests 라이브러리 등을 사용하여 API_ENDPOINT로 요청을 보냅니다.
    # response = requests.get(f"{API_ENDPOINT}/weather", params={"q": city, "appid": API_KEY, "units": used_units})
    # data = response.json()
    # --- 시뮬레이션 끝 ---

    # 가상 응답 데이터 생성
    temperature = random.uniform(5, 25) if used_units == 'metric' else random.uniform(40, 80)
    weather_conditions = ["맑음", "구름 조금", "흐림", "비"]
    
    mock_data = {
        "city": city,
        "temperature": round(temperature, 1),
        "unit": "°C" if used_units == 'metric' else "°F",
        "condition": random.choice(weather_conditions),
        "humidity": random.randint(30, 90),
        "api_key_used": f"{API_KEY[:4]}..." # 실제 키 노출 방지
    }
    logger.info(f"'{city}' 날씨 정보 조회 완료.")
    logger.debug(f"응답 데이터: {mock_data}")
    return mock_data

def get_forecast(city: str, days: int = 3) -> Dict[str, Any]:
    """
    지정된 도시의 향후 몇 일간의 날씨 예보를 (가상으로) 가져옵니다.

    Args:
        city: 예보를 조회할 도시 이름.
        days: 예보 일수 (기본값: 3).

    Returns:
        날씨 예보 정보가 담긴 JSON 객체. API 키가 없으면 에러 메시지 반환.
    """
    logger.info(f"'{city}' 도시의 {days}일 날씨 예보 요청")
    
    if not API_KEY or API_KEY == "YOUR_DEFAULT_API_KEY":
        logger.error("날씨 API 키가 설정되지 않았습니다.")
        return {"error": "날씨 API 키가 .env 또는 UI 설정에서 구성되지 않았습니다."}
        
    # --- 가상 API 호출 시뮬레이션 ---
    # 실제로는 forecast 엔드포인트로 요청
    # response = requests.get(f"{API_ENDPOINT}/forecast", params={"q": city, "appid": API_KEY, "units": DEFAULT_UNITS, "cnt": days})
    # data = response.json()
    # --- 시뮬레이션 끝 ---

    # 가상 예보 데이터 생성
    forecast_list = []
    for i in range(days):
        day_forecast = {
            "day": i + 1,
            "high_temp": round(random.uniform(10, 30), 1),
            "low_temp": round(random.uniform(0, 15), 1),
            "condition": random.choice(["맑음", "흐림 후 갬", "소나기", "바람 강함"])
        }
        forecast_list.append(day_forecast)
        
    mock_forecast = {
        "city": city,
        "forecast_days": days,
        "unit": "°C" if DEFAULT_UNITS == 'metric' else "°F",
        "daily_forecast": forecast_list
    }
    logger.info(f"'{city}' {days}일 예보 조회 완료.")
    logger.debug(f"예보 데이터: {mock_forecast}")
    return mock_forecast
