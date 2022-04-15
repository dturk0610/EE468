function getAllDepts(){
    const Http = new XMLHttpRequest();
    var deptDropDown = document.getElementById( "deptDropDown" );

    const url = '/api/getAllDepts';

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=( e )=>{
        if ( Http.readyState != 4 ) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);

        var L = deptDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
           deptDropDown.remove(i);
        }

        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "No Depts available";
            deptDropDown.appendChild(opt);
            return; 
        }

        for (var i = 0; i < keys.length; i++){
            var deptName = jsonResp[keys[i]]['dept'];
            var opt = document.createElement('option');
            opt.value = deptName;
            opt.innerHTML = deptName;
            deptDropDown.appendChild(opt);
        }
        getAllClasses();
        //var newInner = Table.toHtmlFromJson( response, "All department info" );
        //allDeptInfoDiv.innerHTML = newInner;
    }
}

function getAllClasses(){
    const Http = new XMLHttpRequest();
    var deptDropDown = document.getElementById( "deptDropDown" );
    var classDropDown = document.getElementById( "classDropDown" );

    const url = '/api/getAllClassesForDept?dept=' + deptDropDown.value;

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=( e )=>{
        if ( Http.readyState != 4 ) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);

        var L = classDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
            classDropDown.remove(i);
        }

        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "No classes for this department";
            classDropDown.appendChild(opt);
            return; 
        }

        for (var i = 0; i < keys.length; i++){
            var className = jsonResp[keys[i]]['courseID'];
            var opt = document.createElement('option');
            opt.value = className;
            opt.innerHTML = className;
            classDropDown.appendChild(opt);
        }
        listAllSectionInfo();
    }
}

function listAllSectionInfo(){
    const Http = new XMLHttpRequest();
    var classDropDown = document.getElementById( "classDropDown" );
    var semDropDown = document.getElementById('semDropDown');
    var yrDropDown = document.getElementById('yrDropDown');
    var secDiv = document.getElementById('allCourseInDeptDiv');

    const url = '/api/F6?courseID=' + classDropDown.value + "&sem=" + semDropDown.value + "&year=" + yrDropDown.value;

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        if (Http.readyState != 4) return;
        var response = Http.response;
        var jsonResp = JSON.parse(response);
        var keys = Object.keys(jsonResp);
        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            secDiv.className = ""
            secDiv.innerHTML = "No Sections for this course, semester and year";
            return; 
        }

        secDiv.className = "scrollingTable";
        secDiv.style.height = (keys.length + 3) * 20;
        var newInner = Table.toHtmlFromJson( response, "Sections:" );
        secDiv.innerHTML = newInner;
    }
}