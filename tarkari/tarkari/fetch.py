# Importing the needed library

import PIL
import mysql.connector
from mysql.connector import Error
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from nepali_date import NepaliDate
# Loading Fonts….
# Note the following line works on Ubuntu 12.04
# On other operating systems you should set the correct path
# To the font you want to use.
font = ImageFont.truetype("mangal-1361510185.ttf", 55)

# Opening the file gg.png
imageFile = "tarkari-nepali.png"
im1 = Image.open(imageFile)
im2 = Image.open(imageFile)

# Drawing the text on the picture
draw = ImageDraw.Draw(im1)
draw1 = ImageDraw.Draw(im2)
date = str(NepaliDate.today())
print(date)
try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='tarkari',
                                              user='root',
                                              password='')
    sql_select_Query = "select * from t_list"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in python_developers is - ", cursor.rowcount)
    print("Printing each row's column values i.e.  developer record")
    i = 0

    for row in records:
        if (i < 33):
            draw.text((100, (500 + i * 80)), row[0], (0, 0, 0), font=font)
            draw.text((953, (500 + i * 80)), row[1], (0, 0, 0), font=font)
            draw.text((1250, (500 + i * 80)), row[3], (0, 0, 0), font=font)
            draw.text((1600, (500 + i * 80)), row[2], (0, 0, 0), font=font)
            draw.text((1900, (500 + i * 80)), row[4], (0, 0, 0), font=font)

        else:
            break
        i += 1

    j=0
    for row in records:
        if (j >= 33):
            draw1.text((100, (-2150 + j * 80)), row[0], (0, 0, 0), font=font)
            draw1.text((953, (-2150 + j * 80)), row[1], (0, 0, 0), font=font)
            draw1.text((1250, (-2150 + j * 80)), row[3], (0, 0, 0), font=font)
            draw1.text((1600, (-2150 + j * 80)), row[2], (0, 0, 0), font=font)
            draw1.text((1900, (-2150 + j * 80)), row[4], (0, 0, 0), font=font)
        j += 1

    cursor.close()

    draw.text((950, 200), date, (0, 0, 0), font=font)
    draw1.text((950, 200), date, (0, 0, 0), font=font)

    draw = ImageDraw.Draw(im1)
    draw1 = ImageDraw.Draw(im2)

    # draw.text((100, 100)," लसुन सुकेको चाइनिज",(0,0,0),font=font)

    # Save the image with a new name
    im1.save("Wholsale_tarkari1.png")
    im2.save("Wholsale_tarkarie2.png")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if (mySQLconnection.is_connected()):
        mysql.connection.close()
        print("MySQL connection is closed")
