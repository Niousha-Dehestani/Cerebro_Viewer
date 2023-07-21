#load the Libraries

import matplotlib.pyplot as plt
from cerebro import cerebro_brain_utils as cbu
from cerebro import cerebro_brain_viewer as cbv
import numpy as np


my_brain_viewer = cbv.Cerebro_brain_viewer(offscreen=True,  background_color=(1,1,1,0), null_color=(0.9, 0.9, 0.9, 0.3))
surface = "pial"
surface_model = my_brain_viewer.load_template_GIFTI_cortical_surface_models(surface)

# render a surface
cifti_space = my_brain_viewer.visualize_cifti_space(
    volumetric_structures="none", # Change to "none" for just cortex, or "all" for cortex, subcortex, cerebellum, and brainstem
    cifti_expansion_scale=20,
    cifti_left_right_seperation=10,
    volumetric_structure_offset=(0, 5, -25),
)

#render data over surface
# Specify the specific coordinate and colors(Amygdala and prefrontal cortex)

coordinate = np.array([
    [-27,-4,-20],
    [1,55,-3]
])

my_brain_viewer.visualize_spheres(coordinate, radii=[10, 15], coordinate_offset=0, color=(0,0.5,0.5))

#show plot
fig, ax = plt.subplots(figsize=(10,10))
ax.axis('off')
my_brain_viewer.offscreen_draw_to_matplotlib_axes(ax)

# Clear this viewer
my_brain_viewer.viewer.window.destroy()