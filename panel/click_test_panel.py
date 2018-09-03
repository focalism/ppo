from src.panel import Panel
from src.uidefinition import UIDefinition


class ClickPanel(Panel):

    definition = UIDefinition().root('div')\
        .with_descendant('#double_click', 'double')\
        .with_descendant('#single_click','single')\
        .with_descendant('#jump', 'jump')\
        .with_descendant('#jump_new_page', 'jump new')


class LoginPanel(Panel):

    definition = UIDefinition().root('#login')\
        .with_descendant("#name", 'name')\
        .with_descendant("#email", 'email')


class MouseOverPanel(Panel):

    definition = UIDefinition().root('#hover')\
        .with_descendant('#mouse_hover','hover')
