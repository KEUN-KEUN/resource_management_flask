from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class DashboardTest(SQLModel, table=True):
    __tablename__ = "dashboard_test"

    grid_id: str = Field(
        primary_key=True,
        max_length=50,
        description="Grid Identifier",
        sa_column_kwargs={"unique": True, "nullable": False},
    )

    today_total_quantity: int = Field(
        max_length=10,
        description="Today's Total Quantity",
        sa_column_kwargs={"unique": True, "nullable": False},
    )

