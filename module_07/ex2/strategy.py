from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            trans_creature = cast(TransformCapability, creature)
            protocol = [trans_creature.transform()]
            protocol.append(creature.attack())
            protocol.append(trans_creature.revert())
            return protocol

        raise InvalidStrategyError(creature.name, "aggressive")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            heal_creature = cast(HealCapability, creature)
            protocol = [creature.attack()]
            protocol.append(heal_creature.heal())
            return protocol

        raise InvalidStrategyError(creature.name, "defensive")
