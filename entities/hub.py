from __future__ import annotations
from .zones.zone import Zone


class Hub:
    def __init__(
            self,
            name: str,
            x_axis: int,
            y_axis: int,
            color: int,
            max_drones: int,
            zone_type: Zone | None = None,
            connections: list[Hub] | None = None
    ) -> None:

        self._name = name
        self._x_axis = x_axis
        self._y_axis = y_axis
        self._color = color
        self._max_drones = max_drones

        if zone_type is not None:
            self._zone_type = zone_type
        else:
            self._zone_type = Zone()

        if connections is not None:
            self._connections = connections
        else:
            self._connections = []

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_zone_type(self) -> Zone:
        return self._zone_type

    def set_zone_type(self, zone_type: Zone) -> None:
        self._zone_type = zone_type

    def get_x_axis(self) -> int:
        return self._x_axis

    def set_x_axis(self, x_axis: int) -> None:
        self._x_axis = x_axis

    def get_y_axis(self) -> int:
        return self._y_axis

    def set_y_axis(self, y_axis: int) -> None:
        self._y_axis = y_axis

    def get_color(self) -> int:
        return self._color

    def set_color(self, color: int) -> None:
        self._color = color

    def get_max_drones(self) -> int:
        return self._max_drones

    def set_max_drones(self, max_drones: int) -> None:
        self._max_drones = max_drones

    def get_connections(self) -> list[Hub]:
        return self._connections

    def add_connection(self, hub: Hub) -> None:
        self._connections.append(hub)
