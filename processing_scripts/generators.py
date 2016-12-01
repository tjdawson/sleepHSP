import csv
import itertools
import string

hf_order_a_config, hf_order_b_config, \
    hl_order_a_config, hl_order_b_config = "U:/Experiments/sleepHSP/processing_scripts/config/hf_order_a.csv", \
                                           "U:/Experiments/sleepHSP/processing_scripts/config/hf_order_b.csv", \
                                           "U:/Experiments/sleepHSP/processing_scripts/config/hl_order_a.csv", \
                                           "U:/Experiments/sleepHSP/processing_scripts/config/hl_order_b.csv"


def generate_shuffle_sequence(config_file):
    """Takes a configuration file and produces a shuffle sequence
    Input: a csv file with header Trial, VideoFile, MysteryWord, TargetWord
    Output: a string with the ibex shuffle_sequence var"""
    shuffle_sequence_begin = "var shuffleSequence = seq(\"intro\", \"intro1\", \"intro2\", \"intro3\", \"sep\", \n"
    shuffle_sequence_middle = ""
    shuffle_sequence_end = "\"sr\", \"end\"\n);"

    with open(config_file, 'rb+') as config_file:
        config_file = csv.reader(config_file)
        next(config_file, None)  # skip header
        config_file = list(config_file)

        for n, line in enumerate(config_file):
            for i in range(5):
                shuffle_sequence_middle += "\"{}_{}_guess{}\", ".format(line[2].lower(), line[3], i)
            if n != len(config_file)-1:  # every iteration but the last one writes a separator
                shuffle_sequence_middle += "\"sep\","
            shuffle_sequence_middle += "\n"
        shuffle_sequence = shuffle_sequence_begin + shuffle_sequence_middle + shuffle_sequence_end

        return shuffle_sequence


def generate_forms(config_file):
    with open(config_file, 'rb+') as config_file:
        config_file = csv.reader(config_file)
        next(config_file, None)  # skip header
        config_file = list(config_file)

        word_list = set()
        for row in config_file:
            word_list.add("{}_{}".format(row[2].lower(), row[3].lower()))

        output = ""
        word_list = list(word_list)
        for word in word_list:
            for i in range(5):
                guess = "[\"%s_guess%s\", \"Form\", { \nhtml: {include: \"%s_guess%s.html\"}, \n validators: {guess: function (s) {if (s.match(/^[A-Za-z']+$/)) return true; else return \"Please enter only a single word per guess\"; } } }]," % (word, i, word, i)
                output += guess + "\n\n"
        return output


def generate_defaults():
    return "var defaults = [\n\
    \"Separator\", {\n\
        transfer: \"keypress\",\n\
        normalMessage: \"Please look up at the display on the wall and watch the video. When it's finished, press any key to start guessing.\",\n\
        errorMessage: \"Please wait for the video to finish. Then, press any key to start guessing.\"\n\
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


