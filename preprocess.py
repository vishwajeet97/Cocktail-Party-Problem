import utilities as utl

# Read the images stored in ./images/original
names = ["baboon", "lena", "peppers"]
images = utl.listImages(names, "original", False)


# Plot the orginal images which are colored
utl.plotImages(images, names, "original", False)

# Plot the images after they are resized and converted to black and white
images = utl.listImages(names, "original", True)
utl.plotImages(images, names, "blackNwhite", True, False)

# Save the black and white images in ./images/bnw
# Uncomment the below line to save the images
# utl.saveImages(images, names, "bnw")

# Plot the histogram of each image
utl.showHistogram(images, names, "bnw_histogram", False)