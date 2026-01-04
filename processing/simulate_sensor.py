import requests
import time
import random
import json

API_URL = "http://127.0.0.1:8000/api/crossings/identify/"

def simulate_sensor_data():
    """
    Simulates raw gait signals from an mmWave sensor.
    """
    # Generating some random numbers to mimic signal amplitude/frequency features
    return {
        "amplitude": [random.uniform(0.1, 1.0) for _ in range(50)],
        "frequency": [random.uniform(10, 50) for _ in range(50)],
        "timestamp": time.time()
    }

def main():
    print("Starting mmWave Sensor Simulation...")
    locations = ["Forest Path A", "Checkpoint 1", "Remote Trail B", "River Crossing"]
    
    try:
        while True:
            # Randomly decide when someone crosses (every 5-15 seconds)
            wait_time = random.randint(5, 15)
            print(f"Waiting for next crossing event... (~{wait_time}s)")
            time.sleep(wait_time)
            
            print("Motion detected! Capturing gait data...")
            gait_data = simulate_sensor_data()
            location = random.choice(locations)
            
            payload = {
                "gait_data": gait_data,
                "location": location
            }
            
            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    status = result.get('status')
                    confidence = result.get('confidence', 0)
                    person = result.get('person')
                    
                    if status == "Identified":
                        print(f"✅ PERSON IDENTIFIED: {person['full_name']} at {location}")
                        print(f"   Confidence: {confidence:.2f}")
                    else:
                        print(f"⚠️  UNKNOWN PERSON DETECTED at {location}")
                        print(f"   Confidence: {confidence:.2f}")
                else:
                    print(f"❌ Error sending data: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                print("❌ Backend connection failed. Make sure Django is running.")
                
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
