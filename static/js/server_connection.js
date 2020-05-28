function test_function1() {
    $.ajax({
        url: '/api/request/',
        method: 'POST',
        data: {id: 'A', value: '1'},
        success: function (d) {
            console.log(d);
        },
        error: function (d) {
            console.log(d);
        }
    });
}

function test_function2() {
    $.ajax({
        url: '/api/request/',
        method: 'POST',
        data: {id: 'B', value: '2'},
        success: function (d) {
            console.log(d);
        },
        error: function (d) {
            console.log(d);
        }
    });
}

function test_function3() {
    $.ajax({
        url: '/api/request/',
        method: 'GET',
        data: {id: 'C', value: '3'},
        success: function (d) {
            console.log(d);
        },
        error: function (d) {
            console.log(d);
        }
    });
}

function makeCompileRequest() {
    let code = editor.getValue()
    let rule_array = code.split('\n')
    $.ajax({
        url: '/api/request/',
        method: 'POST',
        data: {
            rules: rule_array
        },
        success: function (d) {
            console.log(d);
        },
        error: function (d) {
            console.log(d);
        }
    });
}