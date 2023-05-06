from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BConnet(MDApp):
  def build(self):
    self.root = BoxLayout(orientation='vertical')

    # Create a BoxLayout for the buttons
    bottom_box = BoxLayout(orientation='vertical', size_hint=(1, None), height=30)

    # Add the buttons to the bottom_box
    bottom_box.add_widget(Button(text='Button 1'))
    bottom_box.add_widget(Button(text='Button 2'))
    # Add the bottom_box to the root BoxLayout
    self.root.add_widget(bottom_box)

    return self.root

if __name__ == "__main__":
  BConnet().run()
    