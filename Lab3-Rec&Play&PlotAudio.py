###     Recording an Audio      ###
# ------ libraries for recording and saving audio -----
# import PyAudio
# import wave

# ------ variables that define the audio format and quality -----
# FRAME_PER_PUFFER = 3200  # chunks number ( 3200 frames )
# FORMAT = PyAudio.paInt16  # format of the audio samples ( 16-bit integer format)
# CHANNELS = 1  # number of audio channels ( mono stream )
# RATE = 16000  # the sampling rate of the audio = 16000 samples per second. (Hz)
# p = PyAudio.PyAudio()  # create object ( instance of PyAudio class )

# ------ opens an audio stream with the specified format, channels, rate, buffer size -----
# stream = p.open(
#     format=FORMAT,
#     channels=CHANNELS,
#     rate=RATE,
#     input=True,
#     frames_per_buffer=FRAME_PER_PUFFER
# )
#
# print("start recording")

# time = 5  # the duration of the recording

# initializes an empty list to store the recorded audio data:
# frames = []

# ("' The for loop records audio data in chunks of size FRAME_PER_PUFFER"
# "for a total of 5 seconds and appends each chunk to the frames list.'")

# for i in range(0, int(RATE / FRAME_PER_PUFFER * time)):
#     data = stream.read(FRAME_PER_PUFFER)
#     frames.append(data)
#
# stream.stop_stream()  # stop the audio stream
# stream.close()  # close the audio stream
# p.terminate()  # terminate the PyAudio instance

# create a new WAV file named “Output.wav” in write mode:
# new_file = wave.open("Output.wav", "wb")
# new_file.setnchannels(CHANNELS)  # set the number of channels in the WAV file to 1
# new_file.setsampwidth(p.get_sample_size(FORMAT))  # set the sample width in bytes based on the specified format
# new_file.setframerate(RATE)  # set the frame rate of the WAV file to 16000 frames per second
# new_file.writeframes(b"".join(frames))  # write the recorded audio data to the WAV file
# new_file.close()  # close the WAV file object

###   Play The Audio    ###

# import winsound

# fileName = "Output.wav"
# winsound.PlaySound(fileName, winsound.SND_FILENAME)


###     Plot Audio      ###

import wave
import matplotlib.pyplot as plt
import numpy

file = wave.open(
    "edited-file.wav", "rb"
)  # read file , (rb) = read binary ( binary mode )
sample_freq = file.getframerate()  # Sample frequency
n_samples = file.getnframes()  # number of samples per time (s)
signal_wave = file.readframes(-1)  # reading audio signal
file.close()  # closing the file

time_of_audio = n_samples / sample_freq  # duration of audio=no. of Sample/SF
# print("Time duration: " + time_of_audio)  # printing the duration

# audio signal is converted to an array of integers
signal_array = numpy.frombuffer(signal_wave, dtype=numpy.int16)

# the time of array is created with start time 0 , end time equal to t_audio
times = numpy.linspace(0, time_of_audio, num=n_samples)

plt.figure(figsize=(10, 5))  # new figure object ( w=10 inch , h=5 inch )
plt.plot(times, times, signal_array)
# plt.plot(869400, 869400)
# plt.plot(1738800, 1738800)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, time_of_audio)  # limits of the x-axis of a plot
plt.show()
