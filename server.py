# server.py
import asyncio
import websockets


async def handle_connection(websocket):
    print("Client connected")
    try:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

            # Echo the message back to the client
            response = f"Server received "

            await websocket.send(response + " and from server")
            print(f"Sent: {response} ")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# local laptop iP is : 10.100.0.83

async def main():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8765)

    print("WebSocket server is running on ws://0.0.0.0:8765")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
