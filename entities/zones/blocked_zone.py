from .zone import Zone


class BlockedZone(Zone):
    def is_blocked(self) -> bool:
        return True
