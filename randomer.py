import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

in_r1 = 0
in_r2 = 0

class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)

        r1 = Label(text = 'ОТ')
        self.in_r1 = TextInput()
        r2 = Label(text = 'ДО')
        self.in_r2 = TextInput()
        
        self.btn = Button(text = 'Сгенерировать', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5})
        self.btn.on_press = self.next

        self.res = Label(text = '')

        line1 = BoxLayout(size_hint = (0.8, None), height='40sp')
        outer = BoxLayout(orientation='vertical', padding = 8, spacing = 60)

        line1.add_widget(r1)
        line1.add_widget(self.in_r1)
        line1.add_widget(r2)
        line1.add_widget(self.in_r2)

        outer.add_widget(line1)
        outer.add_widget(self.btn)
        outer.add_widget(self.res)

        self.add_widget(outer)

    def next(self):
        global in_r1, in_r2

        in_r1 = int(self.in_r1.text)
        in_r2 = int(self.in_r2.text)

        result = str(random.randint(in_r1, in_r2))

        self.res.text = result        

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        return sm

app = MyApp()
app.run() 