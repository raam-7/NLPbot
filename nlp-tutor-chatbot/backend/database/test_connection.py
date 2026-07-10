from sqlalchemy import text

from database.session import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))

        print("\n✅ Connected Successfully!\n")

        print(result.fetchone()[0])

except Exception as e:
    print("\n❌ Database Connection Failed!\n")
    print(e)