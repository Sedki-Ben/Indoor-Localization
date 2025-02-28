import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def preprocess_csi_data(csi_amplitude, csi_phase, rssi_values):
    """
    Preprocess the CSI and RSSI data for model input.
    
    Parameters:
    - csi_amplitude: numpy array of shape (num_samples, num_subcarriers)
    - csi_phase: numpy array of shape (num_samples, num_subcarriers) (already unwrapped)
    - rssi_values: numpy array of shape (num_samples,)
    
    Returns:
    - Preprocessed CSI features
    - Normalized RSSI values
    - Tuple of fitted scalers for potential inverse transformations
    """

    # Normalize CSI amplitude using StandardScaler
    scaler_amp = StandardScaler()
    csi_amplitude_norm = scaler_amp.fit_transform(csi_amplitude)
    print("Normalized CSI Amplitude shape:", csi_amplitude_norm.shape)
    print("Sample of normalized CSI Amplitude (first sample, first 5 subcarriers):", csi_amplitude_norm[0, :5])

    # Normalize CSI phase to range [-1, 1] using MinMaxScaler
    scaler_phase = MinMaxScaler(feature_range=(-1, 1))
    csi_phase_norm = scaler_phase.fit_transform(csi_phase)
    print("Normalized CSI Phase shape:", csi_phase_norm.shape)
    print("Sample of normalized CSI Phase (first sample, first 5 subcarriers):", csi_phase_norm[0, :5])

    # Normalize RSSI values to [0, 1] range using MinMaxScaler
    rssi_values = rssi_values.reshape(-1, 1)  # Reshape for compatibility
    scaler_rssi = MinMaxScaler(feature_range=(0, 1))
    rssi_norm = scaler_rssi.fit_transform(rssi_values)
    print("Normalized RSSI shape:", rssi_norm.shape)
    print("Sample of normalized RSSI (first 5 samples):", rssi_norm[:5].flatten())

    # Stack amplitude and phase as separate channels
    csi_features = np.stack([csi_amplitude_norm, csi_phase_norm], axis=2)
    print("Final CSI features shape:", csi_features.shape)

    return csi_features, rssi_norm, (scaler_amp, scaler_phase, scaler_rssi)



    #Call the preprocessing function
    csi_features, rssi_norm, scalers = preprocess_csi_data(csi_amplitude, csi_phase, rssi_values)

    #Optionally, save the preprocessed data for later use
    np.save("csi_features.npy", csi_features)
    np.save("rssi_norm.npy", rssi_norm)