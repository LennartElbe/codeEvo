<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE>Code Evo</TITLE>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script type="text/javascript" src="./practice.js"></script>
    <script src="js/ace/ace.js"></script>
</HEAD>

<BODY>
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm">
                <h1>Code Evo</h1>
            </div>
        </div>
        <div class="row">
            <div id="program-code"></div>
        </div>
        <div class="row">
            <div class="dropdown">
                <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Students</button>
                <div class="dropdown-menu" id="dropdownSwitchEngine" aria-labelledby="dropdownMenuButton">
                </div>
            </div>
            <div class="col-sm" style="position: relative;">
                <div id="program-code">
                </div>
            </div>
            <div class="col-sm" style="position: relative; height: 500px;">
                <div id="program-output">
                </div>
            </div>
        </div>
        <div class="row">
            <button class="btn btn-primary" type="button" id="butt">Press Me</button>
            <button class="btn btn-info" type="button" id="clear">Clear Output</button>
        </div>
    </div>
</BODY>

</HTML>