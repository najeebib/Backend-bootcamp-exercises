import logging
from fastapi import Request


class Logger:
    @staticmethod
    def log_request(request: Request):
        logging.info(f"Request received: {request.method} {request.url}")
        return True

