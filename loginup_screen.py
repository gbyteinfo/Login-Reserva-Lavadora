from kivy.lang import Builder

from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors.magic_behavior import MagicBehavior


kv = """
<LoginupScreen>
    name: "loginup_screen"
    MDScreen:
        md_bg_color:[27/255,29/255,34/255,1]
        #radius: [30,30,0,0]
        MDCard:
            size_hint: None,None
            size: "320dp","530dp"
            pos_hint:{"center_x":.5,"center_y":.5}
            md_bg_color:[27/255,29/255,34/255,1]
            elevation:5
            padding:10 # usando dp com padrao de fmedida para adequar aos tamanhois da tela
            spacing:10 # usando dp com padrao de medida para adequar aos tamanhois da tela
            radius:[36,36,36,36]
            orientation: 'vertical'
        # Imagem Logo
            FitImage:
                size_hint:None,None
                width:"251dp"
                height:"242dp"
                id:bg_imagem
                source:'resources/images/logoSombra2.png'
                pos_hint:{"center_x":.5}
            Widget:
                size_hint_y:None
                height:"10dp"
            MDTextField:
                hint_text:"Seu Flat"
                icon_right:"account"
                icon_right_color:self.theme_cls.primary_color
                #helper_text:"Exemplo: 1010"
                helper_text_mode:"on_focus"
                pos_hint:{"center_x":.5,"center_y":.5}
                size_hint_x: None
                width: dp(235)
                font_size: dp(16)
                line_color_normal: self.theme_cls.primary_color
                line_color_focus:[85/255,92/255,111/255,1]
                theme_text_color:"Custom"
                #multiline: True
                #mode:"fill"
                #fill_color:[1,1,1,.1]
            Widget:
                size_hint_y:None
                height:"5dp"  

            MDTextField:
                hint_text:"Sua Senha"
                icon_right:"eye-off"
                icon_right_color:self.theme_cls.primary_color
                helper_text:"Exemplo: 1010"
                helper_text_mode:"on_focus"
                pos_hint:{"center_x":.5,"center_y":.5}
                size_hint_x: None
                width: dp(235)
                font_size: dp(16)
                line_color_normal:self.theme_cls.primary_color
                line_color_focus:[85/255,92/255,111/255,1]
                password:True
                #mode:"retangle"
                #fill_color:[1,1,1,.1]
            MDSwitch:
                text:"sdafsdfasdfsadfsdfsdafsadfsdafsd"
                id: switchDados
                pos_hint: {'center_x': .5, 'center_y': .5}
                width: dp(64)
                active:True
            
            MagicButton:
                text:"Efetuar Login"
                size_hint_x: .8
                pos_hint:{"center_x":.5,"center_y":.5}
                #on_release: self.twist()
                #on_release: self.wobble()
                on_release: self.grow()
            Widget:
                size_hint_y:None
                height:"20dp"

"""

class MagicButton(MagicBehavior, MDRaisedButton):
    pass

class LoginupScreen(MDScreen):
    Builder.load_string(kv)