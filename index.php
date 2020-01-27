<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE>PRACTICE</TITLE>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script type="text/javascript" src="./practice.js"></script>
</HEAD>

<BODY>
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm">
                <h1>Einf. in die Programmierung Klausurlösungen</h1>
                <textarea rows="4" cols="50" id="input"></textarea>
            </div>
        </div>
        <div class="row">
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