# Minecraft-Optimizer
一个~~简陋~~高度自定义化的Modrinth模组批量下载器

# 如何使用
## 简单用法
将Release中的可执行文件下载下来，移动到你的游戏目录下(即与`.minecraft`文件夹在同一目录中)<br>
在同一目录下新建`ModList.yaml`文件，然后根据你的Minecraft模组加载器，将仓库中对应的文件的所有内容复制到这个文件中(如：如果你的加载器是`fabric`，那就将仓库中的`ModList_fabric.yaml`中所有内容复制到你目录下的`ModList.yaml`中)<br>
然后运行```
./mo.exe
```shell
并选择你的`版本隔离状态`和`Minecraft版本`，程序会自动进行下载

## 高级用法
如果你想要使用自己的模组列表，那么你可以通过修改`ModList.yaml`的内容来实现<br>
`ModList.yaml`中，`loader`对应你的模组加载器，`mods`为你的模组列表<br>
其中，`mods`下面的内容为你要添加的模组对应的`ID`，可以通过在模组页面点击`Copy ID`获取
