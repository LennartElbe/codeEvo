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
        jQuery("#dropdownSwitchStudent").children().removeClass('active');
        jQuery(this).addClass('active');
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
    jQuery('#dropdownSwitchProblem').on('click', "a.dropdown-item", function() {
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
        for (var i = 0; i < ar.length; i++) {
            jQuery('#dropdownSwitchVersion').append("<a class=\"dropdown-item\" data-toggle=\"button\" value=\"" + ar[i] + "\">" + ar[i] + "</a>");
        }
    });
    jQuery('#dropdownSwitchVersion').on('click', "a.dropdown-item", function() {
        jQuery("#dropdownSwitchVersion").children().removeClass('active');
        jQuery(this).addClass('active');
        var version = jQuery(this).text();
        var student = jQuery('#dropdownSwitchStudent a.active').text();
        var problem = jQuery('#dropdownSwitchProblem a.active').text();
        var path = ["StudentProblem", student, problem, version].join('/');
        jQuery.get(path, function(data) {
            editor.setValue(data);
        });
        jQuery('#versionsDropDown span.whichVersion').text(version);
    });
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
})
