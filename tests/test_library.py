from plotsetups_me import plotparams
from plotsetups_me import ds9colors
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib.colors import LogNorm

#First we print the colormaps registered already in the run
ds9colors.list_registered_colormaps()
##We register all the colormaps
ds9colors.register_all()
##We check if they have been registered
ds9colors.list_registered_colormaps()

##Now we plot a broken exponential disk with all the colors
plotparams.plot_params()

model=fits.open('model_brokenexponential.fits')[0].data

#First figure: standard colors
fig = plt.figure(figsize=(15,30))

a_ax=fig.add_subplot(631)
a_ax.imshow(model,cmap='ds9_a', origin='lower')
a_ax.set_title('ds9_a')

aips_ax=fig.add_subplot(632)
aips_ax.imshow(model,cmap='ds9_aips', origin='lower')
aips_ax.set_title('ds9_aips')

b_ax=fig.add_subplot(633)
b_ax.imshow(model,cmap='ds9_b', origin='lower')
b_ax.set_title('ds9_b')

bb_ax=fig.add_subplot(634)
bb_ax.imshow(model,cmap='ds9_bb', origin='lower')
bb_ax.set_title('ds9_bb')

blue_ax=fig.add_subplot(635)
blue_ax.imshow(model,cmap='ds9_blue', origin='lower')
blue_ax.set_title('ds9_blue')

color_ax=fig.add_subplot(636)
color_ax.imshow(model,cmap='ds9_color', origin='lower')
color_ax.set_title('ds9_color')

cool_ax=fig.add_subplot(637)
cool_ax.imshow(model,cmap='ds9_cool', origin='lower')
cool_ax.set_title('ds9_cool')

green_ax=fig.add_subplot(638)
green_ax.imshow(model,cmap='ds9_green', origin='lower')
green_ax.set_title('ds9_green')

grey_ax=fig.add_subplot(639)
grey_ax.imshow(model,cmap='ds9_grey', origin='lower')
grey_ax.set_title('ds9_grey')

he_ax=fig.add_subplot(6,3,10)
he_ax.imshow(model,cmap='ds9_he', origin='lower')
he_ax.set_title('ds9_he')

heat_ax=fig.add_subplot(6,3,11)
heat_ax.imshow(model,cmap='ds9_heat', origin='lower')
heat_ax.set_title('ds9_heat')

hsv_ax=fig.add_subplot(6,3,12)
hsv_ax.imshow(model,cmap='ds9_hsv', origin='lower')
hsv_ax.set_title('ds9_hsv')

i8_ax=fig.add_subplot(6,3,13)
i8_ax.imshow(model,cmap='ds9_i8', origin='lower')
i8_ax.set_title('ds9_i8')

rain_ax=fig.add_subplot(6,3,14)
rain_ax.imshow(model,cmap='ds9_rainbow', origin='lower')
rain_ax.set_title('ds9_rainbow')

red_ax=fig.add_subplot(6,3,15)
red_ax.imshow(model,cmap='ds9_red', origin='lower')
red_ax.set_title('ds9_red')

sls_ax=fig.add_subplot(6,3,16)
sls_ax.imshow(model,cmap='ds9_sls', origin='lower')
sls_ax.set_title('ds9_sls')

sti_ax=fig.add_subplot(6,3,17)
sti_ax.imshow(model,cmap='ds9_staircase', origin='lower')
sti_ax.set_title('ds9_staircase')

std_ax=fig.add_subplot(6,3,18)
std_ax.imshow(model,cmap='ds9_standard', origin='lower')
std_ax.set_title('ds9_standard')
plt.tight_layout()
plt.savefig('Example_normalcmpas.pdf')

#Second figure: reversed colormaps
fig = plt.figure(figsize=(15,30))

a_ax=fig.add_subplot(631)
a_ax.imshow(model,cmap='ds9_a_r', origin='lower')
a_ax.set_title('ds9_a_r')

aips_ax=fig.add_subplot(632)
aips_ax.imshow(model,cmap='ds9_aips_r', origin='lower')
aips_ax.set_title('ds9_aips_r')

b_ax=fig.add_subplot(633)
b_ax.imshow(model,cmap='ds9_b_r', origin='lower')
b_ax.set_title('ds9_b_r')

bb_ax=fig.add_subplot(634)
bb_ax.imshow(model,cmap='ds9_bb_r', origin='lower')
bb_ax.set_title('ds9_bb_r')

blue_ax=fig.add_subplot(635)
blue_ax.imshow(model,cmap='ds9_blue_r', origin='lower')
blue_ax.set_title('ds9_blue_r')

color_ax=fig.add_subplot(636)
color_ax.imshow(model,cmap='ds9_color_r', origin='lower')
color_ax.set_title('ds9_color_r')

cool_ax=fig.add_subplot(637)
cool_ax.imshow(model,cmap='ds9_cool_r', origin='lower')
cool_ax.set_title('ds9_cool_r')

green_ax=fig.add_subplot(638)
green_ax.imshow(model,cmap='ds9_green_r', origin='lower')
green_ax.set_title('ds9_green_r')

grey_ax=fig.add_subplot(639)
grey_ax.imshow(model,cmap='ds9_grey_r', origin='lower')
grey_ax.set_title('ds9_grey_r')

he_ax=fig.add_subplot(6,3,10)
he_ax.imshow(model,cmap='ds9_he_r', origin='lower')
he_ax.set_title('ds9_he_r')

heat_ax=fig.add_subplot(6,3,11)
heat_ax.imshow(model,cmap='ds9_heat_r', origin='lower')
heat_ax.set_title('ds9_heat_r')

hsv_ax=fig.add_subplot(6,3,12)
hsv_ax.imshow(model,cmap='ds9_hsv_r', origin='lower')
hsv_ax.set_title('ds9_hsv_r')

i8_ax=fig.add_subplot(6,3,13)
i8_ax.imshow(model,cmap='ds9_i8_r', origin='lower')
i8_ax.set_title('ds9_i8_r')

rain_ax=fig.add_subplot(6,3,14)
rain_ax.imshow(model,cmap='ds9_rainbow_r', origin='lower')
rain_ax.set_title('ds9_rainbow_r')

red_ax=fig.add_subplot(6,3,15)
red_ax.imshow(model,cmap='ds9_red_r', origin='lower')
red_ax.set_title('ds9_red_r')

sls_ax=fig.add_subplot(6,3,16)
sls_ax.imshow(model,cmap='ds9_sls_r', origin='lower')
sls_ax.set_title('ds9_sls_r')

sti_ax=fig.add_subplot(6,3,17)
sti_ax.imshow(model,cmap='ds9_staircase_r', origin='lower')
sti_ax.set_title('ds9_staircase_r')

std_ax=fig.add_subplot(6,3,18)
std_ax.imshow(model,cmap='ds9_standard_r', origin='lower')
std_ax.set_title('ds9_standard_r')
plt.tight_layout()
plt.savefig('Example_reversedcmpas.pdf')