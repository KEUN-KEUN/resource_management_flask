import abc
from allocation.domain import model

class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    def add(self, dashboard_test: model.DashboardTest):
        self._add(dashboard_test)
        self.seen.add(dashboard_test)

    def get(self, grid_id) -> model.DashboardTest:
        dashboard_test = self._get(grid_id)
        if dashboard_test:
            self.seen.add(dashboard_test)
        return dashboard_test

    def _add(self, dashboard_test: model.DashboardTest):
        raise NotImplementedError
    
    def _get(self, grid_id) -> model.DashboardTest:
        raise NotImplementedError
    