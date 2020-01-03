from kivy.app import App
from kivymd.theming import ThemeManager
import kivymd.factory_registers
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.uix.boxlayout import BoxLayout

class MyContent(BoxLayout):
    pass

class MainApp(App):
    theme_cls = ThemeManager()
    theme_cls.accent_palette = 'Blue'

    def on_start(self):
        panel = MDExpansionPanel(title="Perfil", icon="índice.png", content=MyContent())
        self.root.ids.panel_container.add_widget(panel)

MainApp().run()