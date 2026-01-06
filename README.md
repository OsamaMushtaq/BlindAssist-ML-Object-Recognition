# 🦯 BlindAssist
## Machine Learning Enhanced Object Recognition, GPS Tracking, and Speech Feedback

**Final Year Project (FYP)**  
**Lahore Garrison University**  
**Batch: 2024**

---

## 📌 Project Overview

Over **284 million people worldwide** live with visual impairments, facing daily challenges in independent navigation and personal safety. While several assistive tools exist, many lack **real-time intelligence**, **environment awareness**, and **integrated safety mechanisms**.

**BlindAssist** is a **hardware–software integrated smart assistive system** designed to enhance mobility and safety for visually impaired individuals. By combining **machine learning–based object recognition**, **ultrasonic obstacle detection**, **GPS navigation**, and **speech feedback**, the system provides real-time guidance and emergency support through a smart stick interface.

---

## ❗ Problem Statement

Existing assistive technologies for visually impaired individuals often lack real-time assistance and comprehensive functionality, leaving users vulnerable in dynamic environments. The absence of intelligent obstacle detection, object recognition, and navigation support increases dependency and safety risks.

The **BlindAssist** project addresses these challenges by integrating **machine learning, GPS tracking, and speech feedback** into a single intelligent system. The aim is to empower visually impaired individuals, bridge accessibility gaps, and foster inclusivity through innovative assistive technology.

---

## 💡 Solution Overview

BlindAssist functions as a **smart assistive stick** that continuously monitors the surrounding environment and provides **audio-based guidance** to the user.

### Key Features
- 🔍 Real-time obstacle detection using ultrasonic sensors  
- 🧠 Machine learning–based object recognition via camera input  
- 🗺️ GPS-based navigation and location tracking  
- 🔊 Speech feedback system for hands-free interaction  
- 🚨 Emergency alert mechanism using GSM communication  

---

## 🏗️ System Architecture & Workflow

The following diagram illustrates the complete workflow of the BlindAssist system, including user interaction, sensor processing, object recognition, navigation assistance, and emergency alert handling.

![System Architecture and Workflow](diagrams/dfd.png)

---

## 🦯 Hardware Prototype

The physical prototype integrates sensing, processing, and communication modules into a compact smart stick suitable for real-world usage.

![BlindAssist Hardware Prototype](hardware/stick.jpg)

---

## 🔌 Circuit Design

The circuit diagram shows the interconnection between the Raspberry Pi, ultrasonic sensors, camera module, GPS, GSM module, and power supply.

![Circuit Diagram](hardware/circuit_diagram.png)

---

## 🧩 Hardware Components

- **Raspberry Pi 4 Model B** – Central processing unit  
- **Ultrasonic Sensors (HC-SR04)** – Obstacle detection  
- **Raspberry Pi Camera Module v2** – Image capture  
- **GPS Neo-6M Module** – Location tracking  
- **GSM SIM900A Module** – Emergency alerts  
- **Li-Po Battery & LM7805 Regulator** – Power management  
- **Push Buttons** – Emergency and system control  

---

## 💻 Software Tools & Libraries

- **Python** – Primary programming language  
- **RPi.GPIO** – GPIO interfacing  
- **OpenCV** – Image processing and object recognition  
- **TensorFlow Lite** – ML inference on Raspberry Pi  
- **Picamera2** – Camera interface  
- **pyttsx3** – Text-to-speech conversion  
- **pySerial** – GPS and GSM communication  

---

## ⚙️ System Evaluation & Results

The system was rigorously evaluated across core functionalities.

### Performance Summary
- **Obstacle Detection:** ±1 cm error margin  
- **Object Recognition:** ~92% accuracy  
- **Navigation Assistance:** GPS accuracy within 3 meters  
- **Emergency Alerts:** Message sent within ~8 seconds  

These results confirm that **BlindAssist enhances navigation safety and situational awareness**.

---

## 📂 Repository Structure

```text
BlindAssist-ML-Object-Recognition/
├── src/            # Core source code
├── hardware/       # Hardware images & circuit diagrams
├── diagrams/       # System architecture & workflow
├── docs/           # SRS, Proposal, Final Report
└── README.md
