tula = ['tula',"https://upenn.box.com/shared/static/arwlug5ut8q0oqjyzqw2jgojsilbb8by.wav"]

vash = ['vash',"https://upenn.box.com/shared/static/7vf20edesh09vhpu0gvsmwad10rh8w1g.wav"]

zant = ['zant',"https://upenn.box.com/shared/static/0m1fbrf3mbxye03u51hkt7068yzt97f9.wav"]

bist = ['bist',"https://upenn.box.com/shared/static/6iy4bryf47tfbnezw99up11nyct0pc1n.wav"]

blime = ['blime',"https://upenn.box.com/shared/static/rjxbpmsx3c0bvsv70d7tvzzm5qkga75w.wav"]

doon = ['doon',"https://upenn.box.com/shared/static/fqealhm7q2yjf30r8bnplkgaig02un92.wav"]

geck = ['geck',"https://upenn.box.com/shared/static/feiw0gciwv9la1dn8eua246s3tetjnqa.wav"]

jair = ['jair',"https://upenn.box.com/shared/static/t23mlw61gcj87nd284qgbt1pljxyxw67.wav"]

mipen = ['mipen',"https://upenn.box.com/shared/static/abiqfpvizk2cw3wx2jac1x1ng1t3bia5.wav"]

tace = ['tace',"https://upenn.box.com/shared/static/lbdk700uiok9ksaspjubxdx4tr99duyr.wav"]

telpen = ['telpen',"https://upenn.box.com/shared/static/iwftdmu55c7zl8j5mhvt6d7exhphzgb9.wav"]

tiz = ['tiz',"https://upenn.box.com/shared/static/pvd098eua5f22407esf75k20hk12pn9f.wav"]

sounds = [bist,blime,doon,geck,jair,mipen,tace,telpen,tiz,tula,vash,zant]

for sound in sounds:

    audio_html = "<div align=\"center\"> \n" \
                 "\t<audio controls> \n" \
                 "\t\t<p>{}</p> \n" \
                 "\t\t<source src=\"{}\" type=\"audio/wav\"> \n" \
                 "\t\tYour browser does not support the audio element.\n" \
                 "\t</audio> \n" \
                 "</div>".format(sound[0],sound[1])
    print audio_html
