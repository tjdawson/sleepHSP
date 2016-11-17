from collections import defaultdict
from copy import deepcopy
import csv
import errno
from nltk import WordNetLemmatizer
import os
import random
import shutil
import subprocess

results = 'U:/Experiments/sleepHSP/results/results.csv'

dir_prefix = "U:/Experiments/sleepHSP followup/followups"
test_id = 'test'
output_file = 'U:/Experiments/sleepHSP followup/followups/{}/'.format(test_id)
dir_prefix = dir_prefix + "/" + test_id + "/"
main_dir = dir_prefix
skeleton_dir_prefix = "U:/Experiments/sleepHSP followup/sleepHSPfollowup/"

# this is a list of frequent english words, we'll choose randomly from this when there aren't enough distractors
frequent_words = []
with open('./frequent_words.TXT','r') as f:
    f = f.read().splitlines()
    for x in f:
        frequent_words.append(x)

# these are correct answers that differ in morphological form from our defined target words
correct_answers = {
    "bag": ["baggie", "baggy"],
    "horse": ["horsey", "horsie"],
    "mommy": ["mom", "mum", "mummy", "ma", "mama", "mamma", "momma", "mammy", "mam", "mother", "mumsy"],
    "nose": ["nosie", "nosy", "nosey"],
    "phone": ["telephone", "telly"],
    "thing": ["thingy", "thingamajig"],
    "dog":  ["doge"]
}


def random_dict_value(input_dict, value_index, check_value):
    frequent_words_list = [x for x in frequent_words if x not in check_value]

    random_value = random.choice(input_dict.values())[value_index]

    if random_value not in check_value:
        return random_value

    try:
        return random_dict_value(input_dict, value_index, check_value)
    except RuntimeError:
        return random.choice(frequent_words_list)


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


