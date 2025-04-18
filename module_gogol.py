from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt


class module_gogol(GDO_Module):

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_UInt('gogol_played_total').not_null().initial('0'),
        ]

    def gdo_user_config(self) -> list[GDT]:
        return [
            GDT_UInt('gogol_played').not_null().initial('0'),
        ]
