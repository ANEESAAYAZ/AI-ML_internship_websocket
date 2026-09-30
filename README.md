# FastAPI WebSocket Chat

A simple beginner-friendly WebSocket chat project built with **FastAPI, Python, HTML, and JavaScript**.

This project demonstrates how a client and server can communicate in real time using WebSockets.

## Features

* FastAPI WebSocket server
* Real-time communication between client and server
* HTML and JavaScript test client
* Client sends messages to the server
* Server receives and sends a response back
* Simple WebSocket connection using `ws://`

## Technologies Used

* Python
* FastAPI
* WebSockets
* HTML
* JavaScript
* Uvicorn

## Project Structure

```text
AI-ML_internship_websocket/
│
├── main.py
├── test.html
├── .gitignore
└── README.md
```

## How It Works

The client establishes a WebSocket connection with the FastAPI server:

```text
Browser
   ↓
WebSocket connection
   ↓
FastAPI Server
   ↓
Receives message
   ↓
Sends response back
   ↓
Browser
```

For example:

```text
Client: Hello

Server: Message text was: Hello
```

## Run the Project

### 1. Activate the virtual environment

```bash
myenv\Scripts\activate
```

### 2. Start the FastAPI server

```bash
uvicorn main:app --reload
```

The server will run at:

```text
http://127.0.0.1:8000
```

### 3. Open the test page

Open `test.html` in your browser.

The JavaScript connects to:

```text
ws://localhost:8000/ws
```

### 4. Send a message

Type a message in the input box and click **Send**.

The message is sent from the browser to the FastAPI WebSocket server, and the server sends a response back to the browser.

## WebSocket Endpoint

```text
ws://localhost:8000/ws
```

The endpoint is defined in `main.py`:

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```

## Learning Purpose

This project was created to understand:

* WebSocket connections
* `async` and `await`
* Client-server communication
* FastAPI WebSocket endpoints
* Sending and receiving messages
* Basic real-time communication

## Future Improvements

* Build a proper chat interface
* Display me
