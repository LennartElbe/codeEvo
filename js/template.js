var editor;
var _data;

jQuery(document).ready(function() {
    console.log("hi the js is ready!");
    editor = ace.edit("program-code");
    editor.setTheme("ace/theme/github");
    editor.session.setMode("ace/mode/python");
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
        jQuery('#dropdownSwitchProblem').children().remove();
        var student = jQuery(this).text();
        var ar = {};
        for (var i = 0; i < _data[student].length; i++) {
            ar[_data[student][i][0]] = 1;
        }
        var ar2 = Object.keys(ar);
        for (var i = 0; i < ar2.length; i++) {
            jQuery('#dropdownSwitchProblem').append("<a class=\"dropdown-item\" data-toggle=\"button\" value=\"" + ar2[i] + "\">" + ar2[i] + "</a>");
        }
    });
})
