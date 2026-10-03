from fastapi import FastAPI, WebSocket, WebSocketDisconnect
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []  # This line initializes an empty list to keep track of active WebSocket connections.

    async def connect(self, websocket: WebSocket):
        await websocket.accept()  # This line accepts the incoming WebSocket connection.
        self.active_connections.append(websocket)  # This line adds the accepted WebSocket connection to the list of active connections.

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)  # This line removes the disconnected WebSocket connection from the list of active connections.

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)  # This line sends a personal message to a specific WebSocket connection.

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)  # This line sends a broadcast message to all active WebSocket connections.