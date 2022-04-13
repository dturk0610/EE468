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
        var newInner = Table.toHtmlFromJson( response, "Num of students in each section" );
        F4Div.innerHTML = newInner;
    }

}

function getAllClasses(){
    const Http = new XMLHttpRequest();  

    var courseDropDown = document.getElementById("courseDropDown");
  
    const url = '/api/getAllClasses';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);
        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "You have no classes registered in the teaches table!";
            courseDropDown.appendChild(opt);
            return; 
        }

        var L = courseDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
           courseDropDown.remove(i);
        }

        for (var i = 0; i < keys.length; i++){
            var courseID = jsonResp[keys[i]]['courseID'];
            var opt = document.createElement('option');
            opt.value = courseID;
            opt.innerHTML = courseID;
            courseDropDown.appendChild(opt);
        }
    }
}

function updateSections(){
    const Http = new XMLHttpRequest();
    var courseDropDown = document.getElementById("courseDropDown");
    var secDropDown = document.getElementById("sectionDropDown");
    
    const url = '/api/getAllSections?courseID=' + courseDropDown.value;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);
        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "No sections available";
            secDropDown.appendChild(opt);
            return; 
        }

        var L = secDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
           secDropDown.remove(i);
        }

        for (var i = 0; i < keys.length; i++){
            var secID = jsonResp[keys[i]]['secID'];
            var sem = jsonResp[keys[i]]['sem'];
            var year = jsonResp[keys[i]]['year'];
            var opt = document.createElement('option');
            opt.value = "?courseID=" + courseDropDown.value + "&secID=" + secID + "&sem=" + sem + "&year=" + year;
            opt.innerHTML = "section: " + secID + " semester: " + sem + " year: " + year;
            secDropDown.appendChild(opt);
        }
    }
}