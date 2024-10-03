import pygame
import time
import ctypes

# Función para ocultar la ventana de la consola
def hide_console():
    ctypes.windll.kernel32.SetConsoleTitleW("")
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE

# Inicializar el mixer de pygame
pygame.mixer.init()

# Cargar el archivo de sonido
sonido = pygame.mixer.Sound("a.mp3")

# Ocultar la ventana de la consola
hide_console()

# Reproducir el sonido indefinidamente
while True:
    sonido.play()
    while pygame.mixer.get_busy():
        time.sleep(1)
