
# Panda.py

from .animal import Animal


class Elephant(Animal):
    def __init__(self, name="Pret"):
        super().__init__(name, species="Panda")

    def sound(self):
        return "toots"

    def action(self):
        return "remembers everything!"
