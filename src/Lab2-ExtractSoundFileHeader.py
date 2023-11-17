import winsound
import wave

# file_name = "../assets/audio/sample-file-4.wav"

# winsound.PlaySound(file_name, winsound.SND_FILENAME)

# file = wave.open(file_name, "rb")   # rb : read mode


###    Get File Info   ###
# print("the number of channels", file.getnchannels())
# print("the width of sample", file.getsampwidth())
# print("the frame rate", file.getframerate())
# print("the number of frames", file.getnframes())
# print("the time of sound", file.getnframes() / file.getframerate())
# print("the params", file.getparams())

###    Write On File   ###
# frames = file.readframes(-1)
# new_file = wave.open("../assets/audio/edited-file2.wav", "wb")    # wb : write mode
# new_file.setnchannels(2)
# new_file.setsampwidth(2)
# new_file.setframerate(4410)     # 44100 => 4410 being slow...
# new_file.setnframes(869400)
# new_file.writeframes(frames)
#
# winsound.PlaySound("../assets/audio/edited-file2.wav", winsound.SND_FILENAME)
#
# new_file.close()
###################






file_name = "../assets/audio/edited-file.wav"
file = wave.open(file_name, "rb")
frames = file.readframes(-1)

new_file = wave.open("../assets/audio/edited-file3.wav", "wb")
new_file.setnchannels(2)
new_file.setsampwidth(2)
new_file.setframerate(88200)     # 44100 * 2 => 88200 being fast...
new_file.setnframes(869400)
new_file.writeframes(frames)

print("edited-file3.wav" + " is playing now...")
winsound.PlaySound("../assets/audio/edited-file3.wav", winsound.SND_FILENAME)

new_file.close()






# ---New File After Edit--- #

# new_file_name = "../assets/audio/edited-file.wav"
# print(new_file_name + " is playing now...")
# winsound.PlaySound(new_file_name, winsound.SND_FILENAME)
#
# eFile = wave.open(new_file_name, "rb")
#
# print("the number of channels", eFile.getnchannels())
# print("the width of sample", eFile.getsampwidth())
# print("the frame rate", eFile.getframerate())
# print("the number of frames", eFile.getnframes())
# print("the time of sound", eFile.getnframes() / eFile.getframerate())
# print("the params", eFile.getparams())
