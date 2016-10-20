from collections import defaultdict
import csv
import errno
import itertools
from nltk import WordNetLemmatizer
from operator import itemgetter
import os
import random
import re
import shutil

results = 'U:/Experiments/sleepHSP/results/results.csv'

dir_prefix = "U:/Experiments/sleepHSP followup/followups"
test_id = 'test'
output_file = 'U:/Experiments/sleepHSP followup/followups/{}/'.format(test_id)
dir_prefix = dir_prefix + "/" + test_id + "/"
main_dir = dir_prefix
skeleton_dir_prefix = "U:/Experiments/sleepHSP followup/sleepHSPfollowup/"


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


def random_dict_value(input_dict, value_index, check_value):
    random_value = random.choice(input_dict.values())[value_index]

    if random_value != check_value:
        return random_value

    return random_dict_value(input_dict, value_index, check_value)


def generate_followup_js(pt2_dict, shuffle_sequence, dir_prefix):
    output = "var manualSendResults = true; \n"

    output += shuffle_sequence + "\n\n" + generate_defaults() + "\n\n" + generate_part2_items(pt2_dict)
    with open('{}/data_includes/experiment.js'.format(dir_prefix), 'wb+') as experiment_js:
        experiment_js.write(output)


def generate_defaults():
    return "var defaults = [\n\
        \"Separator\", {\n\
            transfer: \"keypress\",\n\
            normalMessage: \"Press any key to continue.\",\n\
            errorMessage: \"Press any key to continue.\"\n\
        },\n\
        \"DashedSentence\", {\n\
            mode: \"self-paced reading\"\n\
        },\n\
        \"AcceptabilityJudgment\", {\n\
            as: [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\"],\n\
            presentAsScale: true,\n\
            instructions: \"Use number keys or click boxes to answer.\",\n\
            leftComment: \"(Bad)\", rightComment: \"(Good)\"\n\
        },\n\
        \"Question\", {\n\
            hasCorrect: true\n\
        },\n\
        \"Message\", {\n\
            hideProgressBar: true\n\
        },\n\
        \"Form\", {\n\
            hideProgressBar: false,\n\
            continueOnReturn: true,\n\
            saveReactionTime: false\n\
        }\n\
    ];"


def generate_part2_dict(ibex_data, unique_id):
    """Given an ibex results file, returns a dictionary of the following format --
    mystery word: [target, highest rated guess, lowest rated guess]"""
    lemmy = WordNetLemmatizer()
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

        previous_line = ['', '', '', '', '', '', '', '', '']
        trial_identifier = 5
        mystery_word, target_word, guess, confidence = 0, 1, 2, 2

        for current_line in ibex_data:
            # print "Current line:" + str(current_line)

            if current_line[trial_identifier] == previous_line[trial_identifier]:
                # print "match"
                current_line_info = current_line[trial_identifier].split("_")
                previous_line_info = previous_line[trial_identifier].split("_")

                if (current_line_info[target_word], current_line_info[mystery_word]) not in subj_dict:
                    subj_dict[(current_line_info[target_word], current_line_info[mystery_word])] = [
                        (previous_line[8], current_line[8])]
                else:
                    if (current_line_info[target_word], current_line_info[mystery_word]) in subj_dict:
                        subj_dict[(current_line_info[target_word], current_line_info[mystery_word])] += [
                            (previous_line[8], current_line[8])]

            previous_line = current_line

        if len(subj_dict) != 12:
            raise ValueError("ERROR: subj_dict does not equal 12. Check input results file")

        part_2_dict = defaultdict(list)

        for target_w_mystery_w, g_c_list in subj_dict.iteritems():

            g_c_reversed = reversed(g_c_list)
            g_c_reversed = list(g_c_reversed)
            guesses = []

            for gc in g_c_reversed:
                lemmatized_guess = lemmy.lemmatize(gc[0].strip().decode('unicode_escape').encode('ascii', 'ignore'),
                                                   pos='n')
                lemmatized_guess = lemmatized_guess.encode('utf-8')
                if lemmatized_guess == 'horsey':
                    lemmatized_guess = 'horse'
                guesses.append((lemmatized_guess, gc[1]))
            guesses = [gc for gc in guesses if gc[0] != target_w_mystery_w[0]]
            highest_incorrect = max(guesses, key=itemgetter(1))[0]
            lowest_incorrect = min(guesses, key=itemgetter(1))[0]
            # print "Mystery: {}\nTarget: {}\nHighest-rated: {}\nLowest-rated: {}".format(target_w_mystery_w[1],
            #                                                                             target_w_mystery_w[0],
            #                                                                             highest_incorrect,
            #                                                                             lowest_incorrect)

            part_2_dict[target_w_mystery_w[1]] = [target_w_mystery_w[0], highest_incorrect, lowest_incorrect]
        return part_2_dict


