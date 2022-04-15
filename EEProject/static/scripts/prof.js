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
        var jsonResp = JSON.parse(response);
        var keys = Object.keys( jsonResp );
        var F4Div = document.getElementById( "allSecInfoDiv" );
        if ( keys.length <= 0 ) { 
            F4Div.className = "";
            F4Div.innerHTML = "No classes and/or students registered for this semester and year"; 
            return; 
        }

        F4Div.className = "scrollingTable";
        F4Div.style.height = (keys.length + 3) * 20;
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

        var L = courseDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
           courseDropDown.remove(i);
        }

        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "You have no classes registered in the teaches table!";
            courseDropDown.appendChild(opt);
            return; 
        }

        for (var i = 0; i < keys.length; i++){
            var courseID = jsonResp[keys[i]]['courseID'];
            var opt = document.createElement('option');
            opt.value = courseID;
            opt.innerHTML = courseID;
            courseDropDown.appendChild(opt);
        }
        updateSections();
    }
}

function updateSections(){
    const Http = new XMLHttpRequest();
    var courseDropDown = document.getElementById("courseDropDown");
    var secDropDown = document.getElementById("sectionDropDown");
    
    const url = '/api/getAllInstSections?courseID=' + courseDropDown.value;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);

        var L = secDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
           secDropDown.remove(i);
        }

        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "No sections available";
            secDropDown.appendChild(opt);
            return; 
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

        generateStudentsTable();
    }
}

function generateStudentsTable(){
    const Http = new XMLHttpRequest();

    var secDropDown = document.getElementById("sectionDropDown");
    var studsDiv = document.getElementById("allStudsInSecDiv");
    
    const url = '/api/F5' + secDropDown.value
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);
        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            studsDiv.className = ""
            studsDiv.innerHTML = "No Students in this section";
            return; 
        }

        studsDiv.className = "scrollingTable";
        studsDiv.style.height = (keys.length + 3) * 20;
        var newInner = Table.toHtmlFromJson( response, "Students" );
        studsDiv.innerHTML = newInner;
    }
}