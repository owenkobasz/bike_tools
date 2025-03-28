# stem_viewer_app.py

import streamlit as st
import math
import matplotlib.pyplot as plt

st.title("Bike Stem Comparison Tool (Side View, with Steerer)")

# --- Sidebar Inputs ---
st.sidebar.header("Original Stem Setup")
orig_headtube_angle = st.sidebar.number_input("Original Headtube Angle (°)", min_value=60.0, max_value=75.0, value=72.0, step=0.5)
orig_spacers = st.sidebar.number_input("Original Spacer Stack Height (mm)", min_value=0.0, value=10.0, step=1.0)
orig_stem_length = st.sidebar.number_input("Original Stem Length (mm)", min_value=0.0, value=100.0, step=1.0)
orig_stem_rise = st.sidebar.number_input("Original Stem Rise (°)", value=6.0, step=0.5)

st.sidebar.header("New Stem Setup")
new_headtube_angle = st.sidebar.number_input("New Headtube Angle (°)", min_value=60.0, max_value=75.0, value=70.0, step=0.5)
new_spacers = st.sidebar.number_input("New Spacer Stack Height (mm)", min_value=0.0, value=5.0, step=1.0)
new_stem_length = st.sidebar.number_input("New Stem Length (mm)", min_value=0.0, value=90.0, step=1.0)
new_stem_rise = st.sidebar.number_input("New Stem Rise (°)", value=-6.0, step=0.5)

# --- Calculation ---
def steerer_top(height, angle):
    rad = math.radians(angle)
    return height * math.cos(rad), height * math.sin(rad)

def stem_tip(start_x, start_y, length, rise_angle):
    rad = math.radians(rise_angle)
    return start_x + length * math.cos(rad), start_y + length * math.sin(rad)

# Original
orig_x_spacer, orig_y_spacer = steerer_top(orig_spacers, orig_headtube_angle)
orig_x_tip, orig_y_tip = stem_tip(orig_x_spacer, orig_y_spacer, orig_stem_length, orig_stem_rise)

# New
new_x_spacer, new_y_spacer = steerer_top(new_spacers, new_headtube_angle)
new_x_tip, new_y_tip = stem_tip(new_x_spacer, new_y_spacer, new_stem_length, new_stem_rise)

# Deltas
dx = new_x_tip - orig_x_tip
dy = new_y_tip - orig_y_tip

# --- Display ---
st.subheader("Position Difference")
st.write(f"**Horizontal Change:** {dx:.1f} mm")
st.write(f"**Vertical Change:** {dy:.1f} mm")

# --- Plot ---
fig, ax = plt.subplots()

def draw_setup(spacer_x, spacer_y, tip_x, tip_y, color, label):
    ax.plot([0, spacer_x], [0, spacer_y], color=color, linewidth=2, alpha=0.7)
    ax.plot([spacer_x, tip_x], [spacer_y, tip_y], color=color, linewidth=3, label=label)

# Draw
draw_setup(orig_x_spacer, orig_y_spacer, orig_x_tip, orig_y_tip, "blue", "Original Stem")
draw_setup(new_x_spacer, new_y_spacer, new_x_tip, new_y_tip, "green", "New Stem")

# Delta line
ax.plot([orig_x_tip, new_x_tip], [orig_y_tip, new_y_tip], color="gray", linestyle=":", label="Change")

# Styling
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("Stem Position Comparison (Side View, with Steerer)")
ax.set_xlabel("Horizontal (mm)")
ax.set_ylabel("Vertical (mm)")

# Padding
all_x = [0, orig_x_tip, new_x_tip]
all_y = [0, orig_y_tip, new_y_tip]
padding = 20
ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
ax.set_ylim(0, max(all_y) + padding)

st.pyplot(fig)
