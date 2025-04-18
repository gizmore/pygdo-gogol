from gdo.base.Util import Strings
from gdo.core.GDT_Enum import GDT_Enum


class GDT_BoardSize(GDT_Enum):

    def gdo_choices(self) -> dict:
        return {
            'sm': 'Small: 8x3',
            'm': 'Medium: 10x4',
            'l': 'Large: 12x5',
        }

    def get_size(self) -> tuple[str,...]:
        v = self.get_val()
        v = Strings.substr_from(v, ': ')
        return tuple(v.split('x', 1))

    def get_width(self):
        return self.get_size()[0]

    def get_height(self):
        return self.get_size()[1]
