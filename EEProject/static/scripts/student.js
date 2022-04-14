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
        console.log(response);
        if (keys.length <= 0) { 
            var opt = document.createElement('option');
            opt.value = null;
            opt.innerHTML = "No Depts available";
            deptDropDown.appendChild(opt);
            return; 
        }

        var L = deptDropDown.options.length - 1;
        for( var i = L; i >= 0; i--) {
           deptDropDown.remove(i);
        }

        for (var i = 0; i < keys.length; i++){
            var deptName = jsonResp[keys[i]]['dept'];
            var opt = document.createElement('option');
            opt.value = "dept=" + deptName;
            opt.innerHTML = deptName;
            deptDropDown.appendChild(opt);
        }

        //var newInner = Table.toHtmlFromJson( response, "All department info" );
        //allDeptInfoDiv.innerHTML = newInner;
    }
}

function getAllSections(){
    const Http = new XMLHttpRequest();
    var deptDropDown = document.getElementById( "deptDropDown" );

    const url = '/api/getAllDepts';

    Http.open("GET", url);
    Http.send();
}