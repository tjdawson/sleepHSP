import csv

shuffle_sequence_begin = "var shuffleSequence = seq(\"intro\", \"intro1\", \"intro2\", \"intro3\", \"sep\", \n"

shuffle_sequence_middleHF = ""
shuffle_sequence_middleHL = ""

shuffle_sequence_end = "\"end\"\n);"

HF_config, HL_config = "U:/Experiments/sleepHSP/processing_scripts/config/HF.csv", \
                       "U:/Experiments/sleepHSP/processing_scripts/config/HL.csv"

with open(HL_config, 'rb+') as HL_config:
    HL_config = csv.reader(HL_config)
    HL_config = list(HL_config)

    for n, line in enumerate(HL_config[1:]):
        for i in range(5):
            shuffle_sequence_middleHL += "\"{}_{}_guess{}\", ".format(line[2].lower(), line[3], i)
        if n != len(HL_config)-2:
            shuffle_sequence_middleHL += "\"sep\","
        shuffle_sequence_middleHL += "\n"
    HL = shuffle_sequence_begin + shuffle_sequence_middleHL + shuffle_sequence_end

    print HL