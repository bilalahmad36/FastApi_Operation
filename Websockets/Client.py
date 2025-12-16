import asyncio
import websockets

async def factorial_client():
    uri = "ws://localhost:8000/ws"
    print("Connecting to server...\n")

    async with websockets.connect(uri) as websocket:

        while True:
            print("Connected! Type a number or type 'exit' to quit.\n")
            user_input = input("Enter a number: ")

            # Send exit command
            if user_input.lower() == "exit":
                await websocket.send("exit")
                print("Closing connection...")
                break

            # Send number to server
            await websocket.send(user_input)
            print(f"Sent: {user_input}\n--- Streaming Response ---")

            # Receive streamed messages
            try:
                while True:
                    msg = await websocket.recv()
                    print(msg)

                    if msg.startswith("Final Factorial"):
                        print("--- Done ---\n")
                        break

            except websockets.ConnectionClosed:
                print("Server closed the connection.")
                break

asyncio.run(factorial_client())
