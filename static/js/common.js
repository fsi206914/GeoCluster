// Construct a jquery object representing a two-rows table
function generateTable(firstRowElements, secondRowElements, firstRowEnabled, secondRowEnabled) {
    var i;
    var firstRow = $('<div class="btn-group"></div>');
    for (i in firstRowElements) {
        firstRow.append($("<div class='btn btn-primary btn-number'" + ((firstRowEnabled && firstRowElements[i] != 0) ? "" : " disabled") + ">" + firstRowElements[i] + "</div>"));
    }
    
    var secondRow = $('<div class="btn-group"></div>');
    for (i in secondRowElements) {
        secondRow.append($("<div class='btn btn-danger btn-number'" + ((secondRowEnabled && secondRowElements[i] != 0) ? "" : " disabled") + ">" + secondRowElements[i] + "</div>"));
    }
    
    var table = $('<div></div>');
    table.append(firstRow);
    table.append($('<br/>'));
    table.append(secondRow);
    
    return table;
}

function generateBlock(table, title, stylename, number) {
    var html = $('<div></div>');
    html.append($('<div class="block_title"><span class="badge badge-inverse" style="min-width: 24px; text-align: center;">' + number + '</span><span class="badge badge-' + stylename + '">' + title + '</span></div>'));
    html.append(table);
    return html;
}

function select(target) {
    $(target).removeClass("btn-primary btn-danger").addClass("btn-inverse");
}

$(document).ready(function(){
    $('#btngroup_choosesize > .btn').click(function(e) {
        $('#modal_choosesize').modal("hide");
        init(parseInt(e.currentTarget.innerText));
    });
    $('#modal_choosesize').modal({backdrop: 'static', keyboard: false});
});
