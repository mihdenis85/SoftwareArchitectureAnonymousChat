import asyncio
from typing import List
from fastapi import WebSocket
import logging


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.total_messages: int = 0
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self.lock:
            self.active_connections.append(websocket)
        logging.info(f"New connection: {websocket.client}")

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self.lock:
            self.active_connections.remove(websocket)
        logging.info(f"Disconnected: {websocket.client}")

    async def broadcast(self, message: str) -> None:
        async with self.lock:
            self.total_messages += 1
            logging.info(f"Total messages: {self.total_messages}")
            connections = list(self.active_connections)
        for connection in connections:
            try:
                await connection.send_text(message)
            except WebSocketDisconnect:
                await self.disconnect(connection)
                logging.warning(f"WebSocket disconnected: {connection.client}")
            except Exception as e:
                logging.error(f"Error sending message to {connection.client}: {e}")
