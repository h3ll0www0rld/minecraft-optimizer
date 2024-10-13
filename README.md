# Minecraft-Optimizer
一个~~简陋~~高度自定义化的Modrinth模组批量下载器

# 如何使用
## 简单用法
将项目clone到本地，并下载依赖
```shell
pip install -r requirements.txt
```
然后将`main.py`移动到你的游戏目录下(即与.minecraft文件夹在同一目录中)<br>
在同一目录下新建`ModList.yaml`文件，然后根据你的Minecraft模组加载器，将仓库中`example`文件夹中对应的文件的所有内容复制到这个文件中(如：如果你的加载器是`fabric`，那就将仓库中的`example/fabric_optimize.yaml`中所有内容复制到你目录下的`ModList.yaml`中)<br>
最后运行
```shell
python main.py
```
并选择你的`版本隔离状态`和`Minecraft版本`，程序会自动进行下载

## 高级用法
如果你想要使用自己的模组列表，那么你可以通过修改`ModList.yaml`的内容来实现<br>
`ModList.yaml`中，`loader`对应你的模组加载器，`mods`为你的模组列表<br>
其中，`mods`下面的内容为你要添加的模组对应的一些信息，示例：
```yaml
mods:
  - name: Sodium # 模组名称
    type: Modrinth # 模组来源网站
    ID: AANobbMI # 可以通过在模组页面点击`Copy ID`获取
```
你也可以使用`imports`来导入在线配置，例如:
```yaml
imports:
  - https://raw.githubusercontent.com/h3ll0www0rld/minecraft-optimizer/refs/heads/main/example/fabric_optimize.yaml
```
