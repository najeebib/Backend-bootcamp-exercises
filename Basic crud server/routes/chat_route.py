from fastapi import APIRouter, WebSocket,WebSocketDisconnect, Depends
from modules.profanity_filter import ProfanityFilter
from models.message import Message
from modules.logger import Logger

router = APIRouter()
websocket_clients = []
@router.websocket("/ws")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received from WebSocket: {data}")
    except WebSocketDisconnect:
        websocket_clients.remove(websocket)
    except Exception as e:
        print(e)
    return

@router.post("/send_message")
async def send_message(message: Message, log = Depends(Logger.log_request)):
    if len(message.text) < 50:
        msg = message.text.capitalize()
        filter = ProfanityFilter()
        msg = filter.censor(msg)
        # Broadcast the received message to all connected WebSocket clients
        for client in websocket_clients:
            await client.send_text(f"Message received from POST request: {msg}")
        return {"message": f"Broadcast message to all WebSocket clients: {msg}"}
    else:
        return {"message": f"Message is too long"}



