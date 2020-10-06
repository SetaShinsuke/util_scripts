var break_line = "----n----";
var form = document.getElementById("gnav").nextElementSibling;
var className = "gl";
if(form.className == "glry"){
    className = "th";
};
var gls = form.getElementsByClassName(className);
var url_strs = "";
var url_array = [];
for(var i=0;i<gls.length;i++){
    var gl = gls[i];
    var a = gl.getElementsByTagName("a")[0];
    if(a.text == "\nNext Art Gallery Page"){
        continue;
    };
    var s_img = a.getElementsByTagName("img")[0];
    var url = s_img.src.replace("_s.",".");
    s_img.src = url;
    url_strs += (url +break_line);
};
console.log(url_strs);

var site = document.URL.split("/");
var book_name = site[site.length-1].split(".")[0];
var input = document.getElementsByName("search")[0];
input.value = book_name;
input.value = url_strs;
input.select();
document.execCommand("copy");
console.log("book_name: " + book_name + "\nCopied!");