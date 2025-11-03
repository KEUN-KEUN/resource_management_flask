# allocation/domain/model.py
from dataclasses import dataclass

@dataclass
class DashboardTest:
    grid_id: str
    today_total_quantity: int
