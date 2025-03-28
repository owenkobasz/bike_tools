# stem_viewer_app.py

import streamlit as st
import math
import matplotlib.pyplot as plt

st.title("Bike Stem Comparison Tool")

# --- Mode Selection ---
mode = st.sidebar.radio("Select Mode", ["Basic", "Advanced"])

# --- Sidebar Inputs ---
if mode == "Basic":
    st.sidebar.header("New vs Old Stem")
    headtube_angle = st.sidebar.number_input("Headtube Angle (°)", min_value=60.0, max_value=75.0, value=72.0, step=0.5)

    st.sidebar.header("Original Stem")
    orig_stem_length = st.sidebar.number_input("Original Stem Length (mm)", min_value=0.0, value=100.0, step=1.0)
    orig_stem_rise = st.sidebar.number_input("Original Stem Rise (°)", value=6.0, step=0.5)
    orig_spacers = st.sidebar.number_input("Original Spacer Stack Height (mm)", min_value=0.0, value=10.0, step=1.0)

    st.sidebar.header("New Stem")
    new_stem_length = st.sidebar.number_input("New Stem Length (mm)", min_value=0.0, value=90.0, step=1.0)
    new_stem_rise = st.sidebar.number_input("New Stem Rise (°)", value=-6.0, step=0.5)
    new_spacers = st.sidebar.number_input("New Spacer Stack Height (mm)", min_value=0.0, value=5.0, step=1.0)

else:
    st.sidebar.header("Comparing Stems on Different Bikes")
    st.sidebar.header("Original Bike Setup")
    orig_headtube_angle = st.sidebar.number_input("Original Headtube Angle (°)", min_value=60.0, max_value=75.0, value=72.0, step=0.5)
    orig_reach = st.sidebar.number_input("Original Frame Reach (mm)", min_value=300.0, value=390.0, step=1.0)
    orig_stack = st.sidebar.number_input("Original Frame Stack (mm)", min_value=300.0, value=550.0, step=1.0)
    orig_spacers = st.sidebar.number_input("Original Spacer Stack Height (mm)", min_value=0.0, value=10.0, step=1.0)
    orig_stem_length = st.sidebar.number_input("Original Stem Length (mm)", min_value=0.0, value=100.0, step=1.0)
    orig_stem_rise = st.sidebar.number_input("Original Stem Rise (°)", value=6.0, step=0.5)

    st.sidebar.header("New Bike Setup")
    new_headtube_angle = st.sidebar.number_input("New Headtube Angle (°)", min_value=60.0, max_value=75.0, value=70.0, step=0.5)
    new_reach = st.sidebar.number_input("New Frame Reach (mm)", min_value=300.0, value=395.0, step=1.0)
    new_stack = st.sidebar.number_input("New Frame Stack (mm)", min_value=300.0, value=555.0, step=1.0)
    new_spacers = st.sidebar.number_input("New Spacer Stack Height (mm)", min_value=0.0, value=5.0, step=1.0)
    new_stem_length = st.sidebar.number_input("New Stem Length (mm)", min_value=0.0, value=90.0, step=1.0)
    new_stem_rise = st.sidebar.number_input("New Stem Rise (°)", value=-6.0, step=0.5)

# --- Calculation ---
def steerer_top(height, angle, base_x=0, base_y=0):
    height += 100  # pad for aesthetic reasons
    rad = math.radians(180 - angle)
    return base_x + height * math.cos(rad), base_y + height * math.sin(rad)

def stem_tip(start_x, start_y, length, rise_angle):
    rad = math.radians(rise_angle)
    return start_x + length * math.cos(rad), start_y + length * math.sin(rad)

if mode == "Basic":
    # Both setups use same base and headtube angle
    orig_base_x, orig_base_y = 0, 0
    orig_x_spacer, orig_y_spacer = steerer_top(orig_spacers, headtube_angle)
    orig_x_tip, orig_y_tip = stem_tip(orig_x_spacer, orig_y_spacer, orig_stem_length, orig_stem_rise)

    new_base_x, new_base_y = 0, 0
    new_x_spacer, new_y_spacer = steerer_top(new_spacers, headtube_angle)
    new_x_tip, new_y_tip = stem_tip(new_x_spacer, new_y_spacer, new_stem_length, new_stem_rise)
else:
    # Advanced mode, compute difference relative to anchor
    anchor_x, anchor_y = 0, 0

    delta_x = new_reach - orig_reach
    delta_y = new_stack - orig_stack

    orig_base_x = anchor_x
    orig_base_y = anchor_y

    new_base_x = anchor_x + delta_x
    new_base_y = anchor_y + delta_y

    orig_x_spacer, orig_y_spacer = steerer_top(orig_spacers, orig_headtube_angle, orig_base_x, orig_base_y)
    orig_x_tip, orig_y_tip = stem_tip(orig_x_spacer, orig_y_spacer, orig_stem_length, orig_stem_rise)

    new_x_spacer, new_y_spacer = steerer_top(new_spacers, new_headtube_angle, new_base_x, new_base_y)
    new_x_tip, new_y_tip = stem_tip(new_x_spacer, new_y_spacer, new_stem_length, new_stem_rise)

# Deltas
dx = new_x_tip - orig_x_tip
dy = new_y_tip - orig_y_tip

# --- Display ---
st.write(f"**Difference in reach :** {dx:.1f} mm")
st.write(f"**Difference in Stack :** {dy:.1f} mm")

# --- Plot ---
fig, ax = plt.subplots()

fixed_xlim = (-100, 250)
fixed_ylim = (-20, 250)

def draw_setup(spacer_x, spacer_y, tip_x, tip_y, base_x, base_y, color, label):
    ax.plot([base_x, spacer_x], [base_y, spacer_y], color=color, linewidth=2, alpha=0.7)
    ax.plot([spacer_x, tip_x], [spacer_y, tip_y], color=color, linewidth=3, label=label)

if mode == "Basic":
    draw_setup(orig_x_spacer, orig_y_spacer, orig_x_tip, orig_y_tip, orig_base_x, orig_base_y, "blue", "Original Stem")
    draw_setup(new_x_spacer, new_y_spacer, new_x_tip, new_y_tip, new_base_x, new_base_y, "green", "New Stem")
else:
    draw_setup(orig_x_spacer, orig_y_spacer, orig_x_tip, orig_y_tip, orig_base_x, orig_base_y, "blue", "Original Stem")
    draw_setup(new_x_spacer, new_y_spacer, new_x_tip, new_y_tip, new_base_x, new_base_y, "green", "New Stem")

# Delta line
ax.plot([orig_x_tip, new_x_tip], [orig_y_tip, new_y_tip], color="gray", linestyle=":", label="Change")

# Styling
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title(f"Stem Position Comparison ({mode} Mode)")
ax.set_xlabel("Horizontal (mm)")
ax.set_ylabel("Vertical (mm)")

# Fixed plot limits
ax.set_xlim(fixed_xlim)
ax.set_ylim(fixed_ylim)

st.pyplot(fig)