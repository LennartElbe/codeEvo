var editor;

jQuery(document).ready(function() {
    console.log("hi the js is ready!");
    editor = ace.edit("program-code");
    editor.setTheme("ace/theme/github");
    editor.session.setMode("ace/mode/python");
    jQuery('#dropdownSwitchCode').on('click', 'a', function*() {
        var p = jQuery(this).attr('value');
        jQuery.get(p, function(data) {
            editor.setValue(data)
        })
        jQuery('#sheetsdropdown').text(jQuery(this).text());
    })
})
