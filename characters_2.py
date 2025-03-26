# Character class
class Character:
    # Base class for all characters
    def __init__(
            self,
            name: str,
            image_file: str,
            alive: bool = True,
            affection: int = 0,
            nutrition: int = 2,
            seen: bool = False,
            friend: bool = False
    ):

        self.name = name
        self.image_file = image_file
        self.alive = alive
        self.affection = affection
        self.nutrition = nutrition
        self.seen = seen
        self.friend = friend

    pass
