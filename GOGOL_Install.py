from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_UserType import GDT_UserType


class GOGOL_Install:

    @classmethod
    def install(cls):
        cls.install_player('gol')
        cls.install_player('easy')
        cls.install_player('medium')
        cls.install_player('hard')

    @classmethod
    def install_player(cls, difficulty: str):
        from gdo.gogol.module_gogol import module_gogol
        conditions = {
            "user_name": f"gogol_{difficulty}",
            "user_displayname": f"GoGoL {difficulty}",
            "user_type": GDT_UserType.BOT,
            "user_server": "2",
        }
        if not GDO_User.table().get_by_vals(conditions):
            ai = GDO_User.blank(conditions).insert()
            module_gogol.instance().save_config_val(f"gogol_ai_{difficulty}", ai.get_id())
