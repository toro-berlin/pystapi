#!/usr/bin/env python3

from sys import stderr

from fastapi import FastAPI

try:
    from pydantic_settings import BaseSettings
    from uvicorn.main import run
except ImportError:
    print("install uvicorn and pydantic-settings to use the dev server", file=stderr)
    exit(1)

from stat_fastapi.api import StatApiRouter


class DevSettings(BaseSettings):
    port: int = 8000
    host: str = "127.0.0.1"


app = FastAPI(debug=True)
app.include_router(StatApiRouter().router)


if __name__ == "__main__":
    settings = DevSettings()
    run("stat_fastapi.__dev__:app", reload=True, host=settings.host, port=settings.port)
