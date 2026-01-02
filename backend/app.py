from fastapi import FastAPI, UploadFile, File
from typing import List
import time
import cv2
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app= FastAPI(title="Real-Time Traffic Analyzer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/images",StaticFiles(directory="traffic_dataset"),name="images")
DATASET_DIR = "traffic_dataset"
dataset_files= sorted(os.listdir(DATASET_DIR))
dataset_size=len(dataset_files)
current_index=0

@app.get("/")
def root():
    return {
        "status": "Backend Running",
        "message": "Traffic Analyzer API is live"
    }
    
@app.get("/analyze-traffic")
def analyze_traffic():
    start_time=time.time()
    
    batch= get_next_batch(batch_size=4)
    road_results = []

    for i, image_path in enumerate(batch):
        density = compute_density(image_path)
        level = classify_traffic(density)
        green_time = green_time_for_level(level)

        road_results.append({
            "road_id": f"Road {chr(65 + i)}",
            "image_url": f"http://127.0.0.1:8000/images/{os.path.basename(image_path)}",
            "density_score": density,
            "traffic_level": level,
            "green_time_sec": green_time
        })
    end_time=time.time()
    processing_time_ms= round((end_time-start_time)*1000,2)
    return {
        "processing_time_ms":processing_time_ms,
        "roads": road_results
    }
        

def compute_density(image_path: str) -> float:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")
    #convert to grayscale
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #edge detection
    edges=cv2.Canny(gray,100,200)
    #density score = number of edge pixels
    density = np.sum(edges>0)
    return float(density)


def classify_traffic(density: float) -> str:
    if density > 250000:
        return "High"
    elif density > 150000:
        return "Medium"
    elif density > 50000:
        return "Low"
    else:
        return "Very Low"
    
def green_time_for_level(level: str) -> int:
    if level == "High":
        return 40
    elif level == "Medium":
        return 25
    elif level == "Low":
        return 15
    else:
        return 10

import random

def get_next_batch(batch_size=4):
    global current_index
    offset=random.randint(0,batch_size-1)
    batch=[]
    for i in range(batch_size):
        idx= (current_index + offset+i)%dataset_size
        image_path= os.path.join(DATASET_DIR, dataset_files[idx])
        batch.append(image_path)
    #Move the pointer forward
    current_index= (current_index+batch_size)%dataset_size
    return batch

