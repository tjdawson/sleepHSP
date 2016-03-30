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
output_file = 'U'


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

    mp3_list = [bist, blime, doon, geck, jair, mipen, tace, telpen, tiz, tula, vash, zant, test]
    mp3_dict = {x: "{}{}{}".format(sound_url_prefix, x, sound_url_affix) for x in mp3_list}
    return mp3_dict


mp3_dict = create_mp3_dict()

dir_prefix = "U:/Experiments/sleepHSP followup/followups"
unique_id = raw_input("Enter the participant's unique ID: ")
dir_prefix = dir_prefix + "/" + unique_id + "/"
main_dir = dir_prefix
skeleton_dir_prefix = "U:/Experiments/sleepHSP followup/sleepHSPfollowup/"
output_js = 'U:/Experiments/sleepHSP followup/followups/{}/js_includes/experiment.js'.format(unique_id)
output_word_test_html = 'U:/Experiments/sleepHSP followup/followups/{}/chunk_includes/word_test.html'.format(unique_id)

dirs_to_create = ["js_includes", "chunk_includes", "css_includes", "data_includes"]

make_sure_dir_exists(main_dir)

for directory in dirs_to_create:
    copy(skeleton_dir_prefix + directory, main_dir + directory)

with open(ibex_data, 'rb+') as ibex_data:
    ibex_data = csv.reader(filter(lambda data_row: data_row[0] != '#', ibex_data))
    ibex_data = list(ibex_data)
    # subj = 0
    mystery_word = 3
    target_word = 4
    trial = 6
    g, c = 8, 8
    guesses = []
    confidence_ratings = []

    subj_dict = {}
    count = 0

    for line in ibex_data:

        if line[5] == 'intro3':
            if line[7] == 'subject_id':
                subj = line[8]
                condition = line[8][:8]
            elif line[7] == 'age':
                age = line[8]
            elif line[7] == 'sex':
                sex = line[8]

        if line[5] == 'end':
            pass

        else:
            for e in [line[g1], line[g2], line[g3], line[g4], line[g5]]:
                e = e.strip()

            if (line[subj], line[condition]) not in subj_dict:
                subj_dict[(line[subj], line[condition])] = {(line[target_word], line[mystery_word]):
                                                                [[(line[g1], line[c1]),
                                                                  (line[g2], line[c2]),
                                                                  (line[g3], line[c3]),
                                                                  (line[g4], line[c4]),
                                                                  (line[g5], line[c5])]]}
            else:
                if (line[target_word], line[mystery_word]) in subj_dict[(line[subj], line[condition])]:
                    subj_dict[(line[subj], line[condition])][(line[target_word], line[mystery_word])] += \
                        [[(line[g1], line[c1]),
                          (line[g2], line[c2]),
                          (line[g3], line[c3]),
                          (line[g4], line[c4]),
                          (line[g5], line[c5])]]
                else:
                    subj_dict[(line[subj], line[condition])][(line[target_word], line[mystery_word])] = \
                        [[(line[g1], line[c1]),
                          (line[g2], line[c2]),
                          (line[g3], line[c3]),
                          (line[g4], line[c4]),
                          (line[g5], line[c5])]]

print subj_dict

# with open(output_file, 'wb+') as output_file:
#     output_file = csv.writer(output_file)
#     output_file.writerow(['Subject', 'Condition', 'Mystery Word', 'Target Word', 'Highest-rated incorrect guess', 'Lowest-rated incorrect guess', 'All non-target guesses (most recent first)'])
#
#     for_tts = set()
#
#     for k,v in subj_dict.iteritems():
#         subj_number = k[0]
#         subj_condition = k[1]
#         print "Subject {}, Condition {}:".format(subj_number, subj_condition)
#         for t_word_m_word, g_c_list in v.iteritems():
#             target = t_word_m_word[0]
#             mystery = t_word_m_word[1]
#
#             guesses = []
#
#             reverse_list = reversed(g_c_list)
#             for gc in reverse_list:
#                 gc = reversed(gc)
#                 for guess in gc:
#                     lemmatized_guess = lemmy.lemmatize(guess[0].decode('unicode_escape').encode('ascii','ignore'), pos='n')
#                     lemmatized_guess = lemmatized_guess.encode('utf-8')
#                     if lemmatized_guess == 'horsey':
#                         lemmatized_guess = 'horse'
#                     guesses.append((lemmatized_guess, guess[1]))
#             # guesses = [guess for guess in guesses if guess != ('', '')]
#             # guesses = [guess for guess in guesses if guess != ('-', '-')]
#             # guesses = [guess for guess in guesses if guess[0] != '']
#             # guesses = [guess for guess in guesses if guess[1] != '']
#             guesses = [guess for guess in guesses if guess[0].strip() != target and guess[0] != '' and guess[1].isdigit() == True]
#
#             highest_incorrect = max(guesses, key=itemgetter(1))[0]
#             lowest_incorrect = min(guesses, key=itemgetter(1))[0]
#
#             print "Mystery Word: {}, Target Word: {}\nLowest incorrect guess: {}\nHighest incorrect guess: {}".format(mystery, target, lowest_incorrect, highest_incorrect)
#
#             for_tts.add(("Does {} mean {}?".format(mystery, target), "{}_{}".format(mystery, target)))
#             for_tts.add(("Does {} mean {}?".format(mystery, highest_incorrect), "{}_{}".format(mystery, highest_incorrect)))
#             for_tts.add(("Does {} mean {}?".format(mystery, lowest_incorrect), "{}_{}".format(mystery, lowest_incorrect)))
#
#             print "Guesses (most recent first): " + str(guesses)
#             print '\n'
#
#             row = [subj_number, subj_condition, mystery, target, highest_incorrect, lowest_incorrect, str(guesses)]
#             output_file.writerow(row)
