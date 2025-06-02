import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("SUPABASE_HOST"),
        dbname=os.getenv("SUPABASE_DB"),
        user=os.getenv("SUPABASE_USER"),
        password=os.getenv("SUPABASE_PASS"),
        port=5432
    )

    cursor = conn.cursor()
    cursor.execute("SET search_path TO financeiro;")
    conn.commit()

    print("Conexão bem-sucedida com o banco de dados Supabase e schema definido!")

    cursor.close()
    conn.close()

except Exception as e:
    print("Falha ao conectar no banco de dados.")
    print(f"Erro: {e}")
