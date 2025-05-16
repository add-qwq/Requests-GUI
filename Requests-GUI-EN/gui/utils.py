# 工具函数（如 JSON 格式化）
def format_json(text):
    try:
        import json
        obj = json.loads(text)
        return json.dumps(obj, indent=2, ensure_ascii=False)
    except:
        return text