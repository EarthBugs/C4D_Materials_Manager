Author@地球虫子 Homepage:space.bilibili.com/4708292


This is a script for Cinema 4D, it can help you create materials and import textures easily and quickly.


HOW TO USE:

0.In the .py file, you can edit the suffix of image file, and the names of channels.You can lacate the suffix and channels` code by search ### in the .py file.

1.Be sure each channel`s image file cantains the channel name in its file name.(examples: 'xxx_diffuse.png' and '123-bump.tif' are OK)

2.Put each group of textures in their own folders(the names of these folders will be the names of the materials, and the folder name should not contain non English characters.)

3.Create a new folder, then put the .py file and the textures` folders(mentioned in 2) in a same folder, then run this script in C4D.


Here is a directory structure example:

Material(folder)
    |
    |-m1(folder)
    |-- |-m1_diffuse.tif(image file)
    |    |-m1_reflection.tif(image file)
    |    |-m1_height.tif(image file)
    |    |-m1_normal.tif(image file)
    |
    |-m2(folder)
    |-- |-m2_diffuse.tif(image file)
    |    |-m2_reflection.tif(image file)
    |    |-m2_height.tif(image file)
    |    |-m2_normal.tif(image file)
    |
    |-m3(folder)
    |-- |-m3_diffuse.tif(image file)
         |-m3_reflection.tif(image file)
         |-m3_height.tif(image file)
         |-m3_normal.tif(image file)

Then you will got materials named: m1, m2, m3