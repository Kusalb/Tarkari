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
font = ImageFont.truetype("Roboto-Regular-webfont.woff", 50)

# Opening the file gg.png
imageFile = "exchange-rate.png"
im1 = Image.open(imageFile)


# Drawing the text on the picture
draw = ImageDraw.Draw(im1)
date = str(NepaliDate.today())
print(date)
try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='tarkari',
                                              user='root',
                                              password='')
    sql_select_Query = "select * from money_list"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    i = 0
    for row in records:
        if (i < 33):
            draw.text((100, (500 + i * 80)), row[0], (0, 0, 0), font=font)
            draw.text((700, (500 + i * 80)), row[1], (0, 0, 0), font=font)
            draw.text((1100, (500 + i * 80)), row[2], (0, 0, 0), font=font)
            draw.text((1680, (500 + i * 80)), row[3], (0, 0, 0), font=font)

        else:
            break
        i += 1



    cursor.close()

    draw.text((1000, 200), date, (0, 0, 0), font=font)

    draw = ImageDraw.Draw(im1)

    # draw.text((100, 100)," लसुन सुकेको चाइनिज",(0,0,0),font=font)

    # Save the image with a new name
    im1.save("exchange_rate_printed.png")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if (mySQLconnection.is_connected()):
        mysql.connection.close()
        print("MySQL connection is closed")
