import numpy as np

from matplotlib import colormaps
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

list_ds9colors=['ds9_grey','ds9_red','ds9_green','ds9_blue','ds9_a','ds9_b','ds9_bb','ds9_he','ds9_i8','ds9_aips',
                'ds9_heat','ds9_cool','ds9_rainbow','ds9_staircase','ds9_standard','ds9_color','ds9_sls','ds9_hsv']

def is_cmap_registered(name_of_cmap):
    """
    This function checks if a color map is already registered in the colormaps of python
    name_of_cmap: str
        Name of the DS9 colormap
    """
    list_of_python_cmaps=list(colormaps)
    if name_of_cmap in list_of_python_cmaps:
        
        return(True)
    else:
        return(False)
    
def list_registered_colormaps():
    """
    This function prints the list of ds9 colormaps that have been already registered
    """
    list_of_python_cmaps=list(colormaps)
    list_of_ds9_registered=[]
    for ds9_cmap in list_ds9colors:
        if is_cmap_registered(ds9_cmap):
            list_of_ds9_registered.append(ds9_cmap)

    print('List of registered DS9 colormaps: ')
    if len(list_of_ds9_registered)==0:
        print('No DS9 color map has been registered.')
    else:
        for ds9_cmap in list_of_ds9_registered:
            print(ds9_cmap+' - '+ds9_cmap+'_r')

    return()

def register_grey():
    ds9_name='ds9_grey'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_grey_cdict = {
    'red':   [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]}
        ds9_grey_cmap = LinearSegmentedColormap(ds9_name, ds9_grey_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_grey_cmap)
        ds9_grey_r_cmap = ds9_grey_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_grey_r_cmap)
    return()

def register_red():
    ds9_name='ds9_red'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_red_cdict = {
    'red':   [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
    'blue':  [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)]}
        ds9_red_cmap = LinearSegmentedColormap(ds9_name, ds9_red_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_red_cmap)
        ds9_red_r_cmap = ds9_red_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_red_r_cmap)   

    return()

def register_green():
    ds9_name='ds9_green'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_green_cdict = {
    'red':   [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
    'green': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)]}
        ds9_green_cmap = LinearSegmentedColormap(ds9_name, ds9_green_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_green_cmap)
        ds9_green_r_cmap = ds9_green_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_green_r_cmap)

    return()

