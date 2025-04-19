from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.gogol.GOGOL_Install import GOGOL_Install
from gdo.payment_credits.GDT_Credits import GDT_Credits
from gdo.ui.GDT_Page import GDT_Page


class module_gogol(GDO_Module):

    def gdo_dependencies(self) -> list:
        return [
            'payment_credits',
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Credits('gogol_credits_bet_min').not_null().initial('1'),
            GDT_Credits('gogol_credits_bet_max').not_null().initial('10'),
            GDT_Credits('gogol_credits_price').not_null().initial('2'),
            GDT_UInt('gogol_played_total').not_null().initial('0'),
            GDT_User('gogol_ai_gol').not_null().initial('1'),
            GDT_User('gogol_ai_easy').not_null().initial('1'),
            GDT_User('gogol_ai_medium').not_null().initial('1'),
            GDT_User('gogol_ai_hard').not_null().initial('1'),
        ]

    def cfg_bet_min(self) -> int:
        return self.get_config_value('gogol_credits_bet_min')

    def cfg_bet_max(self) -> int:
        return self.get_config_value('gogol_credits_bet_max')

    def cfg_price(self) -> int:
        return self.get_config_value('gogol_credits_price')

    def cfg_games_total(self) -> int:
        return self.get_config_value('gogol_played_total')

    def cfg_ai_gol(self) -> GDO_User:
        return self.get_config_value('gogol_ai_gol')

    def cfg_ai_easy(self) -> GDO_User:
        return self.get_config_value('gogol_ai_easy')

    def cfg_ai_medium(self) -> GDO_User:
        return self.get_config_value('gogol_ai_medium')

    def cfg_ai_hard(self) -> GDO_User:
        return self.get_config_value('gogol_ai_hard')

    def gdo_user_config(self) -> list[GDT]:
        return [
            GDT_UInt('gogol_played').not_null().initial('0'),
            GDT_UInt('gogol_won').not_null().initial('0'),
        ]

    def gdo_install(self):
        GOGOL_Install.install()

    def gdo_load_scripts(self, page: 'GDT_Page'):
        pass
