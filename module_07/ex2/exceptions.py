class InvalidStrategyError(Exception):
    def __init__(self, creature: str, strategy: str) -> None:
        message = (
            f"Invalid Creature '{creature}' "
            f"for this {strategy} strategy"
        )
        super().__init__(message)
