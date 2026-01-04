from supabase import create_client, Client
from django.conf import settings

def get_supabase() -> Client:
    """Returns a Supabase client instance."""
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_KEY
    if not url or not key:
        raise ValueError("SUPABASE_URL or SUPABASE_KEY not set in Django settings.")
    return create_client(url, key)
