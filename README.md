# Control Systems Visualizer 🎛️

A comprehensive Python GUI application for analyzing and visualizing first-order control systems with real-time parameter adjustment and professional-grade plotting capabilities.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Control](https://img.shields.io/badge/Control%20Systems-Python--control-red)

---

## ✨ Features

- **🎯 Intuitive GUI Interface** — User-friendly parameter input with real-time validation  
- **📊 Multi-Plot Visualization** — Four synchronized analytical plots in a single dashboard  
- **⚡ Real-Time Analysis** — Instant visualization of parameter changes  
- **🎓 Educational Focus** — Perfect for control theory learning and academic demonstrations  
- **🔧 First-Order Systems** — Comprehensive analysis of transfer function:  
  \[
  G(s) = \frac{K}{\tau s + 1}
  \]

### Visualization Types
- **Closed-loop step response** — Transient and steady-state analysis  
- **Bode magnitude plot** — Frequency response in dB  
- **Bode phase plot** — Phase characteristics in degrees  
- **Nyquist diagram** — Stability analysis with critical point marking  

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher  
- pip package manager  

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/control-systems-visualizer.git
   cd control-systems-visualizer
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Install Tkinter**
   On some Linux distributions, you may need to install Tkinter separately:
   ```bash
   sudo apt-get install python3-tk
   ```

---

## 💡 Usage

### Launching the Application
```bash
python control_visualizer.py
```

### Parameter Configuration
- **K (System Gain):** Positive value controlling system amplification  
- **τ (Time Constant):** Positive value determining system response speed  

### Generating Visualizations
1. Enter desired values for **K** and **τ**  
2. Click **"Generate Plots"**  
3. Analyze the four synchronized plots that appear  

---

## 📈 Plot Descriptions

| Plot Type        | Position       | Key Features |
|------------------|----------------|---------------|
| **Step Response** | Top-left       | Rise time, settling time, steady-state value |
| **Bode Magnitude** | Top-right     | Gain margin, frequency response |
| **Bode Phase**     | Bottom-right  | Phase margin, phase characteristics |
| **Nyquist Plot**   | Bottom-left   | Stability margins, critical point |

### Step Response
- Displays system output for unit step input  
- Shows transient response characteristics  
- Visualizes steady-state behavior and settling time  

### Bode Plots
- **Magnitude Plot:** System gain (dB) vs. frequency (rad/s)  
- **Phase Plot:** Phase shift (degrees) vs. frequency (rad/s)  
- Essential for frequency-domain analysis  

### Nyquist Plot
- Complex plane representation of open-loop frequency response  
- Critical point (-1, 0) marked for stability assessment  
- Mirror image shown for negative frequencies  

---

## 🛠️ System Requirements

### Core Dependencies
```python
numpy>=1.21.0
matplotlib>=3.5.0
control>=0.9.4
tkinter>=8.6  # Usually included with Python
```

### Platform Support
✅ Windows 10/11  
✅ macOS 10.14+  
✅ Linux (Ubuntu 18.04+, CentOS 7+)  

---

## 🎯 Applications

### Educational Use Cases
- Control engineering coursework  
- System dynamics demonstrations  
- Control theory laboratory exercises  
- Frequency response method teaching  

### Professional Applications
- Quick control system analysis  
- Parameter tuning visualization  
- System stability assessment  
- Educational content development  

---

## 🖥️ Example Output

The application generates a comprehensive 2×2 subplot dashboard for first-order systems:

| Plot Type | Position | Highlights |
|------------|-----------|-------------|
| Step Response | Top-left | Rise time, settling time, steady-state value |
| Bode Magnitude | Top-right | Gain margin, frequency response |
| Bode Phase | Bottom-right | Phase margin, phase characteristics |
| Nyquist Plot | Bottom-left | Stability margins, critical point |

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Reporting Issues
- Report bugs and feature requests via **GitHub Issues**  
- Include your system information and reproduction steps  

### Development Contributions
```bash
# Fork the repository
git clone https://github.com/your-username/control-systems-visualizer.git

# Create a feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m 'Add amazing feature'

# Push to your branch
git push origin feature/amazing-feature

# Open a Pull Request
```

### Areas for Improvement
- Additional plot types (Root locus, Nichols chart)  
- Support for higher-order systems  
- Export functionality for plots and data  
- Dark mode theme  

---

## 📜 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🔗 Related Projects
- [python-control](https://github.com/python-control/python-control) — Core control systems library  
- [Matplotlib](https://matplotlib.org/) — Professional plotting and visualization  
- [SciPy](https://scipy.org/) — Scientific computing foundation  

---

## 📞 Support
📧 **Email:** krishnabarai160905@gmail.com
🐛 **Issues:** [GitHub Issues](https://github.com/HeroicKrishna160905/control-systems-visualizer/issues)  
💬 **Discussions:** [GitHub Discussions](https://github.com/HeroicKrishna160905/control-systems-visualizer/discussions)

---

<div align="center">

### 🎓 Perfect for students, educators, and engineers in control systems engineering  
**"Visualize the theory, master the practice."**

</div>
