var maxNumDisplayed = 15 + 3;

function listAllProf(){
    const Http = new XMLHttpRequest();

    var nameCheck = document.getElementById( "orderName" );
    var deptCheck = document.getElementById( "orderDept" );
    var salCheck = document.getElementById( "orderSalary" );
    var addToGET = "";
    if ( nameCheck.checked ) addToGET += nameCheck.value + ",";
    if ( deptCheck.checked ) addToGET += deptCheck.value + ",";
    if ( salCheck.checked ) addToGET += salCheck.value;

    const url = '/api/F1?orderByType=' + addToGET;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var profListF1Div = document.getElementById( "orderProfDiv" );
        var keys = Object.keys(JSON.parse(response));
        profListF1Div.className = "scrollingTable";
        var numElements = (keys.length + 3 > maxNumDisplayed) ? maxNumDisplayed : keys.length + 3;
        profListF1Div.style.height = numElements * 20;
        var newInner = Table.toHtmlFromJson( response, "Instructors" );
        profListF1Div.innerHTML = newInner;
    }
}

function listAllDeptInfo(){
    const Http = new XMLHttpRequest();
    const url = '/api/F2';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=( e )=>{
        if ( Http.readyState != 4 ) return;
        var response = Http.response;
        var allDeptInfoDiv = document.getElementById( "allDeptInfoDiv" ); 
        var keys = Object.keys(JSON.parse(response));
        allDeptInfoDiv.className = "scrollingTable";
        var numElements = (keys.length + 3 > maxNumDisplayed) ? maxNumDisplayed : keys.length + 3;
        allDeptInfoDiv.style.height = numElements * 20;
        var newInner = Table.toHtmlFromJson( response, "All department info" );
        allDeptInfoDiv.innerHTML = newInner;
    }
}

function listStudCountPerInst(){
    const Http = new XMLHttpRequest();
    const url = '/api/F3';

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=( e )=>{
        if ( Http.readyState != 4 ) return;
        var response = Http.response;
        var divToWorkWith = document.getElementById('studCountPerInstDiv');
        var keys = Object.keys(JSON.parse(response));
       divToWorkWith.className = "scrollingTable";
       var numElements = (keys.length + 3 > maxNumDisplayed) ? maxNumDisplayed : keys.length + 3;
       divToWorkWith.style.height = numElements * 20;
        var newInner = Table.toHtmlFromJson( response, "Instructor and student count" );
        divToWorkWith.innerHTML = newInner;
    }
}