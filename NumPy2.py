import numpy as np

prices = np.array([100, 200, 300, 400])

# Apply 18% GST
gst = prices * 0.18

total = prices + gst

print("Original Prices:", prices)
print("GST:", gst)
print("Final Prices:", total)