from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.WithSerialization import WithSerialization
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Serialize import GDT_Serialize, Mode
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created


class GDO_Board(WithSerialization, GDO):
    """
    %7
    """
    PLAYER_KEYS: list[str] = [
        'b_1white',
        'b_2black',
        'b_3white',
        'b_4black',
        'b_5white',
        'b_6black',
        'b_7gol',
    ]

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('b_id'),
            GDT_User('b_2black'),
            GDT_User('b_1white'),
            GDT_User('b_4black'),
            GDT_User('b_3white'),
            GDT_User('b_6black'),
            GDT_User('b_5white'),
            GDT_User('b_7gol'),
            GDT_User('b_winner'),
            GDT_UInt('b_turn').not_null().initial(0),
            GDT_Serialize('b_board').mode(Mode.GDOPACK),
            GDT_Created('b_creator'),
            GDT_Creator('b_created'),
        ]

    def get_player(self, n: int) -> GDO_User:
        return self.gdo_value(self.PLAYER_KEYS[n % 7])

    def get_white(self) -> GDO_User:
        return self.gdo_value('b_white')

    def get_current_player(self) -> GDO_User:
        return self.get_player(self.get_turn())

    def next_turn(self):
        pass

    def join(self, user: GDO_User):
        for key in self.PLAYER_KEYS:
            if not self.gdo_val(key):
                self.set_val(key, user)
