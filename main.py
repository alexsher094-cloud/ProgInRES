import numpy as np
from gen import SignalGenerator
from mod import Modulator
from vis import Visualizer

def main():
    # Параметры
    carrier_freq = 50      # Частота несущей, Гц
    signal_freq = 5        # Частота модулирующего сигнала, Гц
    duration = 1           # Длительность, с
    sampling_rate = 1000   # Частота дискретизации, Гц

    
    gen = SignalGenerator()
    time, message_signal = gen.generate_sine_wave(signal_freq, duration, sampling_rate)
    mod = Modulator(carrier_freq)
    am_signal = mod.am_modulate(message_signal, time)
    fm_signal = mod.fm_modulate(message_signal, time)
    viz = Visualizer()
    viz.plot_signal(time, message_signal, title="Modulating Signal (Sine Wave)")
    viz.plot_signal(time, am_signal, title="AM Modulated Signal")
    viz.plot_signal(time, fm_signal, title="FM Modulated Signal")
    noisy_am = viz.add_noise(am_signal, noise_level=0.2)
    viz.plot_signal(time, noisy_am, title="AM Signal with Noise")

    

if __name__ == "__main__":
    main()