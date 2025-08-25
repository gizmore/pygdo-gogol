from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_Serialize import GDT_Serialize, SerializeMode as Mode
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Timestamp import GDT_Timestamp


class GDO_Board(GDO):
    """
    %7
    """
    PLAYER_KEYS: list[str] = [
        'b_1white',
        'b_2black',
        'b_3white',
        'b_4black',
        'b_5gol',
    ]

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('b_id'),
            GDT_Enum('b_player_count').choices({'2': '2', '4': '4'}),
            GDT_User('b_2black'),
            GDT_User('b_1white'),
            GDT_User('b_4black'),
            GDT_User('b_3white'),
            GDT_User('b_5gol'),
            GDT_User('b_winner'),
            GDT_UInt('b_turn').not_null().initial(0),
            GDT_Serialize('b_board').mode(Mode.GDOPACK),
            GDT_Timestamp('b_finished'),
            GDT_Created('b_creator'),
            GDT_Creator('b_created'),
        ]

    def get_player(self, n: int) -> GDO_User:
        return self.gdo_value(self.PLAYER_KEYS[(n % 5) + 1])

    def get_current_player(self) -> GDO_User:
        return self.get_player(self.get_turn())

    def next_turn(self):
        self.increment('b_turn')
        if self.get_current_player() == self.get_player(5):
            self.gol_turn()

    async def join(self, user: GDO_User):
        for key in self.PLAYER_KEYS:
            if not self.gdo_val(key):
                self.set_val(key, user)

    def is_full(self) -> bool:
        return self.get_num_players() == 5

