import utilities as utl

# Read the images stored in ./images/bnw
names = ["baboon", "lena", "peppers"]
images = utl.listImages(names, "bnw", True)

# Getting mixed images
image1 = utl.mixImages(images, [0.23, 0.14, 0.35])
image2 = utl.mixImages(images, [0.32, 0.05, 0.17])
image3 = utl.mixImages(images, [0.07, 0.31, 0.25])

# Plot the mixed images
mnames = ["unos", "dos", "tres"]
mimages = [image1, image2, image3]
utl.plotImages(mimages, mnames, "mixed", True, False)

# Save the mixed images in ./images/mixed
# Uncomment the below line to save the images
# utl.saveImages(mimages, mnames, "mixed")

# Plot the histogram of mixed images
utl.showHistogram(mimages, mnames, "mixed_histogram", False)

