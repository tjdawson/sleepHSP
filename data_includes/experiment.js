// set send results to manual
var manualSendResults = true;

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
    followup_link = "http://spellout.net/ibexexps/trueswell_lab/followup"+unique_id.value+"/experiment.html";
    var display_link = document.createElement('p');
    display_link.textContent = followup_link;
    document.getElementById("display_link").appendChild(display_link)
}

//

var shuffleSequence = seq("intro", "intro1", "intro2", "intro3", "sep", 
"blime_toy_guess0", "blime_toy_guess1", "blime_toy_guess2", "blime_toy_guess3", "blime_toy_guess4", "sep",
"telpen_ball_guess0", "telpen_ball_guess1", "telpen_ball_guess2", "telpen_ball_guess3", "telpen_ball_guess4", "sep",
"geck_nose_guess0", "geck_nose_guess1", "geck_nose_guess2", "geck_nose_guess3", "geck_nose_guess4", "sep",
"tiz_thing_guess0", "tiz_thing_guess1", "tiz_thing_guess2", "tiz_thing_guess3", "tiz_thing_guess4", "sep",
"vash_shoe_guess0", "vash_shoe_guess1", "vash_shoe_guess2", "vash_shoe_guess3", "vash_shoe_guess4", "sep",
"zant_book_guess0", "zant_book_guess1", "zant_book_guess2", "zant_book_guess3", "zant_book_guess4", "sep",
"jair_time_guess0", "jair_time_guess1", "jair_time_guess2", "jair_time_guess3", "jair_time_guess4", "sep",
"tace_phone_guess0", "tace_phone_guess1", "tace_phone_guess2", "tace_phone_guess3", "tace_phone_guess4", "sep",
"doon_necklace_guess0", "doon_necklace_guess1", "doon_necklace_guess2", "doon_necklace_guess3", "doon_necklace_guess4", "sep",
"tula_mommy_guess0", "tula_mommy_guess1", "tula_mommy_guess2", "tula_mommy_guess3", "tula_mommy_guess4", "sep",
"bist_horse_guess0", "bist_horse_guess1", "bist_horse_guess2", "bist_horse_guess3", "bist_horse_guess4", "sep",
"mipen_bag_guess0", "mipen_bag_guess1", "mipen_bag_guess2", "mipen_bag_guess3", "mipen_bag_guess4", "sep",
"blime_toy_guess0", "blime_toy_guess1", "blime_toy_guess2", "blime_toy_guess3", "blime_toy_guess4", "sep",
"telpen_ball_guess0", "telpen_ball_guess1", "telpen_ball_guess2", "telpen_ball_guess3", "telpen_ball_guess4", "sep",
"geck_nose_guess0", "geck_nose_guess1", "geck_nose_guess2", "geck_nose_guess3", "geck_nose_guess4", "sep",
"tiz_thing_guess0", "tiz_thing_guess1", "tiz_thing_guess2", "tiz_thing_guess3", "tiz_thing_guess4", "sep",
"vash_shoe_guess0", "vash_shoe_guess1", "vash_shoe_guess2", "vash_shoe_guess3", "vash_shoe_guess4", "sep",
"zant_book_guess0", "zant_book_guess1", "zant_book_guess2", "zant_book_guess3", "zant_book_guess4", "sep",
"jair_time_guess0", "jair_time_guess1", "jair_time_guess2", "jair_time_guess3", "jair_time_guess4", "sep",
"tace_phone_guess0", "tace_phone_guess1", "tace_phone_guess2", "tace_phone_guess3", "tace_phone_guess4", "sep",
"doon_necklace_guess0", "doon_necklace_guess1", "doon_necklace_guess2", "doon_necklace_guess3", "doon_necklace_guess4", "sep",
"tula_mommy_guess0", "tula_mommy_guess1", "tula_mommy_guess2", "tula_mommy_guess3", "tula_mommy_guess4", "sep",
"bist_horse_guess0", "bist_horse_guess1", "bist_horse_guess2", "bist_horse_guess3", "bist_horse_guess4", "sep",
"mipen_bag_guess0", "mipen_bag_guess1", "mipen_bag_guess2", "mipen_bag_guess3", "mipen_bag_guess4", "sep",
"blime_toy_guess0", "blime_toy_guess1", "blime_toy_guess2", "blime_toy_guess3", "blime_toy_guess4", "sep",
"telpen_ball_guess0", "telpen_ball_guess1", "telpen_ball_guess2", "telpen_ball_guess3", "telpen_ball_guess4", "sep",
"geck_nose_guess0", "geck_nose_guess1", "geck_nose_guess2", "geck_nose_guess3", "geck_nose_guess4", "sep",
"tiz_thing_guess0", "tiz_thing_guess1", "tiz_thing_guess2", "tiz_thing_guess3", "tiz_thing_guess4", "sep",
"vash_shoe_guess0", "vash_shoe_guess1", "vash_shoe_guess2", "vash_shoe_guess3", "vash_shoe_guess4", "sep",
"zant_book_guess0", "zant_book_guess1", "zant_book_guess2", "zant_book_guess3", "zant_book_guess4", "sep",
"jair_time_guess0", "jair_time_guess1", "jair_time_guess2", "jair_time_guess3", "jair_time_guess4", "sep",
"tace_phone_guess0", "tace_phone_guess1", "tace_phone_guess2", "tace_phone_guess3", "tace_phone_guess4", "sep",
"doon_necklace_guess0", "doon_necklace_guess1", "doon_necklace_guess2", "doon_necklace_guess3", "doon_necklace_guess4", "sep",
"tula_mommy_guess0", "tula_mommy_guess1", "tula_mommy_guess2", "tula_mommy_guess3", "tula_mommy_guess4", "sep",
"bist_horse_guess0", "bist_horse_guess1", "bist_horse_guess2", "bist_horse_guess3", "bist_horse_guess4", "sep",
"mipen_bag_guess0", "mipen_bag_guess1", "mipen_bag_guess2", "mipen_bag_guess3", "mipen_bag_guess4", "sep",
"blime_toy_guess0", "blime_toy_guess1", "blime_toy_guess2", "blime_toy_guess3", "blime_toy_guess4", "sep",
"telpen_ball_guess0", "telpen_ball_guess1", "telpen_ball_guess2", "telpen_ball_guess3", "telpen_ball_guess4", "sep",
"geck_nose_guess0", "geck_nose_guess1", "geck_nose_guess2", "geck_nose_guess3", "geck_nose_guess4", "sep",
"tiz_thing_guess0", "tiz_thing_guess1", "tiz_thing_guess2", "tiz_thing_guess3", "tiz_thing_guess4", "sep",
"vash_shoe_guess0", "vash_shoe_guess1", "vash_shoe_guess2", "vash_shoe_guess3", "vash_shoe_guess4", "sep",
"zant_book_guess0", "zant_book_guess1", "zant_book_guess2", "zant_book_guess3", "zant_book_guess4", "sep",
"jair_time_guess0", "jair_time_guess1", "jair_time_guess2", "jair_time_guess3", "jair_time_guess4", "sep",
"tace_phone_guess0", "tace_phone_guess1", "tace_phone_guess2", "tace_phone_guess3", "tace_phone_guess4", "sep",
"doon_necklace_guess0", "doon_necklace_guess1", "doon_necklace_guess2", "doon_necklace_guess3", "doon_necklace_guess4", "sep",
"tula_mommy_guess0", "tula_mommy_guess1", "tula_mommy_guess2", "tula_mommy_guess3", "tula_mommy_guess4", "sep",
"bist_horse_guess0", "bist_horse_guess1", "bist_horse_guess2", "bist_horse_guess3", "bist_horse_guess4", "sep",
"mipen_bag_guess0", "mipen_bag_guess1", "mipen_bag_guess2", "mipen_bag_guess3", "mipen_bag_guess4", "sep",
"blime_toy_guess0", "blime_toy_guess1", "blime_toy_guess2", "blime_toy_guess3", "blime_toy_guess4", "sep",
"telpen_ball_guess0", "telpen_ball_guess1", "telpen_ball_guess2", "telpen_ball_guess3", "telpen_ball_guess4", "sep",
"geck_nose_guess0", "geck_nose_guess1", "geck_nose_guess2", "geck_nose_guess3", "geck_nose_guess4", "sep",
"tiz_thing_guess0", "tiz_thing_guess1", "tiz_thing_guess2", "tiz_thing_guess3", "tiz_thing_guess4", "sep",
"vash_shoe_guess0", "vash_shoe_guess1", "vash_shoe_guess2", "vash_shoe_guess3", "vash_shoe_guess4", "sep",
"zant_book_guess0", "zant_book_guess1", "zant_book_guess2", "zant_book_guess3", "zant_book_guess4", "sep",
"jair_time_guess0", "jair_time_guess1", "jair_time_guess2", "jair_time_guess3", "jair_time_guess4", "sep",
"tace_phone_guess0", "tace_phone_guess1", "tace_phone_guess2", "tace_phone_guess3", "tace_phone_guess4", "sep",
"doon_necklace_guess0", "doon_necklace_guess1", "doon_necklace_guess2", "doon_necklace_guess3", "doon_necklace_guess4", "sep",
"tula_mommy_guess0", "tula_mommy_guess1", "tula_mommy_guess2", "tula_mommy_guess3", "tula_mommy_guess4", "sep",
"bist_horse_guess0", "bist_horse_guess1", "bist_horse_guess2", "bist_horse_guess3", "bist_horse_guess4", "sep",
"mipen_bag_guess0", "mipen_bag_guess1", "mipen_bag_guess2", "mipen_bag_guess3", "mipen_bag_guess4", "sr",
"end"
);

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

    //

    ["sr", "__SendResults__", {}],

    //

    ["sep", "Separator", { }],
    
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
["tula_mommy_guess0", "Form", { 
html: {include: "tula_mommy_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tula_mommy_guess1", "Form", { 
html: {include: "tula_mommy_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tula_mommy_guess2", "Form", { 
html: {include: "tula_mommy_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tula_mommy_guess3", "Form", { 
html: {include: "tula_mommy_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tula_mommy_guess4", "Form", { 
html: {include: "tula_mommy_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tace_phone_guess0", "Form", { 
html: {include: "tace_phone_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tace_phone_guess1", "Form", { 
html: {include: "tace_phone_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tace_phone_guess2", "Form", { 
html: {include: "tace_phone_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tace_phone_guess3", "Form", { 
html: {include: "tace_phone_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tace_phone_guess4", "Form", { 
html: {include: "tace_phone_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["geck_nose_guess0", "Form", { 
html: {include: "geck_nose_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["geck_nose_guess1", "Form", { 
html: {include: "geck_nose_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["geck_nose_guess2", "Form", { 
html: {include: "geck_nose_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["geck_nose_guess3", "Form", { 
html: {include: "geck_nose_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["geck_nose_guess4", "Form", { 
html: {include: "geck_nose_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["zant_book_guess0", "Form", { 
html: {include: "zant_book_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["zant_book_guess1", "Form", { 
html: {include: "zant_book_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["zant_book_guess2", "Form", { 
html: {include: "zant_book_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["zant_book_guess3", "Form", { 
html: {include: "zant_book_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["zant_book_guess4", "Form", { 
html: {include: "zant_book_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["bist_horse_guess0", "Form", { 
html: {include: "bist_horse_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["bist_horse_guess1", "Form", { 
html: {include: "bist_horse_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["bist_horse_guess2", "Form", { 
html: {include: "bist_horse_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["bist_horse_guess3", "Form", { 
html: {include: "bist_horse_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["bist_horse_guess4", "Form", { 
html: {include: "bist_horse_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tiz_thing_guess0", "Form", { 
html: {include: "tiz_thing_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tiz_thing_guess1", "Form", { 
html: {include: "tiz_thing_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tiz_thing_guess2", "Form", { 
html: {include: "tiz_thing_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tiz_thing_guess3", "Form", { 
html: {include: "tiz_thing_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["tiz_thing_guess4", "Form", { 
html: {include: "tiz_thing_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["blime_toy_guess0", "Form", { 
html: {include: "blime_toy_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["blime_toy_guess1", "Form", { 
html: {include: "blime_toy_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["blime_toy_guess2", "Form", { 
html: {include: "blime_toy_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["blime_toy_guess3", "Form", { 
html: {include: "blime_toy_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["blime_toy_guess4", "Form", { 
html: {include: "blime_toy_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["jair_time_guess0", "Form", { 
html: {include: "jair_time_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["jair_time_guess1", "Form", { 
html: {include: "jair_time_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["jair_time_guess2", "Form", { 
html: {include: "jair_time_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["jair_time_guess3", "Form", { 
html: {include: "jair_time_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["jair_time_guess4", "Form", { 
html: {include: "jair_time_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["vash_shoe_guess0", "Form", { 
html: {include: "vash_shoe_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["vash_shoe_guess1", "Form", { 
html: {include: "vash_shoe_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["vash_shoe_guess2", "Form", { 
html: {include: "vash_shoe_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["vash_shoe_guess3", "Form", { 
html: {include: "vash_shoe_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["vash_shoe_guess4", "Form", { 
html: {include: "vash_shoe_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["mipen_bag_guess0", "Form", { 
html: {include: "mipen_bag_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["mipen_bag_guess1", "Form", { 
html: {include: "mipen_bag_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["mipen_bag_guess2", "Form", { 
html: {include: "mipen_bag_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["mipen_bag_guess3", "Form", { 
html: {include: "mipen_bag_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["mipen_bag_guess4", "Form", { 
html: {include: "mipen_bag_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["doon_necklace_guess0", "Form", { 
html: {include: "doon_necklace_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["doon_necklace_guess1", "Form", { 
html: {include: "doon_necklace_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["doon_necklace_guess2", "Form", { 
html: {include: "doon_necklace_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["doon_necklace_guess3", "Form", { 
html: {include: "doon_necklace_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["doon_necklace_guess4", "Form", { 
html: {include: "doon_necklace_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["telpen_ball_guess0", "Form", { 
html: {include: "telpen_ball_guess0.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["telpen_ball_guess1", "Form", { 
html: {include: "telpen_ball_guess1.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["telpen_ball_guess2", "Form", { 
html: {include: "telpen_ball_guess2.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["telpen_ball_guess3", "Form", { 
html: {include: "telpen_ball_guess3.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["telpen_ball_guess4", "Form", { 
html: {include: "telpen_ball_guess4.html"}, 
 validators: {guess: function (s) {if (s.match(/^(?![\s\S])|^[A-Za-z']+$/)) return true; else return "Please enter only a single word per guess"; } } }],

["end", "Form", {
        html: {include: "end.html"},
        hideProgressBar: true,
        countsForProgressBar: false,
        continueMessage: null
    
    }]
];