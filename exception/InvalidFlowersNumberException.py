class InvalidFlowersNumberException(Exception):
    def __init__(self, message="Invalid number of flowers"):
        self.message = message
        super().__init__(self.message)