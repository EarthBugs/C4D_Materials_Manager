#encoding = gbk

import c4d, os
from c4d import gui

c4d.CallCommand(12305, 12305)#打开控制台

print("Author @地球虫子 Homepage：space.bilibili.com/4708292\n \n \nScanning folders...")

####在这里填入后缀名####
####Input suffix of image files here####
suffix = ("png", "jpg", "jpeg", "bmp", "exr", "psd")

####在这里填入通道名####
####Input names of channels here####
channel_name = ("diffuse", "reflection", "height", "normal")


def main():
    
    #获取当前.py文件的位置
    root_path = os.getcwd()
    
    if not root_path:
        c4d.gui.MessageDialog("Please put this script in a correct path.")
        return
    
    #获取path目录下的文件夹
    sub_folders = list()#初始化用于存储文件夹的列表，避免循环结束后被删除
    
    #警告列表（存储导入中出现疑似错误的材质的列表）
    warnning_list = list()
    
    #该循环只进行一次，用于获取root_path路径中的文件夹列表
    for root in os.walk(root_path):
        sub_folders = root[1]#root的第1个元素为其中包含的文件夹
        break#只查到了walk配合循环的用法，只好这么用了
    
    print("%s%s%s" %("Detected folders:", sub_folders, "\n \n "))
    
    #遍历sub_folders中的子文件夹。sub_folders是文件夹内的子文件夹的列表
    for cur_folder in sub_folders:
        
        print("%s%s" %("Processing folder:", cur_folder))
        
        #创建并插入材质
        new_material = c4d.BaseMaterial(5703)#得到默认材质
        new_material.SetName(cur_folder)#材质名称更改为贴图所在文件夹的名称
        doc.InsertMaterial(new_material)#向文档中插入材质
        print("    %s%s" %("Material created:", cur_folder))
            
        #遍历文件夹中的文件。files是cur_folder内文件的列表。temp是占位符，用于指定循环的对象，这两项不会被使用
        for temp, temp, files in os.walk(cur_folder):
            
            #判断files是否为空（即判断文件夹是否为空）
            if files:#不为空
                
                #遍历files
                for image in files:
                    
                    print("    %s%s" %("Processing file:", image))
                    
                    #使用join函数将路径拼合
                    #root_path是.py文件所在目录，cur_folder是.py文件所在目录中子目录的名称，image是图像文件的名称
                    image_path = os.path.join(root_path, cur_folder, image)
                    
                    #判断该文件是否是图像文件。是则进入材质创建流程，否则开始下一轮循环
                    suffix_flag = 0#判断该文件后缀是否是与suffix某个元素吻合，全都不是则为0，是则为1
                    for cur_suffix in suffix:
                        
                        #该文件的后缀名与suffix列表中元素之一吻合，进入材质创建流程
                        if cur_suffix in image:
                            
                            suffix_flag = 1#后缀名吻合，更改flag
                            print("        %s%s%s" %("\"", image, "\" is a image file."))
                            
                            #判断该图像是否是贴图。是则进入贴图导入流程，否则开始下一轮循环
                            channel_flag = 0#判断该图片是否是某通道的图片，任何通道都不是则为0，是则为1
                            for cur_channel in channel_name:
                                
                                #通过检测该图像是否包含channel列表中的字串来判断是否是贴图
                                if cur_channel in image:
                                    
                                    channel_flag = 1#该图片是某通道的图片，更改flag
                                    print("            %s%s%s%s%s" %("\"", image, "\" is a image of \"", cur_channel, "\" channel."))
                                    
                                    print("%s%s" %("            Importing texture:", image))
                                    
                                    try:
                                        #新建shader并初始化
                                        shader = c4d.BaseShader(c4d.Xbitmap)
                                        shader[c4d.BITMAPSHADER_FILENAME] = image_path
                                    
                                    except BaseException:#导入出现错误
                                        print("%s%s" %("            Texture\"", image, "\"import failure !(texture skipped.)" ))
                                        break
                                    
                                    #先判断这是什么通道的文件，再将texture赋予new_material
                                    ####在这里添加通道！####
                                    ####Add channels here!####
                                    #diffuse通道
                                    if cur_channel == "diffuse":
                                        new_material[c4d.MATERIAL_USE_COLOR] = 1
                                        new_material[c4d.MATERIAL_COLOR_SHADER] = shader
                                        new_material.InsertShader(shader)
                                    #reflection通道
                                    if cur_channel == "reflection":
                                        new_material[c4d.MATERIAL_USE_REFLECTION] = 1
                                        new_material[c4d.REFLECTION_LAYER_COLOR_TEXTURE] = shader
                                        new_material.InsertShader(shader)
                                    #height通道
                                    if cur_channel == "height":
                                        new_material[c4d.MATERIAL_USE_BUMP] = 1
                                        new_material[c4d.MATERIAL_BUMP_SHADER] = shader
                                        new_material.InsertShader(shader)
                                    #normal通道
                                    if cur_channel == "normal":
                                        new_material[c4d.MATERIAL_USE_NORMAL] = 1
                                        new_material[c4d.MATERIAL_NORMAL_SHADER] = shader
                                        new_material.InsertShader(shader)
                                    
                                    c4d.EventAdd()#刷新视图
                                    
                                    break#该图片是某个通道的图片，跳出channel循环，不继续将图片与其他通道比对
                                
                            if channel_flag == 0:
                                print("            %s%s%s" %("\"", image, "\"is not an image of any channel !(file skipped.)"))#该图片不是任何通道的图片
                                warnning_list.append((cur_folder, image, "Is not an image of any channel !"))#向警告列表中添加本材质
                                
                            break#该文件是图像文件，跳出suffix循环，不继续将文件与其他后缀名比对
                        
                    if suffix_flag == 0:
                        print("        %s%s%s" %("\"", image, "\"is not a image file !(file skipped.)"))#该文件不是任何格式的图片
                        warnning_list.append((cur_folder, image, "Is not an image file!"))#向警告列表中添加本材质
                
            else:#files为空，向警告列表中添加本材质
                print("        %s%s%s" %("\"", cur_folder, "\"Is an empty folder !"))#files为空
                warnning_list.append((cur_folder, "Is an empty folder !"))#向警告列表中添加本材质
                    
        print("\n ")#在两个文件夹之间换行
        
        print("%s%s" %("Warning, textures listed bellow maybe have some problems:", warnning_list))
                    
if __name__=='__main__':
    main()