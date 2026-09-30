from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
# This endpoint handles WebSocket connections. 
# When a client connects to this endpoint, it will accept the connection and enter a loop 
# where it continuously listens for messages from the client.
#  Upon receiving a message, it will send back a response that includes the text of the received message.
async def websocket_endpoint(websocket: WebSocket): #async function handles waiting for messages and sending responses
    await websocket.accept()  #accpt() handles the initial handshake and establishes the WebSocket connection with the client.await keyword indicates that this function is asynchronous and can be paused and resumed, allowing other tasks to run concurrently.
    while True:
        data = await websocket.receive_text() #receive_text() waits for a message from the client and returns it
        await websocket.send_text(f"Message text was: {data}") #send_text() sends a message back to the client, in this case, it sends a response that includes the text of the received message.