def generate_part2_dict(ibex_data, unique_id):
    """Given an ibex results file, returns a dictionary of the following format --
    mystery word: [target, highest rated guess, lowest rated guess]"""
    Lemmy = WordNetLemmatizer()
    with open(ibex_data, 'rb+') as ibex_data:
        ibex_data = csv.reader(filter(lambda data_row: data_row[0] != '#', ibex_data))
        ibex_data = list(ibex_data)

        subject_id = unique_id
        subject_age = ibex_data[1][8]
        subject_sex = ibex_data[2][8]

        ibex_data = filter(lambda row: row[5] != 'end', ibex_data)
        ibex_data = filter(lambda row: row[5] != 'intro3', ibex_data)
        ibex_data = [[x.lower() for x in y] for y in ibex_data]
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

                current_line_info = [x.lower() for x in current_line_info]
                previous_line_info = [x.lower() for x in previous_line_info]

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

        # initialize a new dictionary for tracking some stats about the subject responses
        response_stats = defaultdict(list)

        for target_w_mystery_w, g_c_list in subj_dict.iteritems():

            g_c_reversed = reversed(g_c_list)
            g_c_reversed = list(g_c_reversed)
            guesses = []

            correct_answer_alternate_form = False
            for gc in g_c_reversed:
                lemmatized_guess = Lemmy.lemmatize(gc[0].strip().decode('unicode_escape').encode('ascii', 'ignore'),
                                                   pos='n')
                lemmatized_guess = lemmatized_guess.encode('utf-8')

                for k,v in correct_answers.iteritems():
                    if lemmatized_guess in v:
                        correct_answer_alternate_form = lemmatized_guess
                        lemmatized_guess = k
                guesses.append((lemmatized_guess, gc[1]))

            guesses = [(x[0], int(x[1])) for x in guesses]
            # find if the target word was guessed during learning
            # and, find the highest confidence for that guess
            # and, find the number of times it was guessed
            target_guessed = 0
            target_highest_confidence = 'NA'
            target_n_times_guessed = 'NA'
            if correct_answer_alternate_form:
                target_guessed = 1
                target_highest_confidence = max(x[1] for x in guesses if x[0] == lemmatized_guess)
                target_n_times_guessed = sum(x[0] == lemmatized_guess for x in guesses)
            elif target_w_mystery_w[0] in [x[0] for x in g_c_reversed]:
                target_guessed = 1
                target_highest_confidence = max(x[1] for x in guesses if x[0] == target_w_mystery_w[0])
                target_n_times_guessed = sum(x[0] == target_w_mystery_w[0] for x in guesses)

            response_stats[target_w_mystery_w[0]] = [target_guessed, target_highest_confidence, target_n_times_guessed]

            guesses = [gc for gc in guesses if gc[0] != target_w_mystery_w[0]]

            if not guesses:
                guesses = [(random.choice(frequent_words), random.randint(1, 5)),
                           (random.choice(frequent_words), random.randint(1, 5)),
                           (random.choice(frequent_words), random.randint(1, 5))
                           ]

            highest_confidence = max(x[1] for x in guesses)
            lowest_confidence = min(x[1] for x in guesses)

            highest_guesses = map(lambda x: x if x[1] >= highest_confidence else None, guesses)
            lowest_guesses = map(lambda x: x if x[1] <= lowest_confidence else None, guesses)

            highest_guesses = (x for x in highest_guesses if x is not None)
            lowest_guesses = (x for x in lowest_guesses if x is not None)

            highest_guess = next(highest_guesses, None)
            lowest_guess = next(lowest_guesses, None)

            highest_guess = highest_guess[0]
            lowest_guess = lowest_guess[0]

            if highest_guess == lowest_guess:
                print "high-low match"
                lowest_guess = next(lowest_guesses, None)
                lowest_guess = lowest_guess[0] if type(lowest_guess) is tuple else None

            highest_guessed = 0
            highest_guess_highest_confidence = 'NA'
            highest_guess_n_times_guessed = 'NA'
            lowest_guessed = 0
            lowest_guess_highest_confidence = 'NA'
            lowest_guess_n_times_guessed = 'NA'

            if highest_guess in [x[0] for x in guesses]:
                highest_guessed = 1
                highest_guess_highest_confidence = max(x[1] for x in guesses if x[0] == highest_guess)
                highest_guess_n_times_guessed = sum(x[0] == highest_guess for x in guesses)

            if lowest_guess in [x[0] for x in guesses]:
                lowest_guessed = 1
                lowest_guess_highest_confidence = max(x[1] for x in guesses if x[0] == lowest_guess)
                lowest_guess_n_times_guessed = sum(x[0] == lowest_guess for x in guesses)

            response_stats[highest_guess] = [highest_guessed, highest_guess_highest_confidence, highest_guess_n_times_guessed]
            response_stats[lowest_guess] = [lowest_guessed, lowest_guess_highest_confidence, lowest_guess_n_times_guessed]
            response_stats['distractor'] = [0, 'NA', 'NA']

            target_word = correct_answer_alternate_form if correct_answer_alternate_form else target_w_mystery_w[0]
            part_2_dict[target_w_mystery_w[1]] = [target_word, highest_guess, lowest_guess]
        print subject_id

        return [part_2_dict, response_stats]


