# Smart Border Crossing Monitoring System

## Overview

This project implements a smart border monitoring system that detects and identifies people crossing a border by analyzing their gait patterns using mmWave radar sensors.

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** React, Vite, Tailwind CSS (or Vanilla CSS as per instructions, but I'll stick to Vanilla/Premium CSS for now)
- **Database:** Supabase (PostgreSQL, Auth, Storage)
- **Sensing:** Python-based gait processing (simulated or real mmWave data)

## Features

- **Geospatial Command Center:** Real-time map with sensor pings for detected crossings.
- **mmWave Signal Visualization:** Live charting of gait signal patterns.
- **Intrusion Detection Alerts:** Instant visual and notification alerts for unknown individuals.
- **Person Registration:** Capture gait data and personal details (Full name, National ID, etc.).
- **Data Analytics:** 24h stats breakdown by location and identity status.

## Setup & Execution

### 1. Backend Setup

```powershell
cd backend
python -m venv venv
.\venv\Scripts\pip install -r requirements.txt
.\venv\Scripts\python manage.py migrate
.\venv\Scripts\python manage.py runserver
```

### 2. Run Simulation

In a separate terminal:

```powershell
cd processing
..\backend\venv\Scripts\python simulate_sensor.py
```

### 3. Open Dashboard

Open `index.html` in your browser.
