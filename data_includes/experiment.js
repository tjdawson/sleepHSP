var shuffleSequence = seq("intro", sepWith("sep", seq("guess0", "guess1"),  
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1"),
                                                      seq("guess0", "guess1")
                                           ),
                         "end" 
                          );
var practiceItemTypes = ["practice"];

var defaults = [
    "Separator", {
        transfer: "keypress",
        normalMessage: "Please wait for the next video. Then, press any key to start guessing.",
        errorMessage: "error\: Please wait for the next video. Then, press any key to start guessing."
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
        hideProgressBar: true,
        continueOnReturn: true,
        saveReactionTime: true
    }
];

var items = [

    ["sep", "Separator", { }],

    //

    ["intro", "Form", {
        html: { include: "intro.html" },
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
    } ]

    

    //["end", "Form", {
      //  html: { include: "end.html" }
    //} ],

    //

    //["blank_screen", "Form", {
      //  include: "blank_screen.html"
    //}]

];