from gdo.core.GDT_UInt import GDT_UInt
from gdo.form.GDT_Form import GDT_Form
from gdo.gogol.GDO_Board import GDO_Board
from gdo.gogol.GDT_AL import GDT_AL
from gdo.gogol.GDT_BoardSize import GDT_BoardSize
from gdo.gogol.MethodGoGoL import MethodGoGoL
from gdo.payment_credits.GDT_Credits import GDT_Credits


class init(MethodGoGoL):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'gogol.init'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'ggi'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_UInt('num_players').min(2).max(6).not_null().initial('2'))
        form.add_field(GDT_BoardSize('size').not_null().initial('small'))
        form.add_field(GDT_Credits('bet').min(self.mod().cfg_bet_min()).max(self.mod().cfg_bet_max()).not_null())
        form.add_field(GDT_AL('ai').positional())
        super().gdo_create_form(form)

    async def form_submitted(self):
        game = GDO_Board.blank({

        }).insert()
        await game.join(self._env_user)
        return self.msg('msg_gogol_inited', (game.get_id(),))
