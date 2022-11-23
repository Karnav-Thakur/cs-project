from PIL import Image,ImageDraw,ImageFont
import textwrap
# img = Image.open('./templates/letterhead.jpg')

img = Image.open('./templates/template.png')

I1 = ImageDraw.Draw(img)
font = ImageFont.truetype('./templates/times.ttf',24)

string = 'hello'
I1.text((300,27),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is name column
I1.text((280,60),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is age column
I1.text((400,93),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is mobile phone column
I1.text((150,182),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is diagnosis column
I1.text((25,300),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is medicine coloumn
I1.text((300,300),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is dosage column
I1.text((550,300),"\n".join(textwrap.wrap(string,10)),fill=(0,0,0),font=font) # this is freq column



# I1.text((100, 250), "Medicine", fill=(0, 0, 0),font=font)
# I1.text((300, 250), "Dosage", fill=(0, 0, 0),font=font)
# I1.text((500, 250), "Time-Freq.-Duration", fill=(0, 0, 0),font=font)

img.show()