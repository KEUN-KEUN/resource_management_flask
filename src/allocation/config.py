import os

def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"


# MSSQL 커넥션 설정
def get_mssql_uri():
    host = os.environ.get("MSSQL_HOST", "10.40.0.111")
    port = os.environ.get("MSSQL_PORT", 1433)
    user = os.environ.get("MSSQL_USER", "sadev")
    password = os.environ.get("MSSQL_PASSWORD", "sadev1003")
    db_name = os.environ.get("MSSQL_DB", "mes_vn_sh")

    # pyodbc 드라이버 기반 연결 문자열
    # (Windows: ODBC Driver 17 for SQL Server, Linux: ODBC Driver 18 for SQL Server)
    return (
        f"mssql+pyodbc://{user}:{password}@{host},{port}/{db_name}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )