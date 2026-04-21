import numpy as np
import matplotlib.pyplot as plt
import os

scores = np.load("output/binplot_data/image_scores.npy")
labels = np.load("output/binplot_data/image_labels.npy")

normal_scores = scores[labels == 0]
anomaly_scores = scores[labels == 1]

print("Normal samples:", len(normal_scores))
print("Anomaly samples:", len(anomaly_scores))
print("Normal score range:", float(normal_scores.min()), "to", float(normal_scores.max()))
print("Anomaly score range:", float(anomaly_scores.min()), "to", float(anomaly_scores.max()))

os.makedirs("output/binplot_data", exist_ok=True)

plt.figure(figsize=(8, 5))
plt.hist(normal_scores, bins=20, alpha=0.6, label="Good")
plt.hist(anomaly_scores, bins=20, alpha=0.6, label="Anomaly")

plt.xlabel("Anomaly Score")
plt.ylabel("Number of Images")
plt.title("Image-level Score Distribution")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("output/binplot_data/binplot_hist.png", dpi=200)
plt.show()
