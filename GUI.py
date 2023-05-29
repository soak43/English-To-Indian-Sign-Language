# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:10:34 2022

@author: Sayali
"""

#import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
#from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from speechrecogtrial1 import getaudio
from grammarcheck import grammar_check
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

Builder.load_file("my.kv")

class MyLayout(Widget):
    pass

class English_to_IndianSignLanguage(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        
        
        #Adding margins
        #botton margin = 40% and top&bottom margins = 30%
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
        #add widgets to window
        
        #Label Widget
        self.statement = Label(
            text = "Enter an English sentence",
            font_size = 25,
            color = "#00FFCE"
            )
        self.window.add_widget(self.statement)
        
        
        
        #Collect user input
        self.input = TextInput(
            multiline = True,
            padding_y = (20,20),
            size_hint = (1, 0.5)
            )
        self.window.add_widget(self.input)
        
        #Button Widget
        self.button = Button(
            text = "Convert to Indian Sign Language",
            size_hint = (1,0.5),
            bold = True,
            background_color = "#00FFCE"
            #background_normal = ""
            )
        #callback funtion attach to button
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        
        self.button1 = Button(
            text = "Give Audio Input",
            size_hint = (1,0.5),
            bold = True,
            background_color = "#00FFCE"
            #background_normal = ""
            )
        
        self.button1.bind(on_press = self.call)
        self.window.add_widget(self.button1)
        
        
        return self.window

    def callback(self, instance):
        grammar_check(self.input.text)
        self.statement.text = self.input.text + " converted to ISL" 
        
    def call(self,instance):
        getaudio()
        self.statement.text = "Recording audio from the microphone"

'''       
def show_popup():   
    show = P()
    
    popupWindow = Popup(title = "Help", content = show, size_hint=(None,None),size=(400,400))
    popupWindow.open()
'''        
        
if __name__ == "__main__":
    English_to_IndianSignLanguage().run()