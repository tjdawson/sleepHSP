import csv
import errno
import itertools
from nltk import WordNetLemmatizer
from operator import itemgetter
import os
import random
import re
import shutil

lemmy = WordNetLemmatizer()

ibex_data = 'U:/Experiments/sleepHSP/results/results.csv'


def make_sure_dir_exists(dir_path):
    try:
        os.makedirs(dir_path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def copy(src, dest):
    # Copy a file, or recursively copy a directory
    try:
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns('experiment.js'))
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        if e.errno == errno.EEXIST:
            shutil.copy(src, dest)
        else:
            print "Directory not copied. Error: {}".format(e)


def create_mp3_dict():
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

    mp3_list = [bist, blime, doon, geck, jair, mipen, tace, telpen, tiz, tula, vash, zant]
    mp3_dict = {x: "{}{}{}".format(sound_url_prefix, x, sound_url_affix) for x in mp3_list}
    mp3_dict["test"] = "{}{}{}".format(sound_url_prefix, test, sound_url_affix)
    return mp3_dict


mp3_dict = create_mp3_dict()

dir_prefix = "U:/Experiments/sleepHSP followup/followups"
unique_id = raw_input("Enter the participant's unique ID: ")
output_file = 'U:/Experiments/sleepHSP followup/followups/{}/'.format(unique_id)
dir_prefix = dir_prefix + "/" + unique_id + "/"
main_dir = dir_prefix
skeleton_dir_prefix = "U:/Experiments/sleepHSP followup/sleepHSPfollowup/"
# output_js = 'U:/Experiments/sleepHSP followup/followups/{}/js_includes/experiment.js'.format(unique_id)
# output_word_test_html = 'U:/Experiments/sleepHSP followup/followups/{}/chunk_includes/word_test.html'.format(unique_id)

# dirs_to_create = ["js_includes", "chunk_includes", "css_includes", "data_includes"]
#
# make_sure_dir_exists(main_dir)
#
# for directory in dirs_to_create:
#     copy(skeleton_dir_prefix + directory, main_dir + directory)

with open(ibex_data, 'rb+') as ibex_data:
    ibex_data = csv.reader(filter(lambda data_row: data_row[0] != '#', ibex_data))
    ibex_data = list(ibex_data)

    subject_id = unique_id
    subject_age = ibex_data[1][8]
    subject_sex = ibex_data[2][8]

    ibex_data = filter(lambda row: row[5] != 'end', ibex_data)
    ibex_data = filter(lambda row: row[5] != 'intro3', ibex_data)

    subj_dict = {}
    guess_and_confidence = []

    previous_line = ['','','','','','','','','']
    trial_identifier = 5
    mystery_word, target_word, guess, confidence = 0, 1, 2, 2

    for current_line in ibex_data:
        print "Current line:" + str(current_line)

        if current_line[trial_identifier] == previous_line[trial_identifier]:
            print "match"
            current_line_info = current_line[trial_identifier].split("_")
            previous_line_info = previous_line[trial_identifier].split("_")

            if (current_line_info[target_word], current_line_info[mystery_word]) not in subj_dict:
                subj_dict[(current_line_info[target_word], current_line_info[mystery_word])] = [(previous_line[8], current_line[8])]
            else:
                if (current_line_info[target_word], current_line_info[mystery_word]) in subj_dict:
                    subj_dict[(current_line_info[target_word], current_line_info[mystery_word])] += [(previous_line[8], current_line[8])]

        previous_line = current_line

    if len(subj_dict) != 12:
        raise ValueError("ERROR: subj_dict does not equal 12. Check input results file")

    for target_w_mystery_w, g_c_list in subj_dict.iteritems():

        g_c_reversed = reversed(g_c_list)
        g_c_reversed = list(g_c_reversed)
        guesses = []

        for gc in g_c_reversed:
            lemmatized_guess = lemmy.lemmatize(gc[0].strip().decode('unicode_escape').encode('ascii', 'ignore'), pos='n')
            lemmatized_guess = lemmatized_guess.encode('utf-8')
            if lemmatized_guess == 'horsey':
                lemmatized_guess = 'horse'
            guesses.append((lemmatized_guess, gc[1]))
        guesses = [gc for gc in guesses if gc[0] != target_w_mystery_w[0]]
        highest_incorrect = max(guesses, key=itemgetter(1))[0]
        lowest_incorrect = min(guesses, key=itemgetter(1))[0]
        print "Mystery: {}\nTarget: {}\nHighest-rated: {}\nLowest-rated: {}".format(target_w_mystery_w[1], target_w_mystery_w[0], highest_incorrect, lowest_incorrect)

# with open(output_file, 'wb+') as output_file:
