import time
import logging
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(f"request_start path={request.url.path}")

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        f"request_end path={request.url.path} status={response.status_code} duration={duration:.4f}s"
    )

    return response
