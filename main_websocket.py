from fastapi import FastAPI, WebSocket, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import threading
import shutil
import os
import cv2
from send_data_websocket import sendData
from setSequence import setSequence
from getTimings import getTimings

app = FastAPI()

# Allow frontend access (CORS for local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

@app.get("/", response_class=HTMLResponse)
async def get():
    with open("index_websocket.html", "r") as f:
        return f.read()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except:
        clients.remove(websocket)

# Broadcast signal updates to all clients
async def send_signal_to_clients(signal):
    for client in clients:
        try:
            await client.send_json(signal)
        except:
            # Remove client if connection is broken
            clients.remove(client)

# Processing video feeds
def run_send_data(cycle_time, video_paths):
    cap1 = cv2.VideoCapture(video_paths[0])
    cap2 = cv2.VideoCapture(video_paths[1])
    cap3 = cv2.VideoCapture(video_paths[2])
    cap4 = cv2.VideoCapture(video_paths[3])

    # Get initial timings to start the sequence
    initial_timings = getTimings(cycle_time, cap1, cap2, cap3, cap4, 0)
    if initial_timings is None:
        print("Error: Could not get initial timings from videos")
        return
        
    sequence_green_time = setSequence(initial_timings)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sendData(sequence_green_time, send_signal_to_clients, cycle_time, cap1, cap2, cap3, cap4))
    
    # Close video captures when done
    cap1.release()
    cap2.release()
    cap3.release()
    cap4.release()

import time

@app.post("/start")
async def start(
    cycle_time: int = Form(...),
    video1: UploadFile = Form(...),
    video2: UploadFile = Form(...),
    video3: UploadFile = Form(...),
    video4: UploadFile = Form(...)
):
    os.makedirs("temp_videos", exist_ok=True)

    video_paths = []
    for i, video in enumerate([video1, video2, video3, video4]):
        path = f"temp_videos/video{i}.mp4"
        with open(path, "wb") as f:
            shutil.copyfileobj(video.file, f)
        video_paths.append(path)

    # Start the processing thread
    thread = threading.Thread(target=run_send_data, args=(cycle_time, video_paths))
    thread.daemon = True  # Make thread daemon so it closes when main program exits
    thread.start()

    # Optional: Wait for a brief moment to make sure processing begins
    time.sleep(1)

    return {"message": "Started processing"}