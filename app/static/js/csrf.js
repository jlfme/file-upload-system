// modify jquery ajax to add csrtoken when doing "local" requests
//
// $('html').ajaxSend(function(event, xhr, settings) {
//     function getCookie(name) {
//         var cookieValue = null;
//         if (document.cookie && document.cookie != '') {
//             var cookies = document.cookie.split(';');
//             for (var i = 0; i < cookies.length; i++) {
//                 var cookie = jQuery.trim(cookies[i]);
//                 // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//     //
//     // alert(settings.url);
//
//     if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//         // Only send the token to relative URLs i.e. locally.
//         xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//
//     }
// });


/**
 *首先在网页头部加上 <meta name="csrf-token" content="{{ csrf_token() }}">
 * 无论何时你发送 AJAX POST 请求，为其添加 X-CSRFToken 头:
 */

var csrftoken = $('meta[name=csrf-token]').attr('content');

$('html').ajaxSend(function(event, xhr, settings){

    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
    }
});
