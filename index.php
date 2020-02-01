<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE>Code Evo</TITLE>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="css/style.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="js/ace/ace.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script type="text/javascript" src="js/template.js"></script>
</HEAD>

<BODY>
    <div class="container-fluid">
        <h1 style="margin-left: -15px">Code Evo</h1>
        <div class="row">
            <div class="dropdown" style="float: right;">
                <button class="btn btn-secondary dropdown-toggle" style="margin-left: 10px" type="button" id="studentsDropDown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Students</button>
                <div class="dropdown-menu" id="dropdownSwitchStudent" aria-labelledby="dropdownMenuButton">
                </div>
            </div>
            <div class="dropdown" style="float: right;">
                <button class="btn btn-secondary dropdown-toggle" style="margin-left: 10px" type="button" id="problemsDropDown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Problems</button>
                <div class="dropdown-menu" id="dropdownSwitchProblem" aria-labelledby="dropdownMenuButton">
                </div>
            </div>
        </div>
        <div class="col-md-12">
            <div id="program-code" style="width: 50%; height: 600px"></div>
        </div>
    </div>
</BODY>

</HTML>