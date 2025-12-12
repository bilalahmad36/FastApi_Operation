from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        number = int(data)

        factorial = 1
        for i in range(1,number + 1):
            factorial *= i
            await websocket.send_text(f"Step {i}: {factorial}")

        await websocket.send_text(f"Final Factorial of {number} is {factorial}")