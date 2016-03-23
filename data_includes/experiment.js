var shuffleSequence = seq("intro", "intro2", "intro3",
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
    "guess0", "guess1", "guess2", "guess3", "guess4", "sep"
                          );
var practiceItemTypes = ["practice"];

var defaults = [
    "Separator", {
        transfer: "keypress",
        normalMessage: "Please wait for the video to finish. Then, press any key to start guessing.",
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

    ["intro", "Form", {
        html: {include: "intro.html"},
    }],

    //

    ["intro2", "Form", {
        html: {include: "intro2.html"},
    }],

    //

    ["intro3", "Form", {
        html: { include: "intro3.html" },
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
    } ]

];
