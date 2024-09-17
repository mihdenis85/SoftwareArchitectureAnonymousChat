from starlette.middleware.cors import CORSMiddleware
import logging
import os
from fastapi import FastAPI

from connections import ConnectionManager
from routes.websocket import router as websocket_router
from routes.count import router as count_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    
    app.include_router(websocket_router)
    app.include_router(count_router)
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
