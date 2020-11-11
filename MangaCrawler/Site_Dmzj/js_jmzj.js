var selectList = document.getElementById("page_select").children;
var tasks = [];
for(var i=0;i<selectList.length;i++){
    var item = selectList[i];
    if(!(item instanceof Option)){
        break;
    };
    var url = "http:" + item.value;
    var urlParts = url.split(".");
    var ext = "";
    if(urlParts.length > 0){
        ext = urlParts[urlParts.length - 1];
        ext = "." + ext;
    };
    var page = i+1;
    var fileName = ("00000" + page).slice(-3) + ext;
    tasks.push({'url': url, 'file_name': fileName, 'page': page});
};
var name = "manga_crawler";
var s = localStorage.getItem(name);
if(s==null){
    s = "{}";
};
var o = JSON.parse(s);
o[document.title] = tasks;
localStorage.setItem(name, JSON.stringify(o));
console.log("Start copy...");
var el = document.createElement('textarea');
el.value = localStorage.getItem(name);
document.body.appendChild(el);
el.select();
document.execCommand('copy');
document.body.removeChild(el);
console.log("Copied!")