def gen_part2_shuffle_sequence(pt2_dict):
    """Input: the dict from part 2
    output: shuffle sequence as a string; list of words to generate forms"""
    shuffle_sequence_begin = "var shuffleSequence = seq(\"intro\", \"intro1\", \"sep\", \n"
    shuffle_sequence_middle = ""
    shuffle_sequence_end = "\"outro1\",\"sr\",\"outro2\"\n);"
    sep = "\"sep\",\n"

    pt2_dict_copy = deepcopy(pt2_dict)
    to_add_to_middle = []
    used_distractors = []
    used_fillers = [None]

    for k, v in pt2_dict.iteritems():
        target = "test_{}_{}_target".format(k, v[0])

        if v[1] is None:
            highest_filler = random_dict_value(pt2_dict_copy, 2, [v[1]]+used_fillers)
            used_fillers.append(highest_filler)
            highest = "test_{}_{}_highest_filler".format(k, highest_filler)
        else:
            highest = "test_{}_{}_highest".format(k, v[1])

        if v[2] is None:
            lowest_filler = random_dict_value(pt2_dict_copy, 2, [v[1]]+used_fillers)
            used_fillers.append(lowest_filler)
            lowest = "test_{}_{}_lowest_filler".format(k, lowest_filler)
        else:
            lowest = "test_{}_{}_lowest".format(k, v[2])

        # Make sure this is picking a target word meaning & that it only chooses that meaning once
        random_distractor = random_dict_value(pt2_dict_copy, 1, [v[1]] + used_distractors)
        used_distractors.append(random_distractor)
        random_distractor = "test_{}_{}_distractor".format(k, random_distractor)

        to_add_to_middle.extend((target, highest, lowest, random_distractor))

    forms_list = [x for x in to_add_to_middle]
    random.shuffle(to_add_to_middle)

    for e in to_add_to_middle[:-1]:
        shuffle_sequence_middle += "\"{}\",{}".format(e, sep)

    shuffle_sequence_middle += "\"{}\",".format(to_add_to_middle[-1])

    return [shuffle_sequence_begin + shuffle_sequence_middle + shuffle_sequence_end, forms_list]


def generate_part2_forms(words_list):
    output = ""
    for word in words_list:
        guess = "[\"%s\", \"Form\", { \nhtml: {include: \"%s.html\"} \n}]," % (word, word)
        output += guess + "\n\n"

    return output


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


def generate_part2_items(pt2_dict):
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
            countsForProgressBar: false,\n\
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
    output += begin + "\n" + generate_part2_forms(pt2_dict) + end
    return output


def generate_part2_html(words_list, dir_prefix, subj_id, subject_responses):
    fnames = ["{}.html".format(word) for word in words_list]
    sound_url_prefix = "http://www.sas.upenn.edu/~tjdawson/Experiments/sleepHSP/followup/sounds/"
    sound_url_affix = "_doubled.mp3"

    sanity_check_exists = os.path.isfile('./sleep_study_all_sanity-check.csv')

    subject_responses = deepcopy(subject_responses)

    with open('./sleep_study_all_sanity-check.csv', 'ab+') as csv_out:
        csv_out = csv.writer(csv_out)
        header = ['Subject', 'Condition', 'Novel_word', 'Probe', 'Probe Type',
                  'Guessed during learning?', 'Highest confidence rating during learning',
                  'Number of times guessed during learning',
                  'Response during test (e.g. response to \'does bist mean horse?\')',
                  'Confidence rating during test']
        if not sanity_check_exists:
            csv_out.writerow(header)
        for fname in fnames:
            fname = fname.split("_")
            subject = subj_id
            condition = 'no_sleep' if 'AMPM' in subject else 'sleep'
            novel_word = fname[1]
            probe = fname[2]
            probe_type = fname[3].split(".")[0]
            if len(fname) > 4:
                probe_type = "_".join([fname[3], fname[4].split(".")[0]])

            if probe_type == 'distractor' or 'filler' in probe_type:
                guessed_during_learning = subject_responses['distractor'][0]
                highest_confidence_during_learning = subject_responses['distractor'][1]
                n_times_guessed_during_learning = subject_responses['distractor'][2]
            else:
                print probe

                for k,v in correct_answers.iteritems():
                    if probe in v:
                        probe = k
                guessed_during_learning = subject_responses[probe][0]
                highest_confidence_during_learning = subject_responses[probe][1]
                n_times_guessed_during_learning = subject_responses[probe][2]

            csv_out.writerow([subject, condition, novel_word, probe, probe_type,
                              guessed_during_learning, highest_confidence_during_learning, n_times_guessed_during_learning])

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


def generate_followup_js(pt2_dict, shuffle, dir_prefix):
    output = "var manualSendResults = true; \n"

    output += shuffle[0] + "\n\n" + generate_defaults() + "\n\n" + generate_part2_items(shuffle[1])
    with open('{}/data_includes/experiment.js'.format(dir_prefix), 'wb+') as experiment_js:
        experiment_js.write(output)


