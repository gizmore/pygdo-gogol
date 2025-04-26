from gdo.base.GDT import GDT
from gdo.core.GDT_Object import GDT_Object
from gdo.form.GDT_Form import GDT_Form
from gdo.gogol.GDO_Board import GDO_Board
from gdo.gogol.MethodGoGoL import MethodGoGoL


class join(MethodGoGoL):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'gogol.join'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'ggj'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Object('id').table(GDO_Board.table()).not_null(),
        )
        super().gdo_create_form(form)

    def get_board(self) -> GDO_Board:
        return self.param_value('id')

    def form_submitted(self):
        board = self.get_board()
        board.join(self._env_user)
        if board.is_full():
            board.start()
        else:
            return self.msg('msg_gogol_joined')
