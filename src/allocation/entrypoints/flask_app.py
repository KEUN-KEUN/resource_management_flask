from datetime import datetime
from sqlalchemy import create_engine, text
from flask import Flask
from src import config

app = Flask(__name__)
engine = create_engine(config.get_mssql_uri(), echo=True, future=True)

@app.route("/api/health")
def health():
   sql = text("SELECT USER_NAME FROM MESUSER WHERE USER_ID = :uid")  
   with engine.connect() as conn:
        result = conn.execute(sql, {"uid": "ADMIN"})
        row = result.fetchone()
        data = dict(row._mapping) if row else {}
   return {"status": "ok", "user": data}  

if __name__ == "__main__":
    app.run(port=8000, debug=True)