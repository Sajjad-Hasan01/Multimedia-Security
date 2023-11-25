import pyaudio
import wave
import winsound
import matplotlib.pyplot as plt
import numpy

###     Recording an Audio      ###
def rec():
    # ------ variables that define the audio format and quality -----
    # FRAME_PER_PUFFER = 3200      # chunks number ( 3200 frames )
    # FORMAT = pyaudio.paInt16     # format of the audio samples ( 16-bit integer format)
    # CHANNELS = 1                 # number of audio channels ( mono stream )
    # RATE = 16000                 # the sampling rate of the audio = 16000 samples per second. (Hz)
    # p = pyaudio.PyAudio()        # create object ( instance of PyAudio class )

    nframes = int(input("Enter number of frames : "))
    channels = int(input("Enter number of channels : "))
    rate = int(input("Enter sampling rate : "))
    FORMAT = pyaudio.paInt16
    p = pyaudio.PyAudio()
    time = int(input("Enter the duration of the recording (in seconds) : "))
    saveas = input("Type path of new audio (with new name and extension) : ")

    # ------ opens an audio stream with the specified format, channels, rate, buffer size -----
    stream = p.open(
        format = FORMAT,
        channels = channels,
        rate = rate,
        input = True,
        frames_per_buffer = nframes
    )

    print("start recording...")

    # initializes an empty list to store the recorded audio data:
    frames = []

    #The for loop records audio data in chunks of size FRAME_PER_PUFFER. for a total of 5 seconds and appends each chunk to the frames list.

    for i in range(0, int(rate / nframes * time)):
        data = stream.read(nframes)
        frames.append(data)

    stream.stop_stream()  # stop the audio stream
    stream.close()        # close the audio stream
    p.terminate()         # terminate the PyAudio instance

    # create a new WAV file named "Output.wav" in write mode:
    new_file = wave.open(saveas, "wb")
    new_file.setnchannels(channels)                     # set the number of channels in the WAV file to 1
    new_file.setsampwidth(p.get_sample_size(FORMAT))    # set the sample width in bytes based on the specified format
    new_file.setframerate(rate)                         # set the frame rate of the WAV file to 16000 frames per second
    new_file.writeframes(b"".join(frames))              # write the recorded audio data to the WAV file
    new_file.close()                                    # close the WAV file object


###   Play The Audio    ###
def play():
    fileName = input("Type path of audio file : ")
    winsound.PlaySound(fileName, winsound.SND_FILENAME)

    file = wave.open(fileName, "rb")
    sample_freq = file.getframerate()
    n_samples = file.getnframes()
    time_of_audio = n_samples / sample_freq
    print("Time duration: ", time_of_audio)


###     Plot Audio      ###
def plot():
    fileName = input("Type path of audio file : ")
    file = wave.open(fileName, "rb")    # read file , (rb) = read binary ( binary mode )
    sample_freq = file.getframerate()         # Sample frequency
    n_samples = file.getnframes()             # number of samples per time (s)
    signal_wave = file.readframes(-1)         # reading audio signal
    file.close()                              # closing the file

    time_of_audio = n_samples / sample_freq   # duration of audio=no. of Sample/SF
    print("Time duration: ", time_of_audio)  # printing the duration

    # audio signal is converted to an array of integers
    signal_array = numpy.frombuffer(signal_wave, dtype=numpy.int16)

    # the time of array is created with start time 0 , end time equal to t_audio
    times = numpy.linspace(0, time_of_audio, num=n_samples)

    plt.figure(figsize=(10, 5))  # new figure object ( w=10 inch , h=5 inch )
    plt.plot(times, signal_array)
    plt.title("Audio Signal")
    plt.ylabel("Signal wave")
    plt.xlabel("Time (s)")
    plt.xlim(0, time_of_audio)  # limits of the x-axis of a plot
    plt.show()


option = int(input("Enter '1' for record new audio \n'2' for play an audio \n'3' for display audio graph : "))
if option == 1:
    rec()

elif option == 2:
    play()

elif option == 3:
    plot()

else:
    print("Retry..")
