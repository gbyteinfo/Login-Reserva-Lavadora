from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from loginup_screen import LoginupScreen

class AutoStop(MDApp):
    def build(self):
        sm = ScreenManager()
        return sm

    def on_start(self):
        ss = LoginupScreen()
        self.root.add_widget(ss)
        self.root.current = "loginup_screen"
AutoStop().run()