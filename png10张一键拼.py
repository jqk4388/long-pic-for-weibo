from os import listdir
from PIL import Image
import math  

def pindange(result, ims, ims_size):
   # 拼接单个长图
   top = 0
   for i, im in enumerate(ims):
      mew_im = im.resize(ims_size[i], Image.ANTIALIAS)  # 等比缩放
      result.paste(mew_im, box=(0, top))
      top += ims_size[i][1] + jianju
   return(result)

kuan = 800
jianju = 10
geshi = 'png'
ims = [Image.open('./%s' % fn) for fn in listdir('./') if fn.endswith('.'+ geshi)]
yanse = (255,255,255)
n = len(list(ims)) #图片总数
fg = 10 #几张一条
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

