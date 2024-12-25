from flet import *
import flet

body = Container(
    Container(
        Stack([
            Container(
                border_radius=11,
                rotate=Rotate(0.98*3.14), #degree
                width=360,
                height=560,
                bgcolor='#22ffffff'
            ),
            Container(
                Container(
                    Column([
                        Container(
                            Image(
                                src='../assets/logo.png',
                                width=60,
                            ),
                            padding=padding.only(150,20)
                        ),
                        Text(
                            "Sign in",
                            size=30,
                            width=360,
                            weight='w900',
                            text_align='center'
                        ),
                        Text(
                            "Please login to use the platform",
                            width=360,
                            text_align='center'
                        ),
                        Container(
                            TextField(
                                width=280,
                                height=40,
                                hint_text='Username',
                                border='underline',
                                color='#303030',
                                prefix_icon=icons.EMAIL
                            ),padding=padding.only(40,20),
                        ),
                        Container(
                            TextField(
                                width=280,
                                height=40,
                                hint_text='Password',
                                border='underline',
                                color='#303030',
                                prefix_icon=icons.LOCK
                            ),padding=padding.only(40,10),
                        ),
                        Container(
                            TextButton(
                                "I forgot my password!"
                            ), padding=padding.only(40)
                        ),
                        Container(
                            ElevatedButton(
                                content=Text(
                                    "SIGN IN",
                                    color='white',
                                    weight='w500'
                                ), width=280, bgcolor='black'
                            ), padding=padding.only(40,10)
                        ),
                        Container(
                            Row([
                                Text(
                                    "Don't have an account?"
                                ),
                                TextButton(
                                    "Create a free account."
                                )
                            ], spacing=0), padding=padding.only(40)
                        )
                    ])
                ),
                width=360,
                height=560,
                bgcolor='#22ffffff',
                border_radius=11,
            )
        ]),
        padding=110,
        width=360,
        height=560,
    ),
    width=580,
    height=740,
    gradient=LinearGradient(['#333399','#ff00cc']),
),

def main(page: Page):
    page.window_max_width=580
    page.window_max_height=740
    page.padding=0
    #page.window_frameless=True
    page.add(body)

app(target=main)