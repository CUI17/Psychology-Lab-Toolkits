#Author: Lee Cui aka #鬼才小17
#2019/04/23


from PIL import Image, ImageDraw, ImageFont



def drawImage(newImg, text, showImage=False):
    text = str(text)
    draw = ImageDraw.Draw(newImg)
    imgSize = newImg.size

    #设置字体格式
    fontSize = 115
    fnt = ImageFont.truetype('song.ttf', fontSize)
    fntSize = fnt.getsize(text)
    while fntSize[0] > imgSize[0] or fntSize[0] > imgSize[0]:
        fontSize -= 5
        fnt = ImageFont.truetype('song.ttf', fontSize)
        fntSize = fnt.getsize(text)

    x = (imgSize[0] - fntSize[0]) / 2
    y = (imgSize[1] - fntSize[1]) / 2

    # fill内部数值为字体颜色（RBG格式）可以更改
    draw.text((x, y), text, font=fnt, fill=(255, 255, 0))

#显示图片的判断
    if showImage:
        newImg.show()
    del draw


def newImage(width, height, text='default', color=(0, 0, 0, 0), show_image=False):
    newImg = Image.new('RGBA', (int(230), int(118)), color)
    drawImage(newImg, text, show_image)
    newImg.save(r'%s%s%s.png' % (type, num, textColor))
    del newImg


def newImageWithFile(fn):
    with open(fn, encoding='utf-8') as f:
        for l in f:
            l = l.strip()
            if l:
                ls = l.split(',')
                if '#' == l[0] or len(ls) < 2:
                    continue

                newImage(*ls)


#命名格式，现有格式为 组别首字母+数字序号+颜色编码（e.g p1r，意思为第一张红色的痛觉相关词汇，可以根据需要修改
type='c'

#num为名字里的数字编号，每生成一张图片加一次一（自增）
num=0
textColor='y'

#需要显示的文字内容，可在列表中修改
textList=["欢迎","使用"]

for text in textList:

        print(text)
        num+=1

        #show_image=True，则运行时立即显示生成的图片, 可改为False
        newImage(230,118,text,show_image=True)


