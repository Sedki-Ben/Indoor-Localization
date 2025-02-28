import numpy as np

# Load the saved data correctly
csi_amplitudes = np.load("data/csi_amplitude.npy", allow_pickle=True)
csi_phases = np.load("data/csi_phase.npy", allow_pickle=True)
rssi_values = np.load("data/rssi.npy", allow_pickle=True)
locations = np.load("data/locations.npy", allow_pickle=True)

# Print the shape of each dataset
print("CSI Amplitudes Shape:", csi_amplitudes.shape)
print("CSI Phases Shape:", csi_phases.shape)
print("RSSI Values Shape:", rssi_values.shape)
print("Locations Shape:", locations.shape)

# Preview some data
print("Sample Locations:\n", locations[:5])
print("Sample RSSI Values:\n", rssi_values[:5])