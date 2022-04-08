function listAllProf(){
    const Http = new XMLHttpRequest();

    var nameCheck = document.getElementById("orderName");
    var deptCheck = document.getElementById("orderDept");
    var salCheck = document.getElementById("orderSalary");
    var addToGET = "";
    if ( nameCheck.checked ) addToGET += nameCheck.value + ",";
    if ( deptCheck.checked ) addToGET += deptCheck.value + ",";
    if ( salCheck.checked ) addToGET += salCheck.value;

    const url = '/myapp/api/F1?orderByType=' + addToGET;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var profListF1Div = document.getElementById("resDiv");
        var newInner = Table.toHtmlFromJson( response, "Instructors" );
        profListF1Div.innerHTML = newInner;
    }
}