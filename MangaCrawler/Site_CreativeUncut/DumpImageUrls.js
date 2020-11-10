// site: https://www.creativeuncut.com/game-art-galleries.html

var break_line = "----n----"
var form = document.getElementById("gnav").nextElementSibling
var className = "gl"
if(form.className == "glry"){
    className = "th"
}
// var gls = document.getElementsByClassName("gbox")[0].getElementsByClassName("gl")
var gls = form.getElementsByClassName(className)
var url_strs = ""
var url_array = []
for(var i=0;i<gls.length;i++){
    var gl = gls[i]
    var a = gl.getElementsByTagName("a")[0]
    //console.log(a.text)
    if(a.text == "\nNext Art Gallery Page"){
        continue
    }
    // var href = a.href
    // console.log(i + ': ' + href)
    // var chars = href.split("/")
    // var url = href.replace(chars[chars.length-1], "art/" + chars[chars.length-1].replace(".html",".jpg"))
    // console.log(i + ": " + url)
    // console.log(url)
    // 新窗口打开
    // window.open(url, "_blank")
    // url_array.push(url)

    var s_img = a.getElementsByTagName("img")[0]
    var url = s_img.src.replace("_s.",".")
    s_img.src = url
    console.log(i + ": " + url)
    url_strs += (url + break_line)
}
// console.log(url_strs.replace(break_line, "\n"))
// 复制链接到粘贴板
// var input = document.getElementsByName("search")[0]
// input.value = url_strs
// input.select()
// document.execCommand("copy")


// url_array.forEach(function(url){
//         setTimeout(function(){
//             var a = document.createElement("a");
//             a.href = url;
//             var evt = document.createEvent("MouseEvents");
//             //the tenth parameter of initMouseEvent sets ctrl key
//             evt.initMouseEvent("click", true, true, window, 0, 0, 0, 0, 0,
//                                         true, false, false, false, 0, null);
//             a.dispatchEvent(evt);
//             console.log("url: " + url)
//         }, 3000);
//     });