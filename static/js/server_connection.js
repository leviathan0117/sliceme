function makeCompileRequest() {
    let code = editor.getValue()
    $.ajax({
        url: '/api/request/',
        method: 'POST',
        data: {code: code},
        success: function (d) {
            //console.log(d);
        },
        error: function (d) {
            //console.log(d);
        }
    });
}