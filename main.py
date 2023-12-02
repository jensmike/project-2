from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Line,Rectangle,Ellipse
from kivy.graphics import Color
from math import sin,cos,tan,exp,log,pi,degrees,radians,acos,asin


def Sin(a):
    return sin(degrees(a))
def Cos(a):
    return cos(degrees(a))
def power(n,nbr):
    puiss=1
    for i in range(0,n):
        puiss=puiss*nbr
    return puiss

def racine(n,nbre):
    return(nbre**(1/n))



class MainInterface(BoxLayout):
    val=0
    List_Button_part31_character=['1','2','3','4','5','6','7','8','9','0','.',',']
    List_Button_part32_character=['Clear','<-','*','/',"+","-","Ans","="]
    List_Button_part21_character=['sqrt','x^2','hex',"bin","exp","ON","log",'sin','sin^-1',"cos","cos^-1","tan","x^n",'Pi','(',")","sqrt","root_n","prev_ans","next_ans"]
    CHARACTER_CHAIN=Button(text='',font_size=19,text_size=(380,None),halign="center",background_color=(0,1,0,0.6),color=(0,1,0,1))
    CHARACTER_CHAIN_RESULT=Button(text='value',background_color=(1,1,0,0.3),color=(0,1,1,1))
   

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.spacing=6
        self.padding="5dp"
        self.orientation="vertical"
        self.but1=Button(text="The calculator By JensMike .inc",background_color=(0.1,0,0,1),color=(0.5,1,0,1))
        self.but2=Button(text="hello")
        self.but3=Button(text="hello")
        self.gridlayout21=GridLayout(spacing=3,cols=6,rows=3)
        self.gridlayout31=GridLayout(spacing=3,cols=3,rows=4)
        self.gridlayout32=GridLayout(spacing=5,cols=2,rows=4)
        self.but5=Button(text="hello")


        

        #self.part1.add_widget(self.but1)
        
        ###############################################################
        # Definition of the structure of the part 1 of the calculator##
        ###############################################################

        self.part1=BoxLayout(size_hint=(1,0.2))
        self.part1.orientation="vertical"

        self.part11=BoxLayout(size_hint=(1,0.2))
        self.part11.add_widget(self.but1)
        
        self.part12=BoxLayout(size_hint=(1,0.4))
        self.part12.add_widget(self.CHARACTER_CHAIN)

        self.part13=BoxLayout(size_hint=(1,0.3))
        self.part13.add_widget(self.CHARACTER_CHAIN_RESULT)

		
        self.part1.add_widget(self.part11)
        self.part1.add_widget(self.part12)
        self.part1.add_widget(self.part13)
        ##############################################################

        ###############################################################
        # Definition of the structure of the part 2 of the calculator##
        ###############################################################
                
        self.part2=BoxLayout(size_hint=(1,0.3))

        for i in range(0,18):
            if i !=5:
                button=Button(text=self.List_Button_part21_character[i],on_press=self.Click_event, size_hint=(0.6,0.3),background_color=(1,0.8,1,0.7),color=(1,1,0,1))
            else:
                button=Button(text=self.List_Button_part21_character[i], size_hint=(0.6,0.3),on_press=self.Click_event,background_color=(1,0.5,0,1),color=(1,0.8,1,1))
            self.gridlayout21.add_widget(button)

    
        self.part2.add_widget(self.gridlayout21)



        ##############################################################
        ###############################################################
        # Definition of the structure of the part 3 of the calculator##
        ###############################################################
        
        self.part3=BoxLayout(size_hint=(1,0.6))
        self.part3.orientation="horizontal"
        self.part3.spacing=6
        self.part31=BoxLayout(size_hint=(0.7,1))
        self.part32=BoxLayout(size_hint=(0.3,1))

        
        for i in range(0,12):
            print(i)
            button=Button(text=self.List_Button_part31_character[i],on_press=self.Click_event, size_hint=(0.25,0.25),background_color=(0,0.8,1,1),color=(1,1,0,1))
            self.gridlayout31.add_widget(button)
        self.part31.add_widget(self.gridlayout31)

        for i in range(0,8):
            if i==0:
                button=Button(text=self.List_Button_part32_character[i],on_press=self.Click_event,size_hint=(0.3,0.3),background_color=(0.6,0.3,0.8,1),color=(1,0.8,1,1))
                self.gridlayout32.add_widget(button)
            else:
                button=Button(text=self.List_Button_part32_character[i],on_press=self.Click_event,size_hint=(0.3,0.3),background_color=(1,1,0,1),color=(1,0.8,1,1))
                self.gridlayout32.add_widget(button)

        self.part32.add_widget(self.gridlayout32)

        self.part3.add_widget(self.part31)
        self.part3.add_widget(self.part32)
        ##############################################################
        self.add_widget(self.part1)
        self.add_widget(self.part2)
        self.add_widget(self.part3)
        
    def Click_event(self,inf):
        
        if inf.text=="=":
            self.calcultation()
        elif inf.text=="<-":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text[:-1]
        elif inf.text=="ON":
            self.CHARACTER_CHAIN.text=""
        elif inf.text=="x^2":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"power(2,"
        elif inf.text=="root_n":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"racine("

        elif inf.text=="sqrt":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"racine(2,"

        elif inf.text=="log":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"log("
        
        elif inf.text=="exp":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"exp("

        elif inf.text=="bin":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"bin("
        elif inf.text=="hex":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"hex("
        elif inf.text=="Ans":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"Ans"
        elif inf.text=="x^n":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"power("
        elif inf.text=="Pi":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"pi"
        elif inf.text=="cos^-1":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"acos("
        elif inf.text=="sin^-1":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"asin("
        elif inf.text=="sin":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"sin("
        elif inf.text=="cos":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"cos("
        elif inf.text=="tan":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+"tan("
        elif inf.text=="Clear":
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text=""
            self.CHARACTER_CHAIN_RESULT.text=""
        else:
            self.CHARACTER_CHAIN.text=self.CHARACTER_CHAIN.text+inf.text
        
       # self.update_screen()

    def update_screen(self):
        self.Label.text=self.CHARACTER_CHAIN
        
    def calcultation(self):
        try:
            Ans=self.val
            self.val=eval(self.CHARACTER_CHAIN.text)
        except:
            self.CHARACTER_CHAIN_RESULT.text="error"
        else:
            self.CHARACTER_CHAIN_RESULT.text=str(self.val)


class CalculatorApp(App):
    def __init__(self):
        super().__init__()
    def build(self):
        return MainInterface()

CalculatorApp().run()