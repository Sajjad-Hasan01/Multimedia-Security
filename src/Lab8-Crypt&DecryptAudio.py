from cryptography.fernet import Fernet
import wave

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, 'rb').read()

def encrypt_audio(audio_path, output_path, key):
    cipher = Fernet(key)

    audio = wave.open(audio_path, 'rb')
    frames = audio.readframes(audio.getnframes)








# Generate and Save encryption key
key = generate_key()
save_key(key, 'encryption_key.key')

# Encrypt audio
encrypt_audio(audio_path, encrypted_path, key)

# Decrypt audio
decrypt_audio(encrypted_path, decrypted_path, key)



#Example
audio_path = 'audio.wav'
