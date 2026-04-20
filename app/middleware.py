import time
import logging
import uuid
from fastapi import Request

logger = logging.getLogger(__name__)



async def log_requests(request: Request, call_next):
    start_time = time.time()

    request_id = str(uuid.uuid4())

    logger.info(f"request_start id={request_id} path={request.url.path}")

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    duration = time.time() - start_time


    logger.info(
        f"request_end path={request.url.path} status={response.status_code} duration={duration:.4f}s"
    )

    return response
