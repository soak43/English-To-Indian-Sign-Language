from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.lang import Builder
from speechrecogtrial1 import getaudio
from grammarcheck import grammar_check
import time

#Designate the .kv file
#Builder.load_file('my.kv')

class MyLayout(Widget):
	start = time.time()
	def presstext(self):
		#Create variables
		input_text = self.ids.sent_input.text

		output = grammar_check(input_text)
		if(output != input_text):
			self.ids.label1.text = f'The grammatically correct sentence is: {output}.\n Please enter the correct English sentence.'
		else:
			#update label
			self.ids.label1.text = f'{input_text} is converted to ISL'

		#Clear input box
		self.ids.sent_input.text = ""

	def audioinput(self):
		input_text = getaudio()
		self.ids.label1.text = f'{input_text} is converted to ISL'

	end = time.time()
	print("The total time required to run = ", end-start)



class myApp(App):
	def build(self):
		return MyLayout()


if __name__ == '__main__':
	myApp().run()
