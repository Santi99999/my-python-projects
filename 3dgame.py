from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
random.seed(0)
window.size = (600,600)
Entity.default_shader = lit_with_shadows_shader
player = FirstPersonController()
Sky()
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super() __init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'grass'
            color = color rgb(255,255,255)
            highlight_color = color lime
            )
def input(key):
    if key == 'escape':
        quit()

app.run()
