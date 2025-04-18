from gdo.form.GDT_Form import GDT_Form
from gdo.gogol.GDT_AL import GDT_AL
from gdo.gogol.GDT_BoardSize import GDT_BoardSize
from gdo.gogol.MethodGoGoL import MethodGoGoL


class init(MethodGoGoL):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_BoardSize('size').not_null())
        form.add_field(GDT_AL('size').positional())
        super().gdo_create_form(form)

    def form_submitted(self):

