import numpy as np

class Modulator:
    """Класс для модуляции сигналов."""

    def __init__(self, carrier_frequency):
        self.carrier_frequency = carrier_frequency

    def am_modulate(self, signal, time):
        """Амплитудная модуляция (AM)."""
        carrier = np.sin(2 * np.pi * self.carrier_frequency * time)
        return (1 + signal) * carrier

    def fm_modulate(self, signal, time, modulation_index=1.0):
        """Частотная модуляция (FM)."""
        phase = 2 * np.pi * self.carrier_frequency * time + modulation_index * signal
        return np.sin(phase)