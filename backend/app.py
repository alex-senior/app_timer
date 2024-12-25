from flet import *
import flet as ft

width=720*1.6
height=405*1.6

class MenuButton(ft.ElevatedButton):
    def __init__(self,icon,text,width, hover_color):
        super().__init__()
        self.icon=icon
        self.text=text
        self.hover_color=hover_color
        self.button = Container(
            Row([
                Icon(
                    self.icon,
                    color='white'
                ),
                Text(
                    self.text,
                    color='white',
                    size=16,
                    weight='w600'
                )
            ]),
            width=width,
            bgcolor='transparent',
            blur=Blur(12,12,BlurTileMode.MIRROR),
            on_hover=self.Hover,
        )
    def Hover(self, e):
        if self.button.bgcolor != self.hover_color:
            self.button.bgcolor=self.hover_color
        else:
            self.button.bgcolor = 'transparent'

    def build(self):
        return self.body

class Sidebar(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.width=300
        self.height=500
        self.bgcolor="#44000000"
        self.menubar = GestureDetector(
            Container(
                Row([
                    Container(
                        width=15,
                        height=15,
                        border_radius=360,
                        bgcolor='red',
                    ),
                    Container(
                        width=15,
                        height=15,
                        border_radius=360,
                        bgcolor='yellow',
                    ),
                    Container(
                        width=15,
                        height=15,
                        border_radius=360,
                        bgcolor='green',
                        blur=Blur(12,12,BlurTileMode.MIRROR),
                    )
                ]),
                height=40,
                width=self.width,
                padding=padding.only(20,10,0,10),
                bgcolor=self.bgcolor
            ),
            on_pan_update=self.update_pos,
        )
        self.body = Container(
            Column([
                self.menubar,
                Container(
                    Text(
                        "Menu",
                        color='#999999',
                        size=14,
                        weight='w500'
                    ),
                    padding=padding.only(20)
                ),
                Container(
                    Column([
                        #MenuButton(icons.DASHBOARD_OUTLINED, "Dashboard", 240, self.bgcolor)
                    ])
                )
            ]),
            width=self.width,
            height=self.height,
            left=50,
            top=50,
            border_radius=6,
            bgcolor=self.bgcolor,
            blur=Blur(12,12,BlurTileMode.MIRROR),
            padding=padding.only(20,10,0,10)
        )

    def update_pos(self, e):
        self.body.top=max(0,self.body.top+e.delta_y)
        self.body.left=max(0,self.body.left+e.delta_x)
        self.body.update()

    def build(self):
        return self.body

body = Container(
    Stack([
        Image(
            src='../assets/0.jpg',
            width=width,
            height=height,
            left=0,
            top=0
        ),
        Sidebar()
    ])
)