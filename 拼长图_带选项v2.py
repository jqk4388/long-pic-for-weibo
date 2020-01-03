
from os import listdir
from PIL import Image
import math

def pinjiechangtu(ims , kuan , jianju, fg):
    yanse = (255,255,255)
    n = len(list(ims)) #图片总数
    m = math.ceil(n / fg) #长图条数
    ims_size = [list(im.size) for im in ims]
    # middle_width = sorted(ims_size, key=lambda im: im[0])[int(len(ims_size)/2)][0]  # 中位数宽度
    middle_width = kuan
    # 计算相对长图目标宽度尺寸
    for i in range(len(ims_size)):
        rate = middle_width/ims_size[i][0]
        ims_size[i][0] = middle_width
        ims_size[i][1] = int(rate*ims_size[i][1])\

    for i in range(1,m+1):
        sum_height = sum([im[1] + jianju for im in ims_size[fg*(i-1):fg*i]]) -jianju #计算总长度
        result = Image.new("RGB", (middle_width, sum_height), yanse) #新建空白长图
        result = pindange(result, ims[fg*(i-1):fg*i], ims_size[fg*(i-1):fg*i]) #拼接单个长图
        result.save('changtu'+ str(i) + '.jpg', quality=80) #存起来
    
    print('\n图片总数: ', n)
    print('分割条数: ', m)
    return

def pindange(result, ims, ims_size):
    # 拼接单个长图
    top = 0
    for i, im in enumerate(ims):
        mew_im = im.resize(ims_size[i], Image.ANTIALIAS)  # 等比缩放
        result.paste(mew_im, box=(0, top))
        top += ims_size[i][1] + jianju
    return(result)

def read_pic(geshi):
    ims = [Image.open('./%s' % fn) for fn in listdir('.') if fn.endswith('.'+ geshi)]
    return(ims)

geshi = input('请输入要拼的图片格式。随便输入jpg，不输png：')
width = input('输入长图宽，不输默认800：')
jianju = input('输入图片间距，不输默认10：')
fg = input('几张图片一条，不输默认10：')

if geshi == "":
    geshi = "png"
else:
	geshi = "jpg"

if width == "":
    width = 800
else:
    width = eval(width)

if jianju == "":
    jianju = 10
else:
    jianju = eval(jianju)

if fg == "":
    fg = 10
else:
    fg = eval(fg)

print('\n连页格式: ', geshi)
print('图片宽: ', width)
print('图片间距: ', jianju)
print('一条塞进'+ str(fg) +'张图')

pinjiechangtu(read_pic(geshi) , width , jianju, fg)

input('\n搞定了!')