from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from connection_manager import ConnectionManager

app = FastAPI()
manager= ConnectionManager()


# @app.websocket("/ws")
# # This endpoint handles WebSocket connections. 
# # When a client connects to this endpoint, it will accept the connection and enter a loop 
# # where it continuously listens for messages from the client.
# #  Upon receiving a message, it will send back a response that includes the text of the received message.
# async def websocket_endpoint(websocket: WebSocket): #async function handles waiting for messages and sending responses
#     await websocket.accept()  #accpt() handles the initial handshake and establishes the WebSocket connection with the client.await keyword indicates that this function is asynchronous and can be paused and resumed, allowing other tasks to run concurrently.
#     try:
#         while True:
#             data = await websocket.receive_text() #receive_text() waits for a message from the client and returns it
#             await websocket.send_text(f"Message text was: {data}") #send_text() sends a message back to the client, in this case, it sends a response that includes the text of the received message.

#     except WebSocketDisconnect:
#         print("Client disconnected")  # If the client disconnects, it will print a message to the console indicating that the client has disconnected.
#     except Exception as e:
#         print(f"Error: {e}")  # If an error occurs during the WebSocket communication, it will be caught and printed to the console.

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)  # This line calls the connect method of the ConnectionManager instance to accept the WebSocket connection and add it to the list of active connections.
    try:
        while True:
            data = await websocket.receive_text()  # This line waits for a message from the client and returns it as a string.
            await manager.send_personal_message(f"You wrote: {data}", websocket)  # This line sends a personal message back to the client that includes the text of the received message.
            await manager.broadcast(f"Client says: {data}")  # This line broadcasts the received message to all active WebSocket connections.

    except WebSocketDisconnect:
        manager.disconnect(websocket)  # This line calls the disconnect method of the ConnectionManager instance to remove the disconnected WebSocket connection from the list of active connections.
        await manager.broadcast("A client disconnected.")  # This line broadcasts a message to all active WebSocket connections indicating that a client has disconnected.
    except Exception as e:
        print(f"Error: {e}")  # This line catches any other exceptions that may occur during the WebSocket communication and prints the error message to the console.