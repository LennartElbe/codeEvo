var editor;
var output;
var diffeditors;
var _data;
// fills in dropdowns, swap displayed code, implementation of next and previous buttons
jQuery(document).ready(function() {
    console.log("hi the js is ready!");
    editor = ace.edit("program-code");
    editor.setTheme("ace/theme/github");
    editor.session.setMode("ace/mode/python");
    output = ace.edit("program-output");
    output.setTheme("ace/theme/github");
    output.session.setMode("ace/mode/python");
    // fill in the dropdowns
    jQuery.getJSON('php/getScripts.php', function(data) {
        var students = {};
        for (var i = 0; i < data.length; i++) {
            var text = data[i].split("/");
            if (!(text[2] in students)) {
                students[text[2]] = [[text[3], text[4]]];
            }
            else {
                students[text[2]].push([text[3], text[4]]);
            }
        }
        var st = Object.keys(students);
        _data = students;
        // add students to dropdown
        for (var i = 0; i < st.length; i++) {
            jQuery('#dropdownSwitchStudent').append("<a class=\"dropdown-item\" data-toggle=\"button\" value=\"" + st[i] + "\">" + st[i] + "</a>");
        }
    });
    // add problems to dropdown
    jQuery('#dropdownSwitchStudent').on('click', "a.dropdown-item", function() {
        jQuery("#dropdownSwitchStudent").children().removeClass('active');
        jQuery(this).addClass('active');
        jQuery('#dropdownSwitchProblem').children().remove();
        var student = jQuery(this).text();
        var ar = {};
        for (var i = 0; i < _data[student].length; i++) {
            ar[_data[student][i][0]] = 1;
        }
        var ar2 = Object.keys(ar);
        jQuery('#studentsDropDown span.whichStudent').text(student);
        for (var i = 0; i < ar2.length; i++) {
            jQuery('#dropdownSwitchProblem').append("<a class=\"dropdown-item\" data-toggle=\"button\" value=\"" + ar2[i] + "\">" + ar2[i] + "</a>");
        }
    });
    // add versions to dropdown
    jQuery('#dropdownSwitchProblem').on('click', "a.dropdown-item", function() {
        editor.setValue("Please select a version.");
        jQuery('#dropdownSwitchVersion').children().remove();
        jQuery("#dropdownSwitchProblem").children().removeClass('active');
        jQuery(this).addClass('active');
        var problem = jQuery(this).text();
        var ar = [];
        var student = jQuery('#dropdownSwitchStudent a.active').text();
        for (var i = 0; i < _data[student].length; i++) {
            if (_data[student][i][0] == problem) {
                ar.push(_data[student][i][1]);
            }
        }
        jQuery('#problemsDropDown span.whichProblem').text(": " + problem);
        jQuery('#versionsDropDown span.whichVersion').text("");
        for (var i = 0; i < ar.length; i++) {
            jQuery('#dropdownSwitchVersion').append("<a class=\"dropdown-item\" data-toggle=\"button\" value=\"" + ar[i] + "\">" + ar[i] + "</a>");
        }
    });
    // switch displayed code when version is selected
    jQuery('#dropdownSwitchVersion').on('click', "a.dropdown-item", function() {
        // jQuery("#righteditorlabel").setVal("#a.dropdown-item".text()); // change the button's text to the name of the active button in the dropdown
        jQuery("#dropdownSwitchVersion").children().removeClass('active');
        jQuery(this).addClass('active');
        var version = jQuery(this).text();
        var student = jQuery('#dropdownSwitchStudent a.active').text();
        var problem = jQuery('#dropdownSwitchProblem a.active').text();
        var path = ["StudentProblem", student, problem, version].join('/');
        var outputpath = ["Output", "StudentProblem", student, problem, version].join('/');
        jQuery.get(path, function(data) {
            editor.setValue(data);
            diffeditors = differ.getEditors();
            var oldvalue = diffeditors.left.getValue();
            diffeditors.right.setValue(oldvalue);
            diffeditors.left.setValue(data); // THIS IS HOW U DO IT
            diffeditors.left.clearSelection();
            diffeditors.right.clearSelection();
        });
        jQuery.get(outputpath, function(data) {
            output.setValue(data);
        })
        jQuery('#versionsDropDown span.whichVersion').text(version);
    });
    // next and previous buttons
    jQuery('#next').on('click', function() {
        var version = jQuery('#dropdownSwitchVersion a.active');
        if (jQuery(version).next().length == 0) {
            return;
        }
        jQuery("#dropdownSwitchVersion").children().removeClass('active');
        jQuery(version).removeClass('active');
        jQuery(version).next().addClass('active');
        jQuery(version).next().trigger('click');
    });
    jQuery('#previous').on('click', function () {
        var version = jQuery('#dropdownSwitchVersion a.active');
        if (jQuery(version).prev().length == 0) {
            return;
        }
        jQuery("#dropdownSwitchVersion").children().removeClass('active');
        jQuery(version).removeClass('active');
        jQuery(version).prev().addClass('active');
        jQuery(version).prev().trigger('click');
    });
    var differ = new AceDiff({
        element: '.acediff',
        left: {
            content: 'your first file content here',
        },
        right: {
            content: 'your second file content here',
        },
    });
})
