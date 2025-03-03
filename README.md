# Indoor-Localization
this is my master thesis project

In this project, we aim to leverage a router and a receiver to capture RSSI and CSI measurements. The router used is a 4-antenna TP-Link Archer A5, while the receiver is an ESP32-WROOM-32 board.

RSSI provides a single value representing signal strength, whereas CSI includes both amplitude and phase information for each subcarrier. In this work, we use a default bandwidth of 20MHz (can be altered later), resulting in 64 subcarriers—52 of which carry meaningful data, while the remaining serve as headers, guard bands, or DC subcarriers.
