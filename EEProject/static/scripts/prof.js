function listAllSectionInfo(){
    const Http = new XMLHttpRequest();

    var semDropDown = document.getElementById("semDropDown");
    var yrDropDown = document.getElementById("yrDropDown");
    
    const url = '/api/F4?sem=' + semDropDown.value + "&year=" + yrDropDown.value;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var F4Div = document.getElementById( "allSecInfoDiv" );
        if (Object.keys(JSON.parse(response)).length <= 0) { 
            F4Div.className = "";
            F4Div.innerHTML = "No classes and/or students registered for this semester and year"; 
            return; 
        }

        F4Div.className = "scrollingTable";
        var newInner = Table.toHtmlFromJson( response, "Instructors" );
        F4Div.innerHTML = newInner;
    }

}