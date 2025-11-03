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


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, dashboard_test):
        self.session.add(dashboard_test)
    
    def _get(self, grid_id) -> model.DashboardTest:
        return self.session.get(model.DashboardTest, grid_id)
        # 구버전 : return self.session.query(model.Product).filter_by(sku=sku).first()
