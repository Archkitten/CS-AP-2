from util_menu import Menu


class IntroMenu(Menu):
    def __init__(self):
        super().__init__()

    def while_loop(self):
        self.screen.fill('Red')
