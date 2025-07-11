from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app =FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=['*'],
                   allow_headers=['*']
                   )

clients=[]
@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data=await websocket.receive_text()
            print(data)
            for client in clients:
                await client.send_text(data)
    except:
        clients.remove(websocket)