from slowapi import Limiter
from fastapi import Request

def get_real_ip(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0]
    return request.client.host

# Create the instance here
limiter = Limiter(key_func=get_real_ip)
