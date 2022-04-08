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
        var columns = Object.keys(objs[0]['fields']);
        for ( var i = 0; i < columns.length; i++ ){
            res += "<th><div><div>"+columns[i]+"</div><div>"+columns[i]+"</div></div></th>\n";
        }
        res += "<th class=\"scrollbarhead\"/>\n";
        res += "</tr>\n</thead>\n";
        res += "<tbody>\n";
        objs.forEach( currObj => {
            var fields = currObj['fields']; // HERE IS THE REAL DATA WE ARE LOOKING FOR
            var keys = Object.keys( fields );
            res += "<tr>"
            for (var i = 0; i < keys.length; i++ ){
                res += "<td>" + fields[keys[i]] + "</td>";
            }
            res+="</tr>\n"

        });
        res += "</tbody>\n";
        res += "</table>\n</div>\n</div>";
        return res;
        //<div><div>Column 4</div><div>Column 4</div></div>
    }
}