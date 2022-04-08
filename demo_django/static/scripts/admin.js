function listAllProf(){
    console.log("YOYOYO");
    const Http = new XMLHttpRequest();
    const url = '/myapp/api/F1';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        document.getElementById("resDiv").innerHTML+=Http.response;
    }
}