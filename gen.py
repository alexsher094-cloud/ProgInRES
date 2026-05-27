import numpy as np

class SignalGenerator:
    """Класс для генерации тестовых сигналов."""

    @staticmethod
    def generate_sine_wave(frequency, duration, sampling_rate=1000):
        """Генерация синусоидального сигнала."""
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        signal = np.sin(2 * np.pi * frequency * t)
        return t, signal

    @staticmethod
    def generate_square_wave(frequency, duration, sampling_rate=1000):
        """Генерация прямоугольного сигнала."""
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        signal = np.sign(np.sin(2 * np.pi * frequency * t))
        return t, signal

    @staticmethod
    def generate_sawtooth_wave(frequency, duration, sampling_rate=1000):
        """Генерация пилообразного сигнала."""
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        signal = 2 * (frequency * t - np.floor(0.5 + frequency * t))
        return t, signal