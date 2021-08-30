# 使用说明
可以扒取多个网站的漫画数据，并支持导入 Tasks.json 手动添加下载任务
目前支持
- Tasks.json
- 有妖气
- 哔哩哔哩漫画
- 动漫之家、漫画柜、creativeuncut、爱看漫画等

## 一、手动导入 Tasks.json
1. 将 `tasks.json` 放在 `tasks` 目录（文件必须以“tasks”开头）  
    程序将依次执行 `tasks` 目录下所有的 `tasks_xxx.json` 文件  

2. 执行文件：  
    > /MangaCrawler/A_Site_General/crwaler_general.py

3. 根据提示，配置 Zip 打包
    - 输入回车、输入0：不打包
    - 输入数字: 把 `tasks_xxx.json` 文件中的 xxx 当作序号进行分组
    > eg:
    [ task_1.json, task_2.json, task_3.json ]
    ↓ step = 2
    [ task_1.json(1&2), task_2.json(3)]

- **分组的部分目前可能有 bug，遇见了再说**


Tasks.json 格式：
```text
{
  'config': {
    'book_name': '铁臂阿童木',
    'referer': 'xxx.xxx.com',
    'proxy': 'xxx.xxx:nnn'
    },
  'chapter1':[{
    'url': 'xxx.xxx.com/xxx.jpg',
    'file_name': '001.jpg'
    },{
    'url': 'xxx.xxx.com/xxx2.jpg',
    'file_name': '002.jpg'
    }...],
  'chapter2': [{
    ...
  }]

```


## 二、有妖气

1. 根据提示，输入漫画ID `https://www.u17.com/comic/53591.html` 中 `/comic/` 后面的ID

2. 输入开始、结束章节  
    **注意！这里的【开始章节】和【结束章节】不是章节名里的序号！**  
    **而是章节真正的 Index ！**

3. 将自动根据 [开始 - 结束] 进行打包 zip

### 自动分P说明：

- 每个章节下载到一个文件夹中
    > eg:  ..\ download \ 超合金社团-_1 \ [第一回, 第二回...]

- 每个 [开始章节 - 结束章节] 视为一个分P，将自动打包到一个 Zip 中，并将自动命名为 `章节名-index[start-end].zip`
    > eg: 超合金社团-01[1-10].zip

- 每个分P中包含多个章节的文件夹，文件夹名字后面的 -_1 的个数表示 P 数，如 `超合金社团-_1-_1` 打包后变 `超合金社团02.zip`
