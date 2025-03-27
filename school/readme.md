**如何使用**
1. pip install -r requirements.txt 安装依赖包
2. ![](img/img.png)
3. 输入自己在https://jw.gdsty.edu.cn/登录的账号密码


**AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'**

解决有两种方法
>方法一
> 
修改ddddocr的_init_.py文件，将其中的ANTIALIAS替换为新方法：

[//]: # (image = image.resize&#40;&#40;int&#40;image.size[0] * &#40;64 / image.size[1]&#41;&#41;, 64&#41;, Image.ANTIALIAS&#41;.convert&#40;'L'&#41;)
image = image.resize((int(image.size[0] * (64 / image.size[1])), 64), Image.LANCZOS).convert('L')

>方法二

pip uninstall -y Pillow
pip install Pillow==9.5.0