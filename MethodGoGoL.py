from gdo.form.MethodForm import MethodForm
from gdo.gogol.module_gogol import module_gogol


class MethodGoGoL(MethodForm):

   def mod(self) -> module_gogol:
        return module_gogol.instance()
