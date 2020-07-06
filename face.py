import faces

sad = open('downloads/Virat Kohli/1.Virat..Kohli.jpg', 'rb')
image = faces.FaceAppImage(file=sad)
happy = image.apply_filter('smile', cropped=True)

#bytes = readimage(path+extension)
#image = Image.open(io.BytesIO(bytes))
#image.save(savepath)