def generate_part2(results, subj_id, dir_prefix):
    part2_dict = generate_part2_dict(results, subj_id) # the second index of this is a dict with stats related to subject responses
    shuffle = gen_part2_shuffle_sequence(part2_dict[0])
    generate_part2_html(shuffle[1], dir_prefix, subj_id, part2_dict[1])
    generate_followup_js(part2_dict, shuffle, dir_prefix)


def process_ibex_results(ibex_csv):
    # given the results csv from Ibex for a condition eg PMAMHFa,
    # split it into csvs for each subject, and create directories to use
    # with the generate_part_2() function
    # then, create all the follow-up surveys.

    data_working_directory = 'C:\\Users\\tjdawson\\Dropbox\\Sleep Study\\HSP survey'

    followups_to_generate = []

    with open(ibex_csv, 'rb+') as ibex_csv:
        ibex_csv = csv.reader(ibex_csv)
        ibex_csv = list(ibex_csv)
        ibex_csv = [r for r in ibex_csv if '#' not in r[0]]

        subject_id = None

        for r in ibex_csv:
            if r[7] == 'subject_id':
                if r[7] != subject_id:
                    subject_id = r[8]
                    subject_dir = '{}\\{}'.format(data_working_directory, subject_id)
                    make_sure_dir_exists(subject_dir)
                    make_sure_dir_exists('{}\\chunk_includes'.format(subject_dir))
                    make_sure_dir_exists('{}\\data_includes'.format(subject_dir))
                    followups_to_generate.append(subject_id)
            with open('{}\\results.csv'.format(subject_dir), 'ab+') as results:
                results = csv.writer(results)
                results.writerow(r)

        print followups_to_generate
        for s in followups_to_generate:
            results = '{}\\{}\\results.csv'.format(data_working_directory,s)
            subject = s
            prefix = '{}\\{}'.format(data_working_directory,s)
            generate_part2(results,subject,prefix)


def github_it(results_dir):
    # this function will create a github branch from
    # the master branch of our sleepHSPfollowup repo
    # ***the branch's name is the subject's unique ID***
    # it copies over the chunk_includes and data_includes
    # directories created by process_ibex_results() to that branch,
    # commits the changes, and publishes the branch
    # finally, it should print a reminder that the user still
    # needs to manually create and sync the followups on the Ibex Farm

    subprocess.check_call(['./commit.sh',results_dir])   # not actually sure yet which method to use for this, or if shell needs to = True
    print "GitHub branch created, ***you must still manually add and sync the Ibex experiment for {}***".format(results_dir.split('/')[-1])

# process_ibex_results('C:\\Users\\tjdawson\\Dropbox\\Sleep Study\\HSP survey\\11 15 2016 AM.csv')
# process_ibex_results('C:\\Users\\tjdawson\\Dropbox\\Sleep Study\\HSP survey\\11 15 2016 PM.csv')
# process_ibex_results('C:\\Users\\tjdawson\\Dropbox\\Sleep Study\\HSP survey\\11 16 2016 AM.csv')
process_ibex_results('C:\\Users\\tjdawson\\Dropbox\\Sleep Study\\HSP survey\\11 17 2016 AM.csv')

### test cases ###

### single guess responses
# single_guess_results = "U:/Experiments/sleepHSP followup/followups/test/test_case_SingleGuess/AMPMHFa_m001/results.csv"
# single_guess_subject = "AMPMHFa_m001"
# single_guess_prefix = "U:/Experiments/sleepHSP followup/followups/test/test_case_SingleGuess/AMPMHFa_m001/"
# generate_part2(single_guess_results, single_guess_subject, single_guess_prefix)

### all correct answers (all responses consistent with target, variable confidence)
# all_correct_results = "U:/Experiments/sleepHSP followup/followups/test/test_case_AllCorrect/AMPMHFa_m001/results.csv"
# all_correct_subject = "AMPMHFa_m001"
# all_correct_prefix = "U:/Experiments/sleepHSP followup/followups/test/test_case_AllCorrect/AMPMHFa_m001/"
# generate_part2(all_correct_results, all_correct_subject, all_correct_prefix)

