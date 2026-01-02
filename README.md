🚦 Real-Time Traffic Signal Management System

A full-stack intelligent traffic management system that dynamically assigns traffic signals based on image-derived traffic density using computer vision.

The system simulates a real-world traffic intersection where the most congested road is given priority (green signal), while others are stopped (red signal).

⸻

📌 Project Overview

Traditional traffic signals operate on static timers, which often leads to unnecessary congestion.
This project demonstrates a real-time, data-driven traffic control system using CCTV images and computer vision.

Key Idea

The road with the highest traffic density receives a GREEN signal, while all other roads receive RED signals.

⸻

🧠 Features
	•	📷 Image-based traffic density analysis (OpenCV)
	•	🚦 Dynamic green/red signal assignment
	•	🔄 Auto-refresh every fixed interval
	•	⏱ Countdown timer for next update
	•	📊 Backend & frontend latency display
	•	🖥 Interactive dashboard with real traffic images
	•	🔁 Randomized dataset simulation for realism

  Frontend (React + Tailwind)
        |
        |  REST API (GET)
        v
Backend (FastAPI + OpenCV)
        |
        v
Traffic Image Dataset (TrafficCAM)

🧰 Tech Stack

Backend
	•	Python
	•	FastAPI
	•	OpenCV
	•	NumPy
	•	Uvicorn

Frontend
	•	React (Vite)
	•	Tailwind CSS
	•	JavaScript (ES6)

⸻

📂 Dataset
	•	TrafficCAM Dataset
	•	Real-world CCTV traffic images
	•	Offline randomization performed once to ensure diversity
	•	Images served statically from backend

⸻

🚦 Traffic Signal Logic

At each update cycle:
	•	🟢 GREEN SIGNAL → Road with highest traffic density
	•	🔴 RED SIGNAL → All other roads

Reminder: This logic is deterministic, interpretable, and mirrors real-world priority-based traffic control.

How to Run the Project

 Backend Setup
 cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
Backend runs at:
http://127.0.0.1:8000

Frontend Setup
cd frontend
npm install
npm run dev
Frontend runs at:
http://localhost:5173

📊 Dashboard Highlights
	•	Road-wise traffic images
	•	Traffic level (Low / Medium / High)
	•	Signal indicator:
	•	🟢🟢🟢 → Green Signal
	•	🔴 → Red Signal
	•	Countdown timer for next update
	•	Latency metrics for performance insight

⸻

🧪 Testing & Validation
	•	Multiple refresh cycles tested
	•	Randomized frames ensure non-repetitive behavior
	•	Signal decisions visually validated against traffic images
	•	Stable performance observed across cycles

⸻

📄 Documentation

A detailed project report is included, covering:
	•	Problem definition
	•	Architecture
	•	Dataset
	•	Algorithm
	•	Module-wise requirement satisfaction
	•	Performance evaluation

