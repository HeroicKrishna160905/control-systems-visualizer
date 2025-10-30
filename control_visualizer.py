import numpy as np
import matplotlib.pyplot as plt
import control
import tkinter as tk
from tkinter import messagebox

def make_system(K, tau):
    """First-order system: K / (τs + 1)"""
    s = control.TransferFunction.s
    return K / (tau * s + 1)

def visualize(K, tau):
    """Draw all control system plots."""
    plt.close('all')
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f"System Visualization (K={K}, τ={tau})", fontsize=14)

    # Transfer functions
    P = make_system(K, tau)
    L = P
    CL = control.feedback(L, 1)

    # Step Response
    t, y = control.step_response(CL)
    axs[0, 0].plot(t, y, lw=2)
    axs[0, 0].set_title("Closed-Loop Step Response")
    axs[0, 0].set_xlabel("Time (s)")
    axs[0, 0].set_ylabel("Amplitude")
    axs[0, 0].grid(True)

    # Bode Plot
    omega = np.logspace(-2, 2, 1000)
    mag, phase, omega = control.bode(L, omega, plot=False)
    axs[0, 1].semilogx(omega, 20 * np.log10(np.maximum(mag, 1e-20)))
    axs[0, 1].set_title("Bode Magnitude (Open-Loop)")
    axs[0, 1].set_ylabel("Magnitude (dB)")
    axs[0, 1].grid(True, which="both")

    axs[1, 1].semilogx(omega, np.degrees(phase))
    axs[1, 1].set_title("Bode Phase (Open-Loop)")
    axs[1, 1].set_xlabel("Frequency (rad/s)")
    axs[1, 1].set_ylabel("Phase (deg)")
    axs[1, 1].grid(True, which="both")

    # Nyquist Plot
    complex_resp = mag * np.exp(1j * phase)
    axs[1, 0].plot(np.real(complex_resp), np.imag(complex_resp), lw=1.5)
    axs[1, 0].plot(np.real(complex_resp), -np.imag(complex_resp), lw=0.8, ls="--")
    axs[1, 0].plot([-1], [0], "rx", markersize=8)
    axs[1, 0].set_title("Nyquist (Open-Loop)")
    axs[1, 0].set_xlabel("Re")
    axs[1, 0].set_ylabel("Im")
    axs[1, 0].axis("equal")
    axs[1, 0].grid(True)

    plt.tight_layout()
    plt.show()

def on_generate():
    try:
        K = float(k_entry.get())
        tau = float(tau_entry.get())
        if K <= 0 or tau <= 0:
            raise ValueError
        visualize(K, tau)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter positive numeric values for K and τ.")

# -------------------- Tkinter GUI --------------------
root = tk.Tk()
root.title("Control System Visualizer")
root.geometry("360x220")

tk.Label(root, text="Enter System Gain (K):", font=("Segoe UI", 10)).pack(pady=5)
k_entry = tk.Entry(root, font=("Segoe UI", 10))
k_entry.insert(0, "2")
k_entry.pack()

tk.Label(root, text="Enter Time Constant (τ):", font=("Segoe UI", 10)).pack(pady=5)
tau_entry = tk.Entry(root, font=("Segoe UI", 10))
tau_entry.insert(0, "1")
tau_entry.pack()

tk.Button(root, text="Generate Plots", command=on_generate, font=("Segoe UI", 10), bg="#4CAF50", fg="white").pack(pady=15)

root.mainloop()

