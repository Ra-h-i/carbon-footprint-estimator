# 🌱 EcoTrack AI — Personal & Campus Carbon Footprint Estimator

> **1M1B Internship Project: Green Skills & Applied AI for Climate Action**  

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Framework](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![Model](https://img.shields.io/badge/Model-Random%20Forest%20Regressor-brightgreen.svg)

---

##  Project Overview

**EcoTrack AI** is an interactive, Machine Learning-powered dashboard designed to help individuals, students, and educational campuses track, visualize, and reduce their carbon footprint. By analyzing personal and daily consumption data—such as electricity usage, transportation, screen time, and waste generation—the application predicts monthly $\text{CO}_2$ emissions with high accuracy and generates real-time, actionable sustainability recommendations.

---

##  Link of deployed webapp: 
https://carbon-footprint-estimator-d3ryta4xamjqzarzkj9yzd.streamlit.app/

---

##  Problem Statement

* **The Challenge:** Most individuals and educational institutions lack real-time visibility into their daily carbon emissions, leading to unmonitored energy waste and high carbon output.
* **The Impact:** Without quantitative data and personal benchmarks, adoption of sustainable habits remains low across campuses.
* **The Solution:** A predictive ML engine paired with an intuitive UI that translates complex consumption metrics into clear carbon estimates and targeted reduction steps[cite: 1, 2].

---

##  Key Features

*  **Predictive Emissions Engine:** Utilizes a trained Random Forest Regressor ($R^2 \approx 0.97$) to estimate monthly carbon footprint ($\text{kg CO}_2\text{e}$) based on daily logs[cite: 1, 2].
*  **Dynamic Benchmarking:** Instantly flags total emissions against eco-friendly targets using visual status indicators (Sustainable / Moderate / High Impact)
*  **Category Breakdown Chart:** Interactive Donut Chart generated via Plotly displaying individual contributions across electricity, travel, devices, and waste
*  **Rule-Based Recommendation Engine:** Provides customized, high-impact strategies tailored to the user's highest emission sources.
*  **Glassmorphism UI Design:** Custom CSS-styled dark interface for optimal visual clarity and scannability.

---

##  Tech Stack & Dependencies

* **Language:** Python 3.14
* **Machine Learning:** `scikit-learn` (Random Forest Regressor), `numpy`, `pandas`
* **Frontend / Web UI:** `streamlit`
* **Data Visualization:** `plotly`
* **Model Serialization:** `joblib`

---

##  Machine Learning Model & Conversion Factors

The ML model is trained on standard environmental conversion metrics:

| Consumption Category | Standard Emission Factor |
| :--- | :--- |
| **Electricity** | $\approx 0.85\text{ kg CO}_2/\text{kWh}$ |
| **Car Travel** | $\approx 0.18\text{ kg CO}_2/\text{km}$ |
| **Public Transit** | $\approx 0.05\text{ kg CO}_2/\text{km}$ |
| **Device Usage** | $\approx 0.03\text{ kg CO}_2/\text{hour}$ |
| **Waste Generation** | $\approx 1.20\text{ kg CO}_2/\text{kg}$|

---


