# haptic-medical-image-exploration
## Exploring Structure-Driven Haptic Signal Simulation for Interactive Medical Image Navigation
## Project Overview

This project presents a software-based prototype for simulating haptic feedback from medical images. The system processes MRI scans to extract structural boundaries and converts them into simulated tactile signals that represent variations in tissue structure. These signals are then mapped to an interactive visualization interface, allowing users to explore the image while observing changes in feedback intensity.

The prototype includes both an interactive exploration component and an automated processing pipeline. The interactive module demonstrates how simulated tactile cues can guide user navigation across image regions, while the batch processing module evaluates feedback distributions across multiple images and generates reproducible outputs. By integrating image processing, interaction design, and quantitative analysis, the project explores how computational methods can approximate tactile guidance in digital medical imaging environments.

This work aims to investigate how structure-driven feedback mechanisms could support perception-aware interfaces in medical visualization systems, particularly in contexts where tactile cues may improve user understanding of spatial and structural features.

## 🔹 Motivation

Haptic feedback plays a critical role in enhancing perception and interaction in immersive interfaces. While physical haptic devices are commonly used in surgical simulators and rehabilitation systems, software-based approximations can provide a scalable alternative for exploratory research.

This project explores how structural information in medical images can be translated into simulated tactile signals, supporting the development of perception-aware interfaces for medical visualization.

## 🔹 Features

- MRI image processing pipeline

- Edge-based structural extraction

- Simulated haptic feedback mapping

- Interactive cursor-based exploration

- Automated dataset processing

- Quantitative feedback analysis

- Reproducible result generation
- 
## 🔹 Methodology

**1. Image Acquisition**

MRI images are loaded from a local dataset.

**2. Structure Extraction**

Gaussian smoothing and Canny edge detection identify tissue boundaries.

**3. Haptic Signal Simulation**

Edge strength is normalized to represent feedback intensity.

**4. Interactive Visualization**

Cursor movement dynamically queries local feedback strength.

**5. Dataset-Level Analysis**

Random sampling is used to analyze feedback distributions across images.

## 🔹 Installation
bash```
pip install numpy opencv-python matplotlib
```
bash```python main.py
```
*The script will:*

- Process all images in the dataset

- Save structural and feedback outputs

- Launch an interactive visualization window

- Generate a feedback distribution plot

## 🔹 Research Perspective

This prototype investigates how structure-driven computational feedback could support tactile perception in digital environments. The approach may inform future work in:

- haptic-assisted medical visualization

- perception-aware human–computer interfaces

- virtual surgical training environments

- rehabilitation interaction systems
  
## 🔹 Future Work

- Incorporating depth estimation for richer tactile mapping

- Learning feedback models using machine learning

- Extending to 3D volumetric medical imaging

- Integrating with physical haptic devices

- Conducting user studies on perception improvement
