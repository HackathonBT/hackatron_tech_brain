import uvicorn
from uvicorn.config import LOGGING_CONFIG
from app.settigs import settings


if __name__ == '__main__':
    LOGGING_CONFIG['formatters']['default']['datefmt'] = '%Y-%m-%d %H:%M:%S'
    LOGGING_CONFIG['formatters']['default']['fmt'] = '(%(asctime)s) %(levelprefix)s %(message)s'
    LOGGING_CONFIG['formatters']['access']['datefmt'] = '%Y-%m-%d %H:%M:%S'
    LOGGING_CONFIG['formatters']['access']['fmt'] = '(%(asctime)s) %(levelprefix)s %(client_addr)s \
                                                      - "%(request_line)s" %(status_code)s'

    uvicorn.run(
        'app.main:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.ENABLE_AUTORELOAD,
        workers=settings.WORKERS
    )
