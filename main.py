import cv2
import os
os.makedirs("results", exist_ok=True)
import numpy as np
import matplotlib.pyplot as plt

# Load image
image_folder = "images"

for filename in os.listdir(image_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(image_folder, filename)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        # Edge detection
        blurred = cv2.GaussianBlur(img, (5,5), 0)
        edges = cv2.Canny(blurred, 30, 120)

        # Save edges in folder
        os.makedirs("results/edges", exist_ok=True)
        cv2.imwrite(f"results/edges/edges_{filename}", edges)

        # Normalize feedback strength
        feedback = edges.astype(float) / 255.0

        # Create feedback map
        feedback_map = cv2.applyColorMap(
            (feedback*255).astype(np.uint8),
            cv2.COLORMAP_JET
        )

        # Save feedback map
        os.makedirs("results/feedback", exist_ok=True)
        cv2.imwrite(f"results/feedback/feedback_{filename}", feedback_map)

        print("Processed:", filename)
# ---- Load one image again for interactive demo ----

demo_path = "images/N1.jpeg"   # choose any image
img = cv2.imread(demo_path, cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(img, (5,5), 0)
edges = cv2.Canny(blurred, 30, 120)

feedback = edges.astype(float) / 255.0
display = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Mouse event function
def mouse_move(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        strength = feedback[y, x]

        # Copy image to draw on
        temp = display.copy()

        # Draw cursor circle
        cv2.circle(temp, (x,y), 5, (0,0,255), -1)

        # Show strength text
        text = f"Feedback strength: {strength:.2f}"
        cv2.putText(temp, text, (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.imshow("Interactive MRI Haptic Map", temp)


# Create window
cv2.namedWindow("Interactive MRI Haptic Map")
cv2.setMouseCallback("Interactive MRI Haptic Map", mouse_move)

# Show initial image
cv2.imshow("Interactive MRI Haptic Map", display)

cv2.waitKey(0)
cv2.destroyAllWindows()

# --- Research analysis: sample feedback across image ---


# Randomly sample points
h, w = feedback.shape
samples = []

for _ in range(1000):
    x = np.random.randint(0, w)
    y = np.random.randint(0, h)
    samples.append(feedback[y, x])
samples = np.array(samples)

print("Average feedback:", samples.mean())
print("Max feedback:", samples.max())

# Plot distribution
plt.hist(samples, bins=20)
plt.title("Distribution of Simulated Haptic Strength")
plt.xlabel("Feedback value")
plt.ylabel("Frequency")

plt.savefig("results/feedback_histogram.png")
plt.show()