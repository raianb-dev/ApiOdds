import datetime
from fastapi import Response
import json

def parser(content = None):
    
    data = {}
    data["message"] = "Performace procedure success"
    data["time"] = f"{datetime.datetime.now()}"
    data["content"] = content
    data["footer"] = "Api/v1 sports football"
    
    return Response(
        json.dumps(data), status_code=200, media_type="aplication/json"
    )
    