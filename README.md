# labelImg_assistant
辅助labelImg进行快速标注的工具 
使用时只需要一直选框即可（同一label），不需要按“d”键
# 使用前提：
安装所需第三方库：  
pywinauto  
pynput  
# 使用流程：
### 使用前调试：  
1.全屏化labelImg软件  
2.修改变量“debug”为“True”  
3.运行本python程序，等待打印“开始”  
4.按“alt”+“tab”键切换到labelImg软件，点击labelImg内“NextImage”按钮  
5.查看打印数据，将next_img_pos全局变量修改成打印出来的鼠标坐标  
  
### 使用流程：    
1.labelImg的“use default labtel”选项勾选  
2.View的Auto save mode勾选上  
3.然后运行本python文件，等待对话框出现“开始”  
4.按“alt”+“tab”键切换到labelImg软件，按w开始标注