## results with some high-low ties thrown in
## these are cases where both the highest and lowest confidence guesses were the same
# high_low_tie_results = "U:/Experiments/sleepHSP followup/followups/test/test_case_HighLowTie/AMPMHFa_m001/results.csv"
# high_low_tie_subject = "AMPMHFa_m001"
# high_low_tie_prefix = "U:/Experiments/sleepHSP followup/followups/test/test_case_HighLowTie/AMPMHFa_m001/"
# generate_part2(high_low_tie_results, high_low_tie_subject, high_low_tie_prefix)

### real subject data ###



# 10/13/16
# PMAMHFa_m100results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m100/results.csv"
# PMAMHFa_m101results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m101/results.csv"
# # PMAMHFa_m102results = ""
# PMAMHFa_m103results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m103/results.csv"
# PMAMHFa_m104results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m104/results.csv"
# PMAMHFa_m105results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m105/results.csv"
# PMAMHFa_m106results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m106/results.csv"
# # PMAMHFa_m107results = ""
# PMAMHFa_m108results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m108/results.csv"
#
# PMAMHFa_m100prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m100/"
# PMAMHFa_m101prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m101/"
# PMAMHFa_m103prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m103/"
# PMAMHFa_m104prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m104/"
# PMAMHFa_m105prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m105/"
# PMAMHFa_m106prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m106/"
# PMAMHFa_m108prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m108/"
#
# PMAMHFa_m100 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m100"
# PMAMHFa_m101 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m101"
# PMAMHFa_m103 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m103"
# PMAMHFa_m104 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m104"
# PMAMHFa_m105 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m105"
# PMAMHFa_m106 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m106"
# PMAMHFa_m108 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m108"
#
# generate_part2(PMAMHFa_m100results, PMAMHFa_m100prefix, PMAMHFa_m100)
# generate_part2(PMAMHFa_m101results, PMAMHFa_m101prefix, PMAMHFa_m101)
# generate_part2(PMAMHFa_m103results, PMAMHFa_m103prefix, PMAMHFa_m103)
# generate_part2(PMAMHFa_m104results, PMAMHFa_m104prefix, PMAMHFa_m104)
# generate_part2(PMAMHFa_m105results, PMAMHFa_m105prefix, PMAMHFa_m105)
# generate_part2(PMAMHFa_m106results, PMAMHFa_m106prefix, PMAMHFa_m106)
# generate_part2(PMAMHFa_m108results, PMAMHFa_m108prefix, PMAMHFa_m108)

# 10/18/16
# PMAMHFa_m200results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m200/results.csv"
# PMAMHFa_m200prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m200/"
# PMAMHFa_m200 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m200"
# generate_part2(PMAMHFa_m200results, PMAMHFa_m200prefix, PMAMHFa_m200)

# PMAMHFa_m201results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m201/results.csv"
# PMAMHFa_m201prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m201/"
# PMAMHFa_m201 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m201"
# generate_part2(PMAMHFa_m201results, PMAMHFa_m201prefix, PMAMHFa_m201)

# PMAMHFa_m202results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m202/results.csv"
# PMAMHFa_m202prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m202/"
# PMAMHFa_m202 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m202"
# generate_part2(PMAMHFa_m202results, PMAMHFa_m202prefix, PMAMHFa_m202)

# PMAMHFa_m203results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m203/results.csv"
# PMAMHFa_m203prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m203/"
# PMAMHFa_m203 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m203"
# generate_part2(PMAMHFa_m203results, PMAMHFa_m203prefix, PMAMHFa_m203)
# ERROR

# PMAMHFa_m204results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m204/results.csv"
# PMAMHFa_m204prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m204/"
# PMAMHFa_m204 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m204"
# generate_part2(PMAMHFa_m204results, PMAMHFa_m204prefix, PMAMHFa_m204)

# PMAMHFa_m205results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m205/results.csv"
# PMAMHFa_m205prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m205/"
# PMAMHFa_m205 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m205"
# generate_part2(PMAMHFa_m205results, PMAMHFa_m205prefix, PMAMHFa_m205)
# ERROR

