from gdo.core.GDT_Enum import GDT_Enum


class GDT_AL(GDT_Enum):

    def gdo_choices(self) -> dict:
        return {
            'easy': 'Easy',
            'medium': 'Medium',
            'hard': 'Hard',
        }
