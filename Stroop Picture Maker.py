#Author: Lee Cui aka #鬼才小17
#2019/04/23


from PIL import Image, ImageDraw, ImageFont



def draw_image(new_img, text, show_image=False):
    text = str(text)
    draw = ImageDraw.Draw(new_img)
    img_size = new_img.size

    font_size = 115
    fnt = ImageFont.truetype('song.ttf', font_size)
    fnt_size = fnt.getsize(text)
    while fnt_size[0] > img_size[0] or fnt_size[0] > img_size[0]:
        font_size -= 5
        fnt = ImageFont.truetype('song.ttf', font_size)
        fnt_size = fnt.getsize(text)

    x = (img_size[0] - fnt_size[0]) / 2
    y = (img_size[1] - fnt_size[1]) / 2

    # fill内部数值为字体颜色（RBG格式）可以更改
    draw.text((x, y), text, font=fnt, fill=(255, 255, 0))


    if show_image:
        new_img.show()
    del draw


def new_image(width, height, text='default', color=(0, 0, 0, 0), show_image=False):
    new_img = Image.new('RGBA', (int(230), int(118)), color)
    draw_image(new_img, text, show_image)
    new_img.save(r'%s%s%s.png' % (type, num, textColor))
    del new_img


def new_image_with_file(fn):
    with open(fn, encoding='utf-8') as f:
        for l in f:
            l = l.strip()
            if l:
                ls = l.split(',')
                if '#' == l[0] or len(ls) < 2:
                    continue

                new_image(*ls)


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
        new_image(230,118,text,show_image=True)


