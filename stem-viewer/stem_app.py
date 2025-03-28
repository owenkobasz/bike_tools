import streamlit as st
import math

st.title("Bike Stem Length & Angle Calculator")
st.write(
    "Compare two bike stems and see how the handlebar position changes."
)

# Input fields
st.sidebar.header("Original Stem")
orig_length = st.sidebar.number_input("Original Stem Length (mm)", min_value=0.0, value=100.0, step=1.0)
orig_angle = st.sidebar.number_input("Original Stem Angle (degrees)", value=6.0, step=0.5)

st.sidebar.header("New Stem")
new_length = st.sidebar.number_input("New Stem Length (mm)", min_value=0.0, value=90.0, step=1.0)
new_angle = st.sidebar.number_input("New Stem Angle (degrees)", value=10.0, step=0.5)

# Calculate horizontal and vertical positions
def stem_position(length, angle_deg):
    angle_rad = math.radians(angle_deg)
    x = length * math.cos(angle_rad)
    y = length * math.sin(angle_rad)
    return x, y

orig_x, orig_y = stem_position(orig_length, orig_angle)
new_x, new_y = stem_position(new_length, new_angle)

dx = new_x - orig_x
dy = new_y - orig_y

# Display results
st.subheader("Results")
st.write(f"**Horizontal Change:** {dx:.1f} mm")
st.write(f"**Vertical Change:** {dy:.1f} mm")

# Optional: simple plot
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.arrow(0, 0, orig_x, orig_y, head_width=5, color="blue", label="Original Stem")
ax.arrow(0, 0, new_x, new_y, head_width=5, color="green", label="New Stem")
ax.set_aspect('equal')
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.grid(True)
ax.legend(["Original Stem", "New Stem"])
st.pyplot(fig)

