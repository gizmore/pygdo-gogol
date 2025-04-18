from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Serialize import GDT_Serialize, Mode
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created


class GDO_Board(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('b_id'),
            GDT_User('b_white').not_null(),
            GDT_User('b_black').not_null(),
            GDT_User('b_winner'),
            GDT_UInt('b_turn').not_null().initial(0),
            GDT_Serialize('b_board').mode(Mode.GDOPACK),
            GDT_Created('b_creator'),
            GDT_Creator('b_created'),
        ]

    def join(self, user: GDO_User):
        pass
