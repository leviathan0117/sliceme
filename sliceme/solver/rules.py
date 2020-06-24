from components import SceneObject
import re


def new(scene, object_type, name):
    if object_type == 'cube':
        cube = SceneObject('cube')
        cube['vertexes'] = re.findall(r'[A-Z][0-9]*]', name)