def register_blue():
    ds9_name='ds9_blue'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_blue_cdict = {
    'red':   [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
    'green': [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
    'blue':  [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]}
        ds9_blue_cmap = LinearSegmentedColormap(ds9_name, ds9_blue_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_blue_cmap)
        ds9_blue_r_cmap = ds9_blue_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_blue_r_cmap)
    return()

def register_a():
    ds9_name='ds9_a'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_a_cdict = {
    'red':   [(0.0, 0.0, 0.0), (.25, 0.0, 0.0), (.5, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (.25, 1.0, 1.0), (.5, 0.0, 0.0), (.77, 0.0, 0.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (.125, 0.0, 0.0), (.5, 1.0, 1.0), (.64, .5, .5), (.77, 0.0, 0.0), (1.0, 0.0, 0.0)]}
        ds9_a_cmap = LinearSegmentedColormap(ds9_name, ds9_a_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_a_cmap)
        ds9_a_r_cmap = ds9_a_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_a_r_cmap)
    return()

def register_b():
    ds9_name='ds9_b'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_b_cdict = {
    'red':   [(0.0, 0.0, 0.0), (.25, 0.0, 0.0), (.5, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (.5, 0.0, 0.0), (.75, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (.25, 1.0, 1.0), (.5, 0.0, 0.0), (.75, 0.0, 0.0), (1.0, 1.0, 1.0)]}
        ds9_b_cmap = LinearSegmentedColormap(ds9_name, ds9_b_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_b_cmap)
        ds9_b_r_cmap = ds9_b_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_b_r_cmap)
    return()

def register_bb():
    ds9_name='ds9_bb'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_bb_cdict = {
    'red':   [(0.0, 0.0, 0.0), (.5, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (.25, 0.0, 0.0), (.75, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (.5, 0.0, 0.0), (1.0, 1.0, 1.0)]}
        ds9_bb_cmap = LinearSegmentedColormap(ds9_name, ds9_bb_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_bb_cmap)
        ds9_bb_r_cmap = ds9_bb_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_bb_r_cmap)
    return()

def register_he():
    ds9_name='ds9_he'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_he_cdict = {
    'red':   [(0.0, 0.0, 0.0), (.015, .5, .5), (.25, .5, .5), (.5, .75, .75), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (.065, 0.0, 0.0), (.125, .5, .5), (.25, .75, .75), (.5, .81, .81), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (.015, .125, .125), (.03, .375, .375), (.065, .625, .625), (.25, .25, .25), (1.0, 1.0, 1.0)]}
        ds9_he_cmap = LinearSegmentedColormap(ds9_name, ds9_he_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_he_cmap)
        ds9_he_r_cmap = ds9_he_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_he_r_cmap)
    return()

def register_i8():
    ds9_name='ds9_i8'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_i8_colors = [
    (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), 
    (0.0, 1.0, 1.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0), 
    (1.0, 0.0, 1.0), (1.0, 1.0, 1.0)]
        ds9_i8_cmap = ListedColormap(ds9_i8_colors,name=ds9_name)
        colormaps.register(name=ds9_name, cmap=ds9_i8_cmap)
        ds9_i8_r_cmap = ds9_i8_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_i8_r_cmap)
    return()

def register_aips():
    ds9_name='ds9_aips'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_aips_colors = [
    (.196, .196, .196), (.475, 0.0, .608), (0.0, 0.0, .785),
    (.373, .655, .925), (0.0, .596, 0.0), (0.0, .965, 0.0),
    (1.0, 1.0, 0.0), (1.0, .694, 0.0), (1.0, 0.0, 0.0)]
        ds9_aips_cmap = ListedColormap(ds9_aips_colors,name=ds9_name)
        colormaps.register(name=ds9_name, cmap=ds9_aips_cmap)
        ds9_aips_r_cmap = ds9_aips_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_aips_r_cmap)
    return()

def register_heat():
    ds9_name='ds9_heat'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_heat_cdict = {
    'red':   [(0.0, 0.0, 0.0), (.34, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (.65, 0.0, 0.0), (.98, 1.0, 1.0), (1.0, 1.0, 1.0)]}
        ds9_heat_cmap = LinearSegmentedColormap(ds9_name, ds9_heat_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_heat_cmap)
        ds9_heat_r_cmap = ds9_heat_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_heat_r_cmap)
    return()

def register_cool():
    ds9_name='ds9_cool'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_cool_cdict = {
    'red':   [(0.0, 0.0, 0.0), (.29, 0.0, 0.0), (.76, .1, .1), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (.22, 0.0, 0.0), (.96, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'blue':  [(0.0, 0.0, 0.0), (.53, 1.0, 1.0), (1.0, 1.0, 1.0)]}
        ds9_cool_cmap = LinearSegmentedColormap(ds9_name, ds9_cool_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_cool_cmap)
        ds9_cool_r_cmap = ds9_cool_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_cool_r_cmap)
    return()

def register_rainbow():
    ds9_name='ds9_rainbow'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_rainbow_cdict = {
    'red':   [(0.0, 1.0, 1.0), (.2, 0.0, 0.0), (.6, 0.0, 0.0), (.8, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'green': [(0.0, 0.0, 0.0), (.2, 0.0, 0.0), (.4, 1.0, 1.0), (.8, 1.0, 1.0), (1.0, 0.0, 0.0)],
    'blue':  [(0.0, 1.0, 1.0), (.4, 1.0, 1.0), (.6, 0.0, 0.0), (1.0, 0.0, 0.0)]}
        ds9_rainbow_cmap = LinearSegmentedColormap(ds9_name, ds9_rainbow_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_rainbow_cmap)
        ds9_rainbow_r_cmap = ds9_rainbow_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_rainbow_r_cmap)
    return()

def register_staircase():
    ds9_name='ds9_staircase'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_staircase_colors = [
    (i * .3, i * .3, i * 1) for i in np.linspace(0.2, 1, 5)
] + [
    (i * .3, i * 1, i * .3) for i in np.linspace(0.2, 1, 5)
] + [
    (i * 1, i * .3, i * .3) for i in np.linspace(0.2, 1, 5)
]
        ds9_staircase_cmap = ListedColormap(ds9_staircase_colors,name=ds9_name)
        colormaps.register(name=ds9_name, cmap=ds9_staircase_cmap)
        ds9_staircase_r_cmap = ds9_staircase_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_staircase_r_cmap)
    return()

def register_standard():
    ds9_name='ds9_standard'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_standard_cdict = {
    'red': [
        (0.0, 0.0, 0.0),
        (0.333, 0.3, 0.3),
        (0.333, 0.0, 0.0),
        (0.666, 0.3, 0.3),
        (0.666, 0.3, 0.3),
        (1.0, 1.0, 1.0)
    ],
    'green': [
        (0.0, 0.0, 0.0),
        (0.333, 0.3, 0.3),
        (0.333, 0.3, 0.3),
        (0.666, 1.0, 1.0),
        (0.666, 0.0, 0.0),
        (1.0, 0.3, 0.3)
    ],
    'blue': [
        (0.0, 0.0, 0.0),
        (0.333, 1.0, 1.0),
        (0.333, 0.0, 0.0),
        (0.666, 0.3, 0.3),
        (0.666, 0.0, 0.0),
        (1.0, 0.3, 0.3)
    ]}
        ds9_standard_cmap = LinearSegmentedColormap(ds9_name, ds9_standard_cdict)
        colormaps.register(name=ds9_name, cmap=ds9_standard_cmap)
        ds9_standard_r_cmap = ds9_standard_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_standard_r_cmap)
    return()

def register_color():
    ds9_name='ds9_color'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_color_colors = [
    (0.0, 0.0, 0.0), (0.18431, 0.18431, 0.18431), (0.37255, 0.37255, 0.37255),
    (0.56078, 0.56078, 0.56078), (0.74902, 0.74902, 0.74902), (0.93725, 0.93725, 0.93725),
    (0.0, 0.18431, 0.93725), (0.0, 0.37255, 0.74902), (0.0, 0.49804, 0.49804),
    (0.0, 0.74902, 0.30980), (0.0, 0.93725, 0.0), (0.30980, 0.62353, 0.0),
    (0.49804, 0.49804, 0.0), (0.62353, 0.30980, 0.0), (0.93725, 0.0, 0.0),
    (0.74902, 0.0, 0.30980)
]
        ds9_color_cmap = ListedColormap(ds9_color_colors,name=ds9_name)
        colormaps.register(name=ds9_name, cmap=ds9_color_cmap)
        ds9_color_r_cmap = ds9_color_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_color_r_cmap)
    return()

