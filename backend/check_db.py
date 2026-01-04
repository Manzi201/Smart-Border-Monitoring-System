import os
import django
from django.conf import settings
from django.db import connection
from dotenv import load_dotenv

def check_connection():
    load_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()
    
    db_name = settings.DATABASES['default']['NAME']
    db_engine = settings.DATABASES['default']['ENGINE']
    
    print(f"--- Database Configuration ---")
    print(f"Engine: {db_engine}")
    print(f"Name/Host: {db_name}")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"\n✅ SUCCESS: Connected to Database!")
            print(f"Version: {version[0]}")
            
            if "PostgreSQL" in version[0]:
                print("--- TARGET: Supabase Cloud (Postgres) ---")
            else:
                print("--- TARGET: Local SQLite ---")
    except Exception as e:
        print(f"\n[ERROR] Could not connect to the database.")
        print(f"Error: {e}")

if __name__ == "__main__":
    check_connection()
