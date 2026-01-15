
# Panda.py

from .animal import Animal


class Panda(Animal):
    def __init__(self, name="Pret"):
        super().__init__(name, species="panda")

    def sound(self):
        return "yum yum"

    def action(self):
        return "eats lots of bamboo!"
