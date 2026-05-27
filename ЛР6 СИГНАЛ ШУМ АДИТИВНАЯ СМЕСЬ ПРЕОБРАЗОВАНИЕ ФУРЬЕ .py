import numpy as np 
import matplotlib.pyplot as plt 

# Параметры для 6 бригады
N = 500  # Длина массива
noise_type = "нормальный"  # Тип шума
noise_param1 = 2  # Математическое ожидание для нормального шума
noise_param2 = 2  # СКО для нормального шума
num_sinusoids = 4  # Число синусоидальных сигналов
amplitudes = [11, 2, 1, 7]  # Амплитуды
frequencies = [0.5, 0.4, 1.2, 0.8]  # Частоты


min_limit_x = 0
max_limit_x = 2 * np.pi
x = np.linspace(min_limit_x, max_limit_x, N)


useful_signal = np.zeros(N)
for i in range(num_sinusoids):
    useful_signal += amplitudes[i] * np.sin(frequencies[i] * x)


if noise_type == "нормальный":
    noise = np.random.normal(noise_param1, noise_param2, N)
elif noise_type == "равномерный":
    noise = np.random.uniform(noise_param1, noise_param2, N)

mixed_signal = useful_signal + noise


def compute_spectrum(signal):
    """
    Вычисляет комплексный спектр сигнала
    """
    return np.fft.fft(signal)


spectrum_useful = compute_spectrum(useful_signal)
spectrum_noise = compute_spectrum(noise)
spectrum_mixed = compute_spectrum(mixed_signal)


reconstructed_useful = np.fft.ifft(spectrum_useful)
reconstructed_noise = np.fft.ifft(spectrum_noise)
reconstructed_mixed = np.fft.ifft(spectrum_mixed)


plt.figure(figsize=(15, 12))


freqs = np.fft.fftfreq(N, (max_limit_x - min_limit_x) / N)
half = N // 2

plt.subplot(3, 3, 1)
plt.stem(freqs[:half], np.abs(spectrum_useful[:half]) / N, 'b', markerfmt=' ', basefmt=' ')
plt.title('Спектр полезного сигнала')
plt.xlabel('Частота (рад⁻¹)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)
plt.xlim(0, max(frequencies) * 1.5)

plt.subplot(3, 3, 2)
plt.plot(freqs[:half], np.abs(spectrum_noise[:half]) / N, 'r-')
plt.title('Спектр шума')
plt.xlabel('Частота (рад⁻¹)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)
plt.xlim(0, max(frequencies) * 1.5)

plt.subplot(3, 3, 3)
plt.plot(freqs[:half], np.abs(spectrum_mixed[:half]) / N, 'g-')
plt.title('Спектр аддитивной смеси')
plt.xlabel('Частота (рад⁻¹)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)
plt.xlim(0, max(frequencies) * 1.5)


plt.subplot(3, 3, 4)
plt.plot(x, useful_signal, 'b-', linewidth=1.5)
plt.title('Исходный полезный сигнал')
plt.xlabel('x (радианы)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)

plt.subplot(3, 3, 5)
plt.plot(x, noise, 'r-', linewidth=1)
plt.title('Исходный шум')
plt.xlabel('x (радианы)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)

plt.subplot(3, 3, 6)
plt.plot(x, mixed_signal, 'g-', linewidth=1.5)
plt.title('Исходная аддитивная смесь')
plt.xlabel('x (радианы)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)


plt.subplot(3, 3, 7)
plt.plot(x, reconstructed_useful.real, 'b--', linewidth=1.5)
plt.title('Восстановленный полезный сигнал (обратное БПФ)')
plt.xlabel('x (радианы)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)

plt.subplot(3, 3, 8)
plt.plot(x, reconstructed_noise.real, 'r--', linewidth=1.5)
plt.title('Восстановленный шум (обратное БПФ)')
plt.xlabel('x (радианы)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)

plt.subplot(3, 3, 9)
plt.plot(x, reconstructed_mixed.real, 'g--', linewidth=1.5)
plt.title('Восстановленная смесь (обратное БПФ)')
plt.xlabel('x (радианы)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

