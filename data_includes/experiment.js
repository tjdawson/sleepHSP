// functions for generating followup links and emails

var email;
var unique_id;
var followup_link;

function send_mail(){
    email = document.getElementById('participant_email');
    unique_id = document.getElementById('unique_id');
    followup_link = "http://spellout.net/ibexexps/trueswell_lab/followup/"+unique_id.value+"/experiment.html";
    document.location.href = "mailto:"+email.value+"?subject=Sleep Study Followup Survey Link&body="+followup_link;
}

function print_link(){
    email = document.getElementById('participant_email');
    unique_id = document.getElementById('unique_id');
    followup_link = "http://spellout.net/ibexexps/trueswell_lab/followup/"+unique_id.value+"/experiment.html";
    var display_link = document.createElement('p');
    display_link.textContent = followup_link;
    document.getElementById("display_link").appendChild(display_link)
}

//

var shuffleSequence = seq("intro", "intro1", "intro2", "intro3",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep",
    "guess0", "guess1", "guess2", "guess3", "guess4", "end"
                          );
var practiceItemTypes = ["practice"];

var defaults = [
    "Separator", {
        transfer: "keypress",
        normalMessage: "Please look up at the display on the wall and watch the video. When it's finished, press any key to start guessing.",
        errorMessage: "Please wait for the video to finish. Then, press any key to start guessing."
    },
    "DashedSentence", {
        mode: "self-paced reading"
    },
    "AcceptabilityJudgment", {
        as: ["1", "2", "3", "4", "5", "6", "7"],
        presentAsScale: true,
        instructions: "Use number keys or click boxes to answer.",
        leftComment: "(Bad)", rightComment: "(Good)"
    },
    "Question", {
        hasCorrect: true
    },
    "Message", {
        hideProgressBar: true
    },
    "Form", {
        hideProgressBar: false,
        continueOnReturn: true,
        saveReactionTime: false
    }
];

var items = [

    ["sep", "Separator", { }],

    //

    ["end", "Form", {
        html: {include: "end.html"},
        hideProgressBar: true,
        countsForProgressBar: false

    }],

    //

    ["intro", "Form", {
        html: {include: "intro.html"},
        hideProgressBar: true,
        countsForProgressBar: false

    }],

    //

    ["intro1", "Form", {
        html: {include: "intro1.html"},
        hideProgressBar: true,
        countsForProgressBar: false

    }],

    //

    ["intro2", "Form", {
        html: {include: "intro2.html"},
        hideProgressBar: true,
        countsForProgressBar: false

    }],

    //

    ["intro3", "Form", {
        html: { include: "intro3.html" },
        hideProgressBar: true,
        countsForProgressBar: false,
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],

    //

    ["guess0", "Form", {
        html: { include: "guess0.html" }
    } ],

    //

    ["guess1", "Form", {
        html: { include: "guess.html" }
    } ],

    //

    ["guess2", "Form", {
        html: { include: "guess.html" }
    } ],

    //

    ["guess3", "Form", {
        html: { include: "guess.html" }
    } ],

    //

    ["guess4", "Form", {
        html: { include: "guess.html" }
    } ],

    //

    ["sep1", "Separator", {
        normalMessage: "Please look up at the display on the wall and wait for the next video. Then, press any key to begin guessing.",
    }]

];