def generate_items(config_file):
    output = ""
    begin = "var items = [\n   [\"sr\", \"__SendResults__\", { }], \n\
    [\"sep\", \"Separator\", { }],\n\
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
    \n\
    }],\n\
    \n\
    //\n\
    \n\
    [\"intro2\", \"Form\", {\n\
        html: {include: \"intro2.html\"},\n\
        hideProgressBar: true,\n\
        countsForProgressBar: false\n\
    \n\
    }],\n\
    \n\
    //\n\
    \n\
    [\"intro3\", \"Form\", {\n\
        html: { include: \"intro3.html\" },\n\
        hideProgressBar: true,\n\
        countsForProgressBar: false,\n\
        validators: {\n\
            age: function (s) { if (s.match(/^\d+$/)) return true; else return \"Bad value for \u2018age\u2019\"; }\n\
        }\n\
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
    output += begin + "\n" + generate_forms(config_file) + end
    return output


def generate_html(config_file, dir_prefix):
    with open(config_file, 'rb+') as config_file:
        config_file = csv.reader(config_file)
        next(config_file, None)  # skip header
        config_file = list(config_file)

        word_list = ["{}_{}".format(row[2].lower(), row[3].lower()) for row in config_file]
        output = ""
        begin = ""
        end = ""

        for i in range(5):
            for word in word_list:
                mystery_word = "\"{}\"".format(word.split('_')[0].upper())
                fname = "{}_guess{}".format(word, i)
                with open("{}/chunk_includes/{}.html".format(dir_prefix,fname), 'wb+') as html:
                    middle = "<style>\n\
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
\n\
<div style=\"width: 40em;\">\n\
\n\
<table cellpadding=\"10\" cellspacing=\"4\">\n\
<tr>\n\
  <td>%s<br>\n\
  Guess %s: <input name=\"guess\" type=\"text\" size=\"40\" %s placeholder=\"%s\"/></td>\n\
</tr>\n\
<tr class=\"bordered\">\n\
    <td>\n\
        <a class=\"left\">Not at all confident</a>\n\
        <label for=\"conf1\"><input type=\"radio\" id=\"conf1\" name=\"confidence\" value=\"1\" %s><span>1</span></label>\n\
        <label for=\"conf2\"><input type=\"radio\" id=\"conf2\" name=\"confidence\" value=\"2\"><span>2</span></label>\n\
        <label for=\"conf3\"><input type=\"radio\" id=\"conf3\" name=\"confidence\" value=\"3\"><span>3</span></label>\n\
        <label for=\"conf4\"><input type=\"radio\" id=\"conf4\" name=\"confidence\" value=\"4\"><span>4</span></label>\n\
        <label for=\"conf5\"><input type=\"radio\" id=\"conf5\" name=\"confidence\" value=\"5\"><span>5</span></label>\n\
        <a class=\"right\">Very confident </a>\n\
    </td>\n\
</tr>\n\
\n\
\n\
</table>\n\
\n\
</div>" % (mystery_word,str(i+1),'class=\"obligatory\"' if i == 0 else '', 'Enter a single guess' if i == 0 else 'Enter a single guess, or click below to continue', 'class=\"obligatory\"' if i == 0 else '')
                    output += begin + middle + end
                    html.write(output)
                    output = ""


def generate_experimentjs(config_file, dir_prefix):
    output = ""
    begin = "// we want to be able to send results before the end \n var manualSendResults = true; \n\
    // functions for generating followup links and emails\n\
var email;\n\
var unique_id;\n\
var followup_link;\n\
\nfunction send_mail(){\n\
    email = document.getElementById(\'participant_email\');\n\
    unique_id = document.getElementById(\'unique_id\');\n\
    followup_link = \"http://spellout.net/ibexexps/trueswell_lab/followup/\"+unique_id.value+\"/experiment.html\";\n\
    document.location.href = \"mailto:\"+email.value+\"?subject=Sleep Study Followup Survey Link&body=\"+followup_link;\n\
}\n\
\n\
function print_link(){\n\
    email = document.getElementById(\'participant_email\');\n\
    unique_id = document.getElementById(\'unique_id\');\n\
    followup_link = \"http://spellout.net/ibexexps/trueswell_lab/followup\"+unique_id.value+\"/experiment.html\";\n\
    var display_link = document.createElement(\'p\');\n\
    display_link.textContent = followup_link;\n\
    document.getElementById(\"display_link\").appendChild(display_link)\n\
}\n\
\n\
//\n\
\n"
    output += begin + generate_shuffle_sequence(config_file) + "\n\n" + generate_defaults() + "\n\n" + generate_items(config_file)
    # return output
    with open('{}/data_includes/experiment.js'.format(dir_prefix), 'wb+') as experiment_js:
        experiment_js.write(output)


def generate_part1(config_file, dir_prefix, num_guesses=5, video=False):
    """Input: a csv file, the number of guesses allowed per item,
    and the path to the root directory for the experiment
        Optional: specify whether to generate html for displaying video
    Output: in the directory specified, the files for an ibex HSP experiment"""
    generate_html(config_file, dir_prefix)
    generate_experimentjs(config_file, dir_prefix)


# print generate_forms(hf_order_a_config)
# generate_part1(hf_order_a_config, 'U:/Experiments/sleepHSP')
generate_part1(hf_order_a_config, 'C:/Users/tjdawson/Dropbox/Sleep_Study/HFa')
generate_part1(hf_order_b_config, 'C:/Users/tjdawson/Dropbox/Sleep_Study/HFb')
generate_part1(hl_order_a_config, 'C:/Users/tjdawson/Dropbox/Sleep_Study/HLa')
generate_part1(hl_order_b_config, 'C:/Users/tjdawson/Dropbox/Sleep_Study/HLb')
