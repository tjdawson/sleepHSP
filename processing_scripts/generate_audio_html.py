sound_url_prefix = "http://www.sas.upenn.edu/~tjdawson/Experiments/sleepHSP/followup/sounds/"
sound_url_affix = "_doubled.mp3"

test = "3401"

bist = "bist"

blime = "blime"

doon = "doon"

geck = "geck"

jair = "jair"

mipen = "mipen"

tace = "tace"

telpen = "telpen"

tiz = "tiz"

tula = "tula"

vash = "vash"

zant = "zant"

mp3_list = [bist, blime, doon, geck, jair, mipen, tace, telpen, tiz, tula, vash, zant, test]
mp3_list = [[x,"{}{}{}".format(sound_url_prefix,x,sound_url_affix)] for x in mp3_list]

for mp3 in mp3_list:

    audio_html = "<div align=\"center\"> \n" \
                 "\t<audio controls> \n" \
                 "\t\t<p>{}</p> \n" \
                 "\t\t<source src=\"{}\" type=\"audio/wav\"> \n" \
                 "\t\tYour browser does not support the audio element.\n" \
                 "\t</audio> \n" \
                 "</div>".format(mp3[0], mp3[1])
    print audio_html
