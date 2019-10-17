from typing import List, Dict, Optional

from models.car import Car


class ParkingLot:

    def __init__(self, spot_names: List[str]):
        # self.spots = dict()
        # for n in spot_names:
        #     self.spots[n] = None

        self.spots: Dict[str, Optional[Car]] = {
            n: None
            for n in spot_names
        }

    @staticmethod
    def create(spots_per_level: int, levels: int) -> "ParkingLot":
        names = []
        level_names = ['A', 'B', 'C', 'D', 'E', 'G']
        for ln in level_names[:levels]:
            for n in range(1, spots_per_level+1):
                names.append(f'{ln}{n}')

        return ParkingLot(names)

    def park(self, car: Car):
        for k, v in self.spots.items():
            if v is None:
                self.spots[k] = car
                break

    def __iter__(self):
        for i in self.spots.items():
            yield i










