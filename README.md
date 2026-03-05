# H2S False Alarm Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange)

Machine Learning powered API to classify H2S gas leak alarms as dangerous or false, reducing unnecessary emergency responses in chemical manufacturing.

[Features](#features) •
[Installation](#installation) •
[Usage](#usage) •
[API Documentation](#api-documentation)

</div>

---

# Table of Contents

- Problem Statement
- Solution Overview
- Features
- Technologies Used
- Model Performance
- Installation
- Usage
- API Documentation
- Project Structure
- Business Impact
- Future Enhancements
- Author

---

# Problem Statement

In chemical manufacturing environments, H2S (Hydrogen Sulfide) gas sensors trigger alarms when detecting potential gas leaks.

Frequent **false alarms** lead to:

- Unnecessary emergency team deployment
- Operational delays
- Increased maintenance and sanitation costs
- Alarm fatigue among safety personnel

**Goal:**  
Distinguish genuine hazards from false alarms **before dispatching emergency teams**.

---

# Solution Overview

This project implements a **Machine Learning classification system** that analyzes sensor data and predicts whether an alarm is dangerous.

Prediction Output:

| Value | Meaning |
|------|--------|
| 1 | Dangerous – Immediate response required |
| 0 | False Alarm – Safe to ignore |

The model is deployed as a **Flask REST API** so factory monitoring systems can classify alarms in real time.

---

# Features

## Intelligent Alarm Classification

- Real-time alarm prediction
- Binary classification
- Instant emergency response decision support

## Data Driven Analysis

The model analyzes **six sensor parameters**:

| Feature | Description |
|------|-------------|
| Ambient Temperature | Factory temperature |
| Calibration | Days since last calibration |
| Unwanted Substance Deposition | Deposits on sensor |
| Humidity (%) | Relative humidity |
| H2S Content (ppm) | Gas concentration |
| Detected Sensors | Number of sensors triggered |

## Production Ready API

- RESTful Flask API
- JSON request and response
- Health check endpoint
- Easy integration with monitoring systems

---

# Technologies Used

| Category | Tools |
|--------|------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API Framework | Flask |
| Model Storage | Pickle |
| API Testing | Postman, cURL |
| Version Control | Git, GitHub |

---

# Model Performance

Machine Learning Pipeline
