import winsound
import wave


###    Get File Info   ###
def play():
    fileName = input("Type path of audio file : ")
    winsound.PlaySound(fileName, winsound.SND_FILENAME)
    file = wave.open(fileName, "rb")    # rb : read mode

    print("the number of channels", file.getnchannels())
    print("the width of sample", file.getsampwidth())
    print("the frame rate", file.getframerate())
    print("the number of frames", file.getnframes())
    print("the time of sound", file.getnframes() / file.getframerate())
    print("the params", file.getparams())


###    Write On File   ###
def create():
    fileName = input("Type path of audio file : ")
    saveas = input("Save as (Type path of new audio with new name and extension) : ")
    channels = input("Channels : ")
    sample_w = input("Sample width : ")
    reate = input("Rate : ")
    nframes = input("Frames number : ")

    file = wave.open(fileName, "rb")    # rb : read mode
    frames = file.readframes(-1)
    new_file = wave.open(saveas, "wb")    # wb : write mode
    new_file.setnchannels(channels)
    new_file.setsampwidth(sample_w)
    new_file.setframerate(reate)     # 44100 => 4410 being slow 10X     # 44100 * 2 => 88200 being fast...
    new_file.setnframes(nframes)
    new_file.writeframes(frames)

    print(saveas, " is playing now...")
    winsound.PlaySound(saveas, winsound.SND_FILENAME)
    new_file.close()


option = int(input("Enter '1' to play an audio \n'2' for edit an audio file : "))
if option == 1:
    play()

elif option == 2:
    create()

else:
    print("Retry..")