def register_sls():
    ds9_name='ds9_sls'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_sls_colors = [
    (0.000000, 0.000000, 0.000000),
    (0.043442, 0.000000, 0.052883),
    (0.086883, 0.000000, 0.105767),
    (0.130325, 0.000000, 0.158650),
    (0.173767, 0.000000, 0.211533),
    (0.217208, 0.000000, 0.264417),
    (0.260650, 0.000000, 0.317300),
    (0.304092, 0.000000, 0.370183),
    (0.347533, 0.000000, 0.423067),
    (0.390975, 0.000000, 0.475950),
    (0.434417, 0.000000, 0.528833),
    (0.477858, 0.000000, 0.581717),
    (0.521300, 0.000000, 0.634600),
    (0.506742, 0.000000, 0.640217),
    (0.492183, 0.000000, 0.645833),
    (0.477625, 0.000000, 0.651450),
    (0.463067, 0.000000, 0.657067),
    (0.448508, 0.000000, 0.662683),
    (0.433950, 0.000000, 0.668300),
    (0.419392, 0.000000, 0.673917),
    (0.404833, 0.000000, 0.679533),
    (0.390275, 0.000000, 0.685150),
    (0.375717, 0.000000, 0.690767),
    (0.361158, 0.000000, 0.696383),
    (0.346600, 0.000000, 0.702000),
    (0.317717, 0.000000, 0.712192),
    (0.288833, 0.000000, 0.722383),
    (0.259950, 0.000000, 0.732575),
    (0.231067, 0.000000, 0.742767),
    (0.202183, 0.000000, 0.752958),
    (0.173300, 0.000000, 0.763150),
    (0.144417, 0.000000, 0.773342),
    (0.115533, 0.000000, 0.783533),
    (0.086650, 0.000000, 0.793725),
    (0.057767, 0.000000, 0.803917),
    (0.028883, 0.000000, 0.814108),
    (0.000000, 0.000000, 0.824300),
    (0.000000, 0.019817, 0.838942),
    (0.000000, 0.039633, 0.853583),
    (0.000000, 0.059450, 0.868225),
    (0.000000, 0.079267, 0.882867),
    (0.000000, 0.099083, 0.897508),
    (0.000000, 0.118900, 0.912150),
    (0.000000, 0.138717, 0.926792),
    (0.000000, 0.158533, 0.941433),
    (0.000000, 0.178350, 0.956075),
    (0.000000, 0.198167, 0.970717),
    (0.000000, 0.217983, 0.985358),
    (0.000000, 0.237800, 1.000000),
    (0.000000, 0.268533, 1.000000),
    (0.000000, 0.299267, 1.000000),
    (0.000000, 0.330000, 1.000000),
    (0.000000, 0.360733, 1.000000),
    (0.000000, 0.391467, 1.000000),
    (0.000000, 0.422200, 1.000000),
    (0.000000, 0.452933, 1.000000),
    (0.000000, 0.483667, 1.000000),
    (0.000000, 0.514400, 1.000000),
    (0.000000, 0.545133, 1.000000),
    (0.000000, 0.575867, 1.000000),
    (0.000000, 0.606600, 1.000000),
    (0.000000, 0.631733, 0.975300),
    (0.000000, 0.656867, 0.950600),
    (0.000000, 0.682000, 0.925900),
    (0.000000, 0.707133, 0.901200),
    (0.000000, 0.732267, 0.876500),
    (0.000000, 0.757400, 0.851800),
    (0.000000, 0.782533, 0.827100),
    (0.000000, 0.807667, 0.802400),
    (0.000000, 0.832800, 0.777700),
    (0.000000, 0.857933, 0.753000),
    (0.000000, 0.883067, 0.728300),
    (0.000000, 0.908200, 0.703600),
    (0.000000, 0.901908, 0.676675),
    (0.000000, 0.895617, 0.649750),
    (0.000000, 0.889325, 0.622825),
    (0.000000, 0.883033, 0.595900),
    (0.000000, 0.876742, 0.568975),
    (0.000000, 0.870450, 0.542050),
    (0.000000, 0.864158, 0.515125),
    (0.000000, 0.857867, 0.488200),
    (0.000000, 0.851575, 0.461275),
    (0.000000, 0.845283, 0.434350),
    (0.000000, 0.838992, 0.407425),
    (0.000000, 0.832700, 0.380500),
    (0.000000, 0.832308, 0.354858),
    (0.000000, 0.831917, 0.329217),
    (0.000000, 0.831525, 0.303575),
    (0.000000, 0.831133, 0.277933),
    (0.000000, 0.830742, 0.252292),
    (0.000000, 0.830350, 0.226650),
    (0.000000, 0.829958, 0.201008),
    (0.000000, 0.829567, 0.175367),
    (0.000000, 0.829175, 0.149725),
    (0.000000, 0.828783, 0.124083),
    (0.000000, 0.828392, 0.098442),
    (0.000000, 0.828000, 0.072800),
    (0.033167, 0.834167, 0.066733),
    (0.066333, 0.840333, 0.060667),
    (0.099500, 0.846500, 0.054600),
    (0.132667, 0.852667, 0.048533),
    (0.165833, 0.858833, 0.042467),
    (0.199000, 0.865000, 0.036400),
    (0.232167, 0.871167, 0.030333),
    (0.265333, 0.877333, 0.024267),
    (0.298500, 0.883500, 0.018200),
    (0.331667, 0.889667, 0.012133),
    (0.364833, 0.895833, 0.006067),
    (0.398000, 0.902000, 0.000000),
    (0.430950, 0.902000, 0.000000),
    (0.463900, 0.902000, 0.000000),
    (0.496850, 0.902000, 0.000000),
    (0.529800, 0.902000, 0.000000),
    (0.562750, 0.902000, 0.000000),
    (0.595700, 0.902000, 0.000000),
    (0.628650, 0.902000, 0.000000),
    (0.661600, 0.902000, 0.000000),
    (0.694550, 0.902000, 0.000000),
    (0.727500, 0.902000, 0.000000),
    (0.760450, 0.902000, 0.000000),
    (0.793400, 0.902000, 0.000000),
    (0.810617, 0.897133, 0.003983),
    (0.827833, 0.892267, 0.007967),
    (0.845050, 0.887400, 0.011950),
    (0.862267, 0.882533, 0.015933),
    (0.879483, 0.877667, 0.019917),
    (0.896700, 0.872800, 0.023900),
    (0.913917, 0.867933, 0.027883),
    (0.931133, 0.863067, 0.031867),
    (0.948350, 0.858200, 0.035850),
    (0.965567, 0.853333, 0.039833),
    (0.982783, 0.848467, 0.043817),
    (1.000000, 0.843600, 0.047800),
    (0.995725, 0.824892, 0.051600),
    (0.991450, 0.806183, 0.055400),
    (0.987175, 0.787475, 0.059200),
    (0.982900, 0.768767, 0.063000),
    (0.978625, 0.750058, 0.066800),
    (0.974350, 0.731350, 0.070600),
    (0.970075, 0.712642, 0.074400),
    (0.965800, 0.693933, 0.078200),
    (0.961525, 0.675225, 0.082000),
    (0.957250, 0.656517, 0.085800),
    (0.952975, 0.637808, 0.089600),
    (0.948700, 0.619100, 0.093400),
    (0.952975, 0.600408, 0.085617),
    (0.957250, 0.581717, 0.077833),
    (0.961525, 0.563025, 0.070050),
    (0.965800, 0.544333, 0.062267),
    (0.970075, 0.525642, 0.054483),
    (0.974350, 0.506950, 0.046700),
    (0.978625, 0.488258, 0.038917),
    (0.982900, 0.469567, 0.031133),
    (0.987175, 0.450875, 0.023350),
    (0.991450, 0.432183, 0.015567),
    (0.995725, 0.413492, 0.007783),
    (1.000000, 0.394800, 0.000000),
    (0.998342, 0.361900, 0.000000),
    (0.996683, 0.329000, 0.000000),
    (0.995025, 0.296100, 0.000000),
    (0.993367, 0.263200, 0.000000),
    (0.991708, 0.230300, 0.000000),
    (0.990050, 0.197400, 0.000000),
    (0.988392, 0.164500, 0.000000),
    (0.986733, 0.131600, 0.000000),
    (0.985075, 0.098700, 0.000000),
    (0.983417, 0.065800, 0.000000),
    (0.981758, 0.032900, 0.000000),
    (0.980100, 0.000000, 0.000000),
    (0.955925, 0.000000, 0.000000),
    (0.931750, 0.000000, 0.000000),
    (0.907575, 0.000000, 0.000000),
    (0.883400, 0.000000, 0.000000),
    (0.859225, 0.000000, 0.000000),
    (0.835050, 0.000000, 0.000000),
    (0.810875, 0.000000, 0.000000),
    (0.786700, 0.000000, 0.000000),
    (0.762525, 0.000000, 0.000000),
    (0.738350, 0.000000, 0.000000),
    (0.714175, 0.000000, 0.000000),
    (0.690000, 0.000000, 0.000000),
    (0.715833, 0.083333, 0.083333),
    (0.741667, 0.166667, 0.166667),
    (0.767500, 0.250000, 0.250000),
    (0.793333, 0.333333, 0.333333),
    (0.819167, 0.416667, 0.416667),
    (0.845000, 0.500000, 0.500000),
    (0.870833, 0.583333, 0.583333),
    (0.896667, 0.666667, 0.666667),
    (0.922500, 0.750000, 0.750000),
    (0.948333, 0.833333, 0.833333),
    (0.974167, 0.916667, 0.916667),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000),
    (1.000000, 1.000000, 1.000000)
]
        ds9_sls_cmap = ListedColormap(ds9_sls_colors,name=ds9_name)
        colormaps.register(name=ds9_name, cmap=ds9_sls_cmap)
        ds9_sls_r_cmap = ds9_sls_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_sls_r_cmap)
    return()

