import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"

export default function showMessage(message, state='error', callback_func) {
    let background_color;
    if (state == 'error') {
        // 设置错误提示时的背景颜色
        background_color = 'linear-gradient(to right, #ff5f6d, #ffc371)'
    } else {
        // 设置非错误提示时的背景颜色
        background_color = 'linear-gradient(to right, #00b09b, #96c93d)'
    }

    Toastify({
        text: message,  //弹出框提示信息
        duration: 2000,
        close: true,
        gravity: "top", // 提示框位置：`top` or `bottom`
        position: "center", // 提示框位置：`left`, `center` or `right`
        stopOnFocus: true, // 设置鼠标悬停：true，表示鼠标悬停在弹出框上时不关闭
        style: {
            background: background_color,
        },
        callback: function(){
            if (!callback_func) return ;
            if (callback_func) {
                callback_func()
            }
        },
        onClick: function(){
            alert('debug onclick')
        } // Callback after click
        }).showToast();
}