# PMAMHFa_m206results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m206/results.csv"
# PMAMHFa_m206prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m206/"
# PMAMHFa_m206 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m206"
# generate_part2(PMAMHFa_m206results, PMAMHFa_m206prefix, PMAMHFa_m206)
#
# PMAMHFa_m207results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m207/results.csv"
# PMAMHFa_m207prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m207/"
# PMAMHFa_m207 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m207"
# generate_part2(PMAMHFa_m207results, PMAMHFa_m207prefix, PMAMHFa_m207)
#
# PMAMHFa_m208results = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m208/results.csv"
# PMAMHFa_m208prefix = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m208/"
# PMAMHFa_m208 = "U:/Experiments/sleepHSP followup/followups/October 2016/PMAMHFa_m208"
# generate_part2(PMAMHFa_m208results, PMAMHFa_m208prefix, PMAMHFa_m208)


# AMPMHFa_m001results = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m001/results.csv"
# AMPMHFa_m002results = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m002/results.csv"
# AMPMHFa_m003results = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m003/results.csv"
# AMPMHFa_m004results = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m004/results.csv"
#
# AMPMHFa_m001prefix = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m001/"
# AMPMHFa_m002prefix = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m002/"
# AMPMHFa_m003prefix = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m003/"
# AMPMHFa_m004prefix = "U:/Experiments/sleepHSP followup/followups/test/AMPMHFa_m004/"
#
# AMPMHFa_m001 = "AMPMHFa_m001"
# AMPMHFa_m002 = "AMPMHFa_m002"
# AMPMHFa_m003 = "AMPMHFa_m003"
# AMPMHFa_m004 = "AMPMHFa_m004"
#
# generate_part2(AMPMHFa_m001results, AMPMHFa_m001, AMPMHFa_m001prefix)
# generate_part2(AMPMHFa_m002results, AMPMHFa_m002, AMPMHFa_m002prefix)
# generate_part2(AMPMHFa_m003results, AMPMHFa_m003, AMPMHFa_m003prefix)
# generate_part2(AMPMHFa_m004results, AMPMHFa_m004, AMPMHFa_m004prefix)
#
# PMAMHFa_m001results = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFa_m001/results.csv"
# PMAMHFa_m002results = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFa_m002/results.csv"
# PMAMHFa_m003results = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFa_m003/results.csv"
#
# PMAMHFa_m001prefix = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFa_m001/"
# PMAMHFa_m002prefix = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFa_m002/"
# PMAMHFa_m003prefix = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFa_m003/"
#
# PMAMHFa_m001 = "PMAMHFa_m001"
# PMAMHFa_m002 = "PMAMHFa_m002"
# PMAMHFa_m003 = "PMAMHFa_m003"
#
# generate_part2(PMAMHFa_m001results, PMAMHFa_m001, PMAMHFa_m001prefix)
# generate_part2(PMAMHFa_m002results, PMAMHFa_m002, PMAMHFa_m002prefix)
# generate_part2(PMAMHFa_m003results, PMAMHFa_m003, PMAMHFa_m003prefix)
#
# PMAMHFb_m001results = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFb_m001/results.csv"
# PMAMHFb_m004results = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFb_m004/results.csv"
# PMAMHFb_m005results = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFb_m005/results.csv"
#
# PMAMHFb_m001prefix = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFb_m001/"
# PMAMHFb_m004prefix = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFb_m004/"
# PMAMHFb_m005prefix = "U:/Experiments/sleepHSP followup/followups/test/PMAMHFb_m005/"
#
# PMAMHFb_m001 = "PMAMHFb_m001"
# PMAMHFb_m004 = "PMAMHFb_m004"
# PMAMHFb_m005 = "PMAMHFb_m005"
#
# generate_part2(PMAMHFb_m001results, PMAMHFb_m001, PMAMHFb_m001prefix)
# generate_part2(PMAMHFb_m004results, PMAMHFb_m004, PMAMHFb_m004prefix)
# generate_part2(PMAMHFb_m005results, PMAMHFb_m005, PMAMHFb_m005prefix)
