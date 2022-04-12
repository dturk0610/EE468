class Table{
    constructor(rowCount, columnCount){
        this.rowCount = rowCount;
        this.columnCount = columnCount;
    }
    static fromJson( json ){
    }
    static fromDict( dict ){

    }
    data(){
        this.data = data;
    }
    toHtml(){
        var res = "<table>";

        res += "</table>"
        //<div><div>Column 4</div><div>Column 4</div></div>
    }

    //https://stackoverflow.com/questions/8232713/how-to-display-scroll-bar-onto-a-html-table
    static toHtmlFromJson( json, tableName ){
        var res = "<div>\n<div>\n<table>\n";
        res += "<caption>" + tableName + "</caption>\n";
        res += "<thead>\n<tr>\n";
        var objs = JSON.parse( json );
        var temp = Object.keys(objs);
        var columns = Object.keys(objs[temp[0]]);
        for ( var i = 0; i < columns.length; i++ ){
            res += "<th><div><div>"+columns[i]+"</div><div>"+columns[i]+"</div></div></th>\n";
        }
        res += "<th class=\"scrollbarhead\"/>\n";
        res += "</tr>\n</thead>\n";
        res += "<tbody>\n";
        for (var i = 0; i < temp.length; i++){
            var curr = objs[temp[i]];
            res += "<tr>";
            for (var j = 0; j < columns.length; j++){
                res += "<td>" + curr[columns[j]] + "</td>";
            }
            res+="</tr>\n"
        }
        res += "</tbody>\n";
        res += "</table>\n</div>\n</div>";
        return res;
        //<div><div>Column 4</div><div>Column 4</div></div>
    }
}