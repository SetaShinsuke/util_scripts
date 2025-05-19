// https://www.manhuacat.com/manga/26871/270585.html

var bookName = document.getElementsByClassName('h2 text-center mt-3 ccdiv-m')[0].innerText;
var chapterName = document.getElementsByClassName('breadcrumb-item active')[0].innerText;
var imgs = Array.from(document.getElementsByClassName('img-content')[0].getElementsByTagName('img'));

var tasks = {'config': {'book_name': bookName}};
tasks['config']['referer'] = 'https://www.manhuacat.com';
tasks[chapterName] = [];

imgs.forEach( img => {
    var name = `${imgs.indexOf(img)}`.padStart(3, '0') + '.jpg';
    tasks[chapterName].push({'url': img.src, 'file_name': name});
});

console.log('Tasks size:');
console.log(tasks.length);

var taskIndex = parseInt(chapterName.split('卷')[0].replace('第',''));
var save_name = `tasks_${taskIndex}.json`;
console.log(save_name);
saveTextFile(JSON.stringify(tasks), save_name);

function saveTextFile(text, fileName) {
    var data = new Blob([text], {type: 'text/plain'});
    let textFile = window.URL.createObjectURL(data);

    var link = document.createElement('a');
    link.setAttribute('download', fileName);
    link.href = textFile;
    document.body.appendChild(link);

    // wait for the link to be added to the document
    window.requestAnimationFrame(function () {
        var event = new MouseEvent('click');
        link.dispatchEvent(event);
        document.body.removeChild(link);
    });

    return textFile;
}