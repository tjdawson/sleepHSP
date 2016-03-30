from pydub import AudioSegment

prefix = "U:/Experiments/sleepHSP/video_presentation/VideoFileFolder/"
affix = ".wav"

files_to_double = ["bist", "blime", "doon", "geck", "jair", "mipen", "tace", "telpen", "tiz", "tula", "vash", "zant"]

for filename in files_to_double:
    file = AudioSegment.from_wav("{}{}{}".format(prefix, filename, affix))
    pause = AudioSegment.silent(duration=1500)
    file_doubled = file+pause+file
    file_doubled.export("{}{}{}{}".format(prefix, filename, "_doubled", ".mp3"), format="mp3")
    print file_doubled.duration_seconds