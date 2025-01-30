class MechanicalError(Exception):
    """
    Custom exception for mechanical failures or constraints in the spaceship.
    """
    def __init__(self, message: str = "A mechanical error occurred."):
        self.message = message
        super().__init__(self.message)