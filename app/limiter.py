from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

def get_real_ip(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0]
    return request.client.host

# Create the instance here

# Use for testing
# limiter = Limiter(key_func=get_real_ip)
limiter = Limiter(key_func=get_remote_address)
