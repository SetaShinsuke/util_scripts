// site: https://www.iimh.net/
var imgs = document.getElementById('viewimages').getElementsByTagName('img');
var a = [];
var tasks = [];
for(var i=0;i<imgs.length;i++){
    if(i === 0){
        continue;
    }
    var img = imgs[i];
    var subStr = img.src.split('/');
    var fileName = subStr[subStr.length - 1];
    a.push(fileName);
    tasks.push({'file_name': (i + '.jpg'), 'url': img.src, 'page': i});
}

var taskJson = {'补充': tasks};
console.log(taskJson);

function copyToClipboard(text) {
    console.log("Start copy...");
    var el = document.createElement('textarea');
    el.value = text;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    console.log("Copied!");
}

copyToClipboard(JSON.stringify(taskJson));