def register_hsv():
    def hsv_to_rgb(h, s, v):
        h = h % 360
        h /= 60.0
        i = int(h)
        f = h - i
        p = v * (1 - s)
        q = v * (1 - s * f)
        t = v * (1 - s * (1 - f))
        if i == 0:
            return v, t, p
        elif i == 1:
            return q, v, p
        elif i == 2:
            return p, v, t
        elif i == 3:
            return p, q, v
        elif i == 4:
            return t, p, v
        elif i == 5:
            return v, p, q

    ds9_name='ds9_hsv'
    if is_cmap_registered(ds9_name):
        print(f'{ds9_name} already registered')
    else:
        ds9_hsv_colors=[]
        size=200
        for i in range(size):
            frac = 1.0 - (i / (size - 1))
            h = frac * 360.0 + 270.0
            s = abs(np.sin(frac * np.pi))
            v = (1.0 - frac) ** (1.0 / 3.0)
            ds9_hsv_colors.append(hsv_to_rgb(h, s, v))
        ds9_hsv_cmap = ListedColormap(ds9_hsv_colors,name=ds9_name)
        colormaps.register(name=ds9_name, cmap=ds9_hsv_cmap)
        ds9_hsv_r_cmap = ds9_hsv_cmap.reversed()
        colormaps.register(name=ds9_name+'_r', cmap=ds9_hsv_r_cmap)
    return()

def register_all():
    for name, func in globals().items():
        if name.startswith("register_") and name != "register_all" and callable(func):
            func()
    return()