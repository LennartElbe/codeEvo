<!DOCTYPE html>
<HTML>
<HEAD>
    <TITLE>Code Evo</TITLE>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="css/ace-diff.min.css" rel="stylesheet">
    <link href="css/ace-diff-dark.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
</HEAD>

<BODY>
    <div class="container-fluid">
        <div class="row-fluid">
            <div class="col-md-12">
                <h1>Code Evo</h1>
                <h5>Select a student, a problem, and a version. The left side of
                     the diff is the currently selected version, and the right
                      side is the last viewed version. Diff is seen in blue.
                      Below the diffs you can see the output of the code on the right.
                      The output is not live.
                      
                <div class="dropdown" style="display: inline-flex;">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="studentsDropDown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Students <span class="whichStudent"></button>
                    <div class="dropdown-menu" id="dropdownSwitchStudent" aria-labelledby="dropdownMenuButton">
                    </div>
                </div>
                <div class="dropdown" style="display: inline-flex;">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="problemsDropDown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Problems <span class="whichProblem"></button>
                    <div class="dropdown-menu" id="dropdownSwitchProblem" aria-labelledby="dropdownMenuButton">
                    </div>
                </div>
                <div class="dropdown" style="display: inline-flex;">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="versionsDropDown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Versions <span class="whichVersion"></span></button>
                    <div class="dropdown-menu" id="dropdownSwitchVersion" aria-labelledby="dropdownMenuButton">
                    </div>
                </div>
                <div style="margin-left: 8px; display: inline-flex;">
                    <button type="button" class="btn btn-primary" id="previous" style="margin-right: 4px">&lt;</button>
                    <button type="button" class="btn btn-primary" id="next">&gt;</button>
                </div>
            </div>
        </div>
        <div class="row-fluid">
            <div class="col-md-12">
                <div class="acediff"></div>
            </div>
        </div>
        <div class="row-fluid">
            <div class="col-md-12">
                <h4 align="center">OUTPUTVVV</h4>
                    <div class="row">
                        <div id="program-code" style="width: 50%; height: 600px"></div>
                        <div id="program-output" style="width: 50%; height: 600px"></div>
                    </div>
            </div>
        </div>
        <div class="row-fluid">
            <div class ="col-md-12" id="StudentButtons"></div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="js/ace/ace.js"></script>
    <script src="js/ace-diff@^2.0.0"></script>
    <script type="text/javascript" src="js/template.js"></script>
</BODY>

</HTML>