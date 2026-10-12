from .zone import Zone


class RestrictedZone(Zone):
    def __init__(self) -> None:
        super().__init__()
        self._movement_cost = 2
