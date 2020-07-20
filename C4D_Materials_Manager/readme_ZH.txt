Author@地球虫子 
主页:space.bilibili.com/4708292


这是一个用来创建材质并导入贴图的C4D脚本。


使用方法：

0.在.py文件中搜索###即可定位到修改后缀名以及修改通道名的相关代码。你可以仿照这些代码的格式去添加后缀名或者通道。

1.确保每个通道的图像的文件名中包含通道的名称。（示例：“balabala_diffuse.png”和“123-bump.tif”都可以）

2.把每组图像放在单独的文件夹里。（文件夹名即为材质名，文件夹名需为全英文）

3.新建一个文件夹，把.py文件和上述每组材质的文件夹放在里面。


目录结构示例：

材质（文件夹）
    |
    |-m1（文件夹）
    |-- |-m1_diffuse.tif（图像文件）
    |    |-m1_reflection.tif（图像文件）
    |    |-m1_height.tif（图像文件）
    |    |-m1_normal.tif（图像文件）
    |
    |-m2（文件夹）
    |-- |-m2_diffuse.tif（图像文件）
    |    |-m2_reflection.tif（图像文件）
    |    |-m2_height.tif（图像文件）
    |    |-m2_normal.tif（图像文件）
    |
    |-m3（文件夹）
    |-- |-m3_diffuse.tif（图像文件）
         |-m3_reflection.tif（图像文件）
         |-m3_height.tif（图像文件）
         |-m3_normal.tif（图像文件）

这样就得到材质m1、m2、m3了。