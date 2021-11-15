
from __future__ import annotations
from abc import ABC, abstractmethod



class IStrategy(ABC):
    @abstractmethod
    def do_algorithm(self, data,last_game, constant=None) -> str:
        pass