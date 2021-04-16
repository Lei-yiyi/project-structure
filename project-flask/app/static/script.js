// 调用后端服务

// 1. 配置 Ajax

// 客户端使用 ajax 技术请求服务端的服务
function ajaxError()
{
    alert('ajax error');
}  // 当 ajax 请求失败时，调用 ajaxError，提示用户 ajax 请求服务失败

function ajaxSuccess(result)
{
    if (result.error) {
        alert('操作失败');
        return;
    }
    location.reload();
}  // 当 ajax 请求成功时，调用 ajaxSuccess，提示用户 ajax 请求服务成功

// 2. 新增待做事项

// 点击 “新增” 按钮后，执行函数 onAddTodo(button)，button 指向的是 “新增” 按钮
function onAddTodo(button)
{
    var children = $(button).parent().children();  // $(button).parent()：指向按钮的父节点；$(button).parent().children()：表示 div 的 2 个子节点
    var title = children.eq(0).val();  // children.eq(0)：指向待做事项的文本框；children.eq(0).val()：待做事项的文本框的值
    var data = JSON.stringify({'title': title});

    $.ajax({
        'url': '/todos/add',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });  // 通过 JQuery 的 ajax 函数调用后端服务，设置 url 为 ‘/todos/add’、type 为 ‘POST’ ，表示新增一条待做事项
}

// 3. 更新待做事项

// 当用户完成一个待做事项后，将待做事项的 status 从 ‘todo’ 更改为 ‘done’
function onUpdateTodo(todoId) 
{
    var data = JSON.stringify({'todoId': todoId});
    
    $.ajax({
        'url': '/todos/update',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });  // 通过 JQuery 的 ajax 函数调用后端服务，设置 url 为 ‘/todos/update’、type 为 ‘POST’ ，更新待做事项的 status
}

// 4. 删除待做事项

function onDeleteTodo(todoId)
{
    var data = JSON.stringify({'todoId': todoId});

    $.ajax({
        'url': '/todos/delete',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': ajaxSuccess
    });  // 通过 JQuery 的 ajax 函数调用后端服务，设置 url 为 ‘/todos/delete’、type 为 ‘POST’ ，删除待做事项
}