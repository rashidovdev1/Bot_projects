import asyncpg
import os

async def create_pool():
    return await asyncpg.create_pool(os.environ.get("DATABASE_URL"))

async def create_table(pool):
    await pool.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            user_id BIGINT,
            username TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)

async def save_message(pool, user_id, username, message):
    await pool.execute(
        "INSERT INTO messages (user_id, username, message) VALUES ($1, $2, $3)",
        user_id, username, message
    )
