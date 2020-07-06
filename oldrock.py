import faces

old_rockfeller = 'https://upload.wikimedia.org/wikipedia/commons/6/6f/John_D._Rockefeller_1885.jpg'
image = faces.FaceAppImage(url=old_rockfeller)
young_rockfeller = image.apply_filter('young')


