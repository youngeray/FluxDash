import uvicorn
# from uvicorn.workers import UvicornWorker

from server import app, AppConfig  # noqa: F401


if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=AppConfig.app_host,
        port=AppConfig.app_port,
        # workers=AppConfig.app_workers,
        reload=AppConfig.app_reload,
    )
# UvicornWorker
