# client.py
import asyncio
import websockets

import cv2
from groq_prompt import logger, capture_images, encode_image



async def communicate():
    uri = "ws://10.100.0.83:8765"  # Replace with your laptop's IP address

    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    await asyncio.sleep(1)

    if not cap1.isOpened() or not cap2.isOpened():
        logger.error("Failed to open one or more cameras.")

    async with websockets.connect(uri) as websocket:
        logger.info("Connected to the server")


        try:
            while True:
                image_path = await capture_images(cap1, cap2)
                base64_image = encode_image(image_path)
                logger.info("encoded image")


                await websocket.send(base64_image)
                logger.info(f"Sent: {response} ")
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")

        # Send a message to the server
        message = "Hello from Glasses"
        await websocket.send(message)
        logger.info(f"Sent: {message}")






async def main():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    if not cap1.isOpened() or not cap2.isOpened():
        logger.error("Failed to open one or more cameras.")
    while True:
        image_path = await capture_images(cap1, cap2)


if __name__ == "__main__":


    asyncio.run(communicate())