def gen_part2_shuffle_sequence(pt2_dict):
    """Input: the dict from part 2
    output: shuffle sequence as a string; list of words to generate forms"""
    shuffle_sequence_begin = "var shuffleSequence = seq(\"intro\", \"intro1\", \"sep\", \n"
    shuffle_sequence_middle = ""
    shuffle_sequence_end = "\"outro1\",\"sr\",\"outro2\",\n);"
    sep = "\"sep\",\n"

    to_add_to_middle = []

    for k, v in pt2_dict.iteritems():
        target = "test_{}_{}_target".format(k, v[0])
        highest = "test_{}_{}_highest".format(k, v[1])
        lowest = "test_{}_{}_lowest".format(k, v[2])
        random_distractor = random_dict_value(pt2_dict, 1, v[1])
        random_distractor = "test_{}_{}_distractor".format(k, random_distractor)

        to_add_to_middle.extend((target, highest, lowest, random_distractor))

    forms_list = [x for x in to_add_to_middle]
    random.shuffle(to_add_to_middle)

    for e in to_add_to_middle[:-1]:
        shuffle_sequence_middle += "\"{}\",{}".format(e, sep)

    shuffle_sequence_middle += "{}".format(to_add_to_middle[-1])

    return [shuffle_sequence_begin + shuffle_sequence_middle + shuffle_sequence_end, forms_list]


def generate_part2_forms(words_list):
    output = ""
    for word in words_list:
        guess = "[\"%s\", \"Form\", { \nhtml: {include: \"%s.html\"} \n}]," % (word, word)
        output += guess + "\n\n"

    return output


def generate_part2_items(words_list):
    output = ""
    begin = "var items = [    [\"sr\", \"__SendResults__\", { }],\n"\
        "[\"sep\", \"Separator\", { }],\n\
        \n\
        //\n\
        \n\
        [\"intro\", \"Form\", {\n\
            html: {include: \"intro.html\"},\n\
            hideProgressBar: true,\n\
            countsForProgressBar: false\n\
        \n\
        }],\n\
        \n\
        //\n\
        \n\
        [\"intro1\", \"Form\", {\n\
            html: {include: \"intro1.html\"},\n\
            hideProgressBar: true,\n\
            countsForProgressBar: false\n\
    validators: {\n\
    audiotest: function(s)\n\
    { if (s == \"3401\")\n\
    return true; else return \"Incorrect entry for \u2018test numbers\u2019\";}\n\
    }\n\
        \n\
        }],\n\
        \n\
        //\n\
        \n\
        [\"outro1\", \"Form\", {\n\
            html: {include: \"outro1.html\"},\n\
            hideProgressBar: true,\n\
            countsForProgressBar: false\n\
        \n\
        }],\n\
        \n\
        //\n\
        \n\
        [\"outro2\", \"Form\", {\n\
            html: { include: \"outro2.html\" },\n\
            hideProgressBar: true,\n\
            countsForProgressBar: false,\n\
        } ],\n\
        \n\
        //"
    end = "[\"end\", \"Form\", {\n\
            html: {include: \"end.html\"},\n\
            hideProgressBar: true,\n\
            countsForProgressBar: false\n\
        \n\
        }]\n\
    ];"
    output += begin + "\n" + generate_part2_forms(words_list) + end
    return output


def generate_part2_html(words_list, dir_prefix):
    fnames = ["{}.html".format(word) for word in words_list]
    sound_url_prefix = "http://www.sas.upenn.edu/~tjdawson/Experiments/sleepHSP/followup/sounds/"
    sound_url_affix = "_doubled.mp3"
    for fname in fnames:
        print fname
        split_fname = fname.split("_")
        mystery, test_word = split_fname[1], split_fname[2]
        src = sound_url_prefix + mystery + sound_url_affix
        audio_html = "<style>\n\
    label {\n\
        display: inline-block;\n\
        margin-bottom: 8px;\n\
    }\n\
    a.left {\n\
        padding-right: 5px;\n\
    }\n\
    a.right {\n\
        padding-left: 5px;\n\
    }\n\
</style>\n\
<div align=\"center\"> \n" \
                     "\t<audio id=\"myaudio\"> \n" \
                     "\t\t<source src=\"%s\" type=\"audio/wav\"> \n" \
                     "\t\tYour browser does not support the audio element.\n" \
                     "\t</audio> \n" \
                     "\t\t<div id=\"questionDiv\" style=\"visibility: hidden;\"><table cellpadding=\"10\" cellspacing=\"4\">\n\
<tr>\n\
  <td>Does %s mean %s?<br>\n\
</tr>\n\
<tr class=\"bordered\">\n\
    <td>\n        " \
                     "<label for=\"yes\"><input type=\"radio\" id=\"yes\" name=\"yes_or_no\" value=\"Yes\" class=\"obligatory\"><span>Yes</span></label>\n" \
                     "<label for=\"no\"><input type=\"radio\" id=\"no\" name=\"yes_or_no\" value=\"No\"><span>No</span></label>\n" \
                     "</td>\n\
</tr>" \
                     "<tr class=\"bordered\">\n\
    <td>\n\
        <a class=\"left\">Not at all confident</a>\n\
        <label for=\"conf1\"><input type=\"radio\" id=\"conf1\" name=\"confidence\" value=\"1\" class=\"obligatory\"><span>1</span></label>\n\
        <label for=\"conf2\"><input type=\"radio\" id=\"conf2\" name=\"confidence\" value=\"2\"><span>2</span></label>\n\
        <label for=\"conf3\"><input type=\"radio\" id=\"conf3\" name=\"confidence\" value=\"3\"><span>3</span></label>\n\
        <label for=\"conf4\"><input type=\"radio\" id=\"conf4\" name=\"confidence\" value=\"4\"><span>4</span></label>\n\
        <label for=\"conf5\"><input type=\"radio\" id=\"conf5\" name=\"confidence\" value=\"5\"><span>5</span></label>\n\
        <a class=\"right\">Very confident </a>\n\
    </td>\n\
</tr>\n\n\
\n\
\n\
</table>\n" \
                     "</div>\n" \
                     "<script type=\"text/javascript\">\n\
  var audio = document.getElementById(\'myaudio\');\n\
   audio.addEventListener(\"ended\", function() {\n\
   document.getElementById(\"questionDiv\").style.visibility = \"visible\";\n\
   audio.currentTime = 0;\n\
});     \n\
audio.play();\n\
</script>" % (src, mystery.upper(), test_word.upper())
        # print audio_html + "\n\n\n"
        with open("{}/chunk_includes/{}".format(dir_prefix, fname), 'wb+') as html:
            html.write(audio_html)


def generate_part2(results, subj_id, dir_prefix):
    part2_dict = generate_part2_dict(results, subj_id)
    shuffle_and_wordlist = gen_part2_shuffle_sequence(part2_dict)
    generate_part2_html(shuffle_and_wordlist[1], dir_prefix)
    generate_followup_js(part2_dict, shuffle_and_wordlist[0], dir_prefix)



AMPMHFa_m001results = "U:/Experiments/sleepHSP followup/followups/AMPMHFa_m001/results.csv"
AMPMHFa_m001prefix = "U:/Experiments/sleepHSP followup/followups/AMPMHFa_m001/"
# AMPMHFa_m002results = "U:/Experiments/sleepHSP followup/followups/AMPMHFa_m002/results.csv"
generate_part2(AMPMHFa_m001results, "AMPMHFa_m001", AMPMHFa_m001prefix)

# PMAMHFb_m001results = "U:/Experiments/sleepHSP followup/followups/PMAMHFb_m001/results.csv"
# PMAMHFb_m004results = "U:/Experiments/sleepHSP followup/followups/PMAMHFb_m004/results.csv"
# PMAMHFb_m005results = "U:/Experiments/sleepHSP followup/followups/PMAMHFb_m005/results.csv"
#
# PMAMHFb_m001prefix = "U:/Experiments/sleepHSP followup/followups/PMAMHFb_m001/"
# PMAMHFb_m004prefix = "U:/Experiments/sleepHSP followup/followups/PMAMHFb_m004/"
# PMAMHFb_m005prefix = "U:/Experiments/sleepHSP followup/followups/PMAMHFb_m005/"
#
# PMAMHFb_m001 = "PMAMHFb_m001"
# PMAMHFb_m004 = "PMAMHFb_m004"
# PMAMHFb_m005 = "PMAMHFb_m005"
#
# generate_part2(PMAMHFb_m001results, PMAMHFb_m001, PMAMHFb_m001prefix)
# generate_part2(PMAMHFb_m004results, PMAMHFb_m004, PMAMHFb_m004prefix)
# generate_part2(PMAMHFb_m005results, PMAMHFb_m005, PMAMHFb_m005prefix)
