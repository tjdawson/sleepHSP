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
mp3_dict = {x:"{}{}{}".format(sound_url_prefix,x,sound_url_affix) for x in mp3_list}
for x, u in mp3_list.iteritems():
    print x, u
    print "\n"