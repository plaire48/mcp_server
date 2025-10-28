import os
from typing import Dict, Any

from fastmcp import FastMCP


mcp = FastMCP(name=os.getenv("MCP_NAME", "json Server"))

@mcp.tool()
def text_to_json(text: str) -> Dict[str, Any]:
    """입력 텍스트를 요약 정보(JSON)로 변환합니다."""
    text = str(text or "")
    words = text.replace("\n", " ").split()
    lines = text.splitlines()
    return {
        "original": text,
        "num_lines": len(lines),
        "num_words": len(words),
        "preview": text[:120],
    }

@mcp.tool()
def append_to_json(existing_json: Dict[str, Any], new_data: Dict[str, Any], key_name: str) -> Dict[str, Any]:
    """기존 JSON에 새로운 데이터를 추가합니다."""
    import json
    
    # 기존 JSON을 복사
    result = existing_json.copy()
    
    # 새로운 데이터를 지정된 키로 추가
    result[key_name] = new_data
    
    return result


if __name__ == "__main__":
    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_PORT", "1009"))
    path = os.getenv("MCP_PATH", "/")
    mcp.run(transport="streamable-http", host=host, port=port, path=path)
