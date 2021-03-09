import matplotlib.pyplot as plt

labels = "PNG", "JPEG", "SVG", "GIF", "Other"
numImages = [376, 348, 153, 104, 19]
explode = (0.1, 0, 0, 0, 0)     # MUST have same # elements as x array (values to be charted)
wedgeColors = ('lightsteelblue', 'lightseagreen', 'indianred', 'slateblue', 'khaki')

fig1, ax1 = plt.subplots()
ax1.pie(numImages, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True,
            startangle=15, colors=wedgeColors)
ax1.axis('equal')   # Equal aspect ratio = circle drawn
plt.suptitle("Frequency of Image Formats on the Web", fontsize=18, c='tab:blue')

plt.show()
