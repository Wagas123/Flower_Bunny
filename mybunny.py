{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "340b13a7-4a58-448f-986f-40bfc844957e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# Streamlit app\u001b[39;00m\n\u001b[0;32m      6\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m🌸 Flower Simulation 🌸\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import streamlit as st\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"🌸 Flower Simulation 🌸\")\n",
    "st.write(\"A beautiful flower just for you! 😊\")\n",
    "\n",
    "# Special Message\n",
    "st.markdown(\"## Happy Flower's Day 'Bunny' Ms. Lorraine!! 💐\")\n",
    "st.markdown(\"### From J 💖\")\n",
    "\n",
    "# Define parameters for the flower\n",
    "n_petals = st.slider(\"Number of Petals\", min_value=3, max_value=12, value=6)\n",
    "k = n_petals / 2  # Controls the number of petals\n",
    "r_max = 10  # Maximum radius\n",
    "\n",
    "# Generate theta values\n",
    "theta = np.linspace(0, 2 * np.pi, 1000)\n",
    "\n",
    "# Compute the radius as a function of theta\n",
    "r = r_max * np.cos(k * theta)\n",
    "\n",
    "# Convert to Cartesian coordinates\n",
    "x = r * np.cos(theta)\n",
    "y = r * np.sin(theta)\n",
    "\n",
    "# Plot the flower\n",
    "fig, ax = plt.subplots(figsize=(6, 6))\n",
    "ax.plot(x, y, color='purple', linewidth=2)\n",
    "ax.fill(x, y, color='pink', alpha=0.6)\n",
    "ax.set_aspect('equal')\n",
    "ax.axis('off')\n",
    "ax.set_title(\"A Flower for You 🌸\")\n",
    "\n",
    "# Display the plot in Streamlit\n",
    "st.pyplot(fig)\n",
    "\n",
    "st.write(\"Share this flower with someone special! 💖\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35de8319-046c-43ec-bf1e-1805a13b8d04",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Simple flower plot with a user-defined number of petals\n",
    "n_petals = int(input(\"Enter number of petals (3-12): \"))\n",
    "\n",
    "# Parameters for the flower\n",
    "k = n_petals / 2  # Controls the number of petals\n",
    "r_max = 10  # Maximum radius\n",
    "\n",
    "# Generate theta values\n",
    "theta = np.linspace(0, 2 * np.pi, 1000)\n",
    "\n",
    "# Compute the radius as a function of theta\n",
    "r = r_max * np.cos(k * theta)\n",
    "\n",
    "# Convert to Cartesian coordinates\n",
    "x = r * np.cos(theta)\n",
    "y = r * np.sin(theta)\n",
    "\n",
    "# Plot the flower\n",
    "fig, ax = plt.subplots(figsize=(6, 6))\n",
    "ax.plot(x, y, color='purple', linewidth=2)\n",
    "ax.fill(x, y, color='pink', alpha=0.6)\n",
    "ax.set_aspect('equal')\n",
    "ax.axis('off')\n",
    "ax.set_title(f\"Flower with {n_petals} Petals 🌸\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
