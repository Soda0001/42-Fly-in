class Zone:
    def __init__(self) -> None:
        self._movement_cost = 1

    def get_movement_cost(self) -> int:
        return self._movement_cost

    def is_blocked(self) -> bool:
        return False
