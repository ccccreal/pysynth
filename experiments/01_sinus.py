import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

SAMPLE_RATE = 48_000   # Samples pro Sekunde
FREQ = 440.0           # Hz (Kammerton A)
DURATION = 2.0         # Sekunden
AMPLITUDE = 0.2        # bewusst leise, schont Ohren und Lautsprecher

# TODO 1: Wie viele Samples brauchst du insgesamt?
n_samples = int(DURATION * SAMPLE_RATE)

# TODO 2: Zeitachse t in Sekunden, ein Wert pro Sample
t = np.arange(n_samples) / SAMPLE_RATE

# TODO 3: Sinus berechnen (Formel: A · sin(2π · f · t))
signal = AMPLITUDE * np.sin(2 * np.pi * FREQ * t)

# Abspielen
sd.play(signal, SAMPLE_RATE)
sd.wait()  # wartet, bis der Ton fertig ist

# TODO 4: Die ersten 500 Samples plotten
# x-Achse in Millisekunden ist schöner als Sample-Index
N_PLOT = 500
fig = plt.figure()
ax = fig.gca()
ax.plot(t[:N_PLOT] * 1000, signal[:N_PLOT])
ax.set_title(f'Sinus {FREQ:.0f} Hz, erste {N_PLOT} Samples')
ax.set_xlabel('t [ms]')
ax.set_ylabel('Amplitude')
ax.grid(True)
plt.tight_layout()
plt.show()