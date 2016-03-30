bist = "bist_horse"

blime = "blime_toy"

doon = "doon_necklace"

geck = "geck_nose"

jair = "jair_time"

mipen = "mipen_bag"

tace = "tace_phone"

telpen = "telpen_ball"

tiz = "tiz_thing"

tula = "tula_mommy"

vash = "vash_shoe"

zant = "zant_book"

word_list = [bist, blime, doon, geck, jair, mipen, tace, telpen, tiz, tula, vash, zant]

for i in range(5):
    for word in word_list:
        if i == 0:
            guess = "[\"%s_guess%s\", \"Form\", { \nhtml: {include: \"guess0.html\"} \n}]," % (word, i)
            print guess + "\n"
        else:
            guess = "[\"%s_guess%s\", \"Form\", { \nhtml: {include: \"guess.html\"} \n}]," % (word, i)
            print guess + "\n"
