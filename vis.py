import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    """Класс для визуализации сигналов."""

    @staticmethod
    def plot_signal(time, signal, title="Signal"):
        """Отображение сигнала на графике."""
        plt.figure()
        plt.plot(time, signal)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()



    @staticmethod
    def add_noise(signal, noise_level=0.1):
        """Добавление гауссовского шума к сигналу."""
        noise = np.random.normal(0, noise_level, len(signal))
        return signal + noise