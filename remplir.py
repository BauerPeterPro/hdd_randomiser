import ctypes
import os
import random
import string
import time

# Fonction pour obtenir l'espace disque d'une partition
def get_disk_space(letter):
    drive = letter + ':/'
    free_bytes = ctypes.c_ulonglong(0)
    total_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive), ctypes.pointer(free_bytes), ctypes.pointer(total_bytes), None)
    free_space = free_bytes.value
    total_space = total_bytes.value
    used_space = total_space - free_space
    return total_space, used_space, free_space

# Affiche l'espace disque pour chaque partition avec une lettre
partitions = [chr(i) for i in range(65, 91) if os.path.exists(chr(i) + ':/')]
for partition in partitions:
    total, used, free = get_disk_space(partition)
    print(f'{partition}: Total: {total}, Used: {used}, Free: {free}')

# Demande à l'utilisateur de choisir une partition
letter = input("Choisissez une partition (lettre en majuscules) : ").upper()
if letter not in partitions:
    print(f"La partition '{letter}' n'existe pas.")
    exit()

# Crée un fichier de 100 Mo avec des données aléatoires
total, used, free = get_disk_space(letter)

# Complète l'espace restant avec des fichiers de 1Mo, puis 1ko
while free > 0:
    if free >= 1000 * 1024 * 1024:
        file_size = 1000 * 1024 * 1024
        filename = str(int(time.time())) + '.vide'
        file_path = letter + ':/' + filename
        print(f"Fichier de 1000Mo créé: {file_path}")
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))
        total, used, free = get_disk_space(letter)
    elif free >= 100 * 1024 * 1024:
        file_size = 100 * 1024 * 1024
        filename = str(int(time.time())) + '.vide'
        file_path = letter + ':/' + filename
        print(f"Fichier de 100Mo créé: {file_path}")
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))
        total, used, free = get_disk_space(letter)
    elif free >= 1024 * 1024:
        file_size = 1024 * 1024
        filename = str(int(time.time())) + '.vide'
        file_path = letter + ':/' + filename
        print(f"Fichier de 1Mo créé: {file_path}")
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))
        total, used, free = get_disk_space(letter)
    elif free >= 1024:
        file_size = 1000
        filename = str(int(time.time())) + '.vide'
        file_path = letter + ':/' + filename
        print(f"Fichier de 1Ko créé: {file_path}")
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))
        total, used, free = get_disk_space(letter)
