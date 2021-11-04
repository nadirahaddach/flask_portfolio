from PIL import Image
import base64
from io import BytesIO
from pathlib import Path

def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


def s_image(path=Path("static/assets/"), simages=None):  # path of static images is defaulted
    if simages is None:  # color_dict is defined with defaults
        simages = [
            {'pic': "Football", 'info': "Go to Trimester 1 for more Information!", 'file': "connorfootball2.jpg"},
            {'pic': "Volleyball", 'info': "Go to Trimester 1 for girls, and Trimester 3 for boys for more Information!", 'file': "paigevolley.jpg"},
            {'pic': "Cheer", 'info': "Go to Trimester 1 for more Information!", 'file': "cheer.jpeg"},
            {'pic': "Cross Country", 'info': "Go to Trimester 1 for more Information!", 'file': "crosscountry.jpeg"},
            {'pic': "Dance", 'info': "Go to Trimester 1 for more Information!", 'file': "dance.jpeg"},
            {'pic': "Field Hockey", 'info': "Go to Trimester 1 for more Information!", 'file': "NatalieFieldHockey.jpg"},
            {'pic': "Golf", 'info': "Go to Trimester 1 for girls, and Trimester 3 for boys for more Information!", 'file': "girlsgolf.jpeg"},
            {'pic': "Tennis", 'info': "Go to Trimester 1 for girls, and Trimester 3 for boys more Information!", 'file': "tennis.jpeg"},
            {'pic': "Water Polo", 'info': "Go to Trimester 1 for boys, and Trimester 2 for girls for more Information!", 'file': "waterpolo.jpeg"},
            {'pic': "Basketball", 'info': "Go to Trimester 2 for more Information", 'file': "basketballjv.jpeg"},
            {'pic': "Soccer", 'info': "Go to Trimester 2 for more Information!", 'file': "soccerjv.jpeg"},
            {'pic': "Wrestling", 'info': "Go to Trimester 2 for more Information!", 'file': "wrestling.jpeg"},
            {'pic': "Rugby", 'info': "Go to Trimester 2 for more Information!", 'file': "prorugby.jpeg"},
            {'pic': "Lacrosse", 'info': "Go to Trimester 3 for more Information!", 'file': "lax.jpeg"},
            {'pic': "Baseball", 'info': "Go to Trimester 3 for more Information!", 'file': "baseball.jpg"},
            {'pic': "Softball", 'info': "Go to Trimester 3 for more Information!", 'file': "softball.jpeg"},
            {'pic': "Gymnastics", 'info': "Go to Trimester 3 for more Information!", 'file': "gymnastics.jpeg"},
            {'pic': "Swim & Dive", 'info': "Go to Trimester 3 for more Information!", 'file': "swim.jpeg"},
            {'pic': "Track and Field", 'info': "Go to Trimester 3 for more Information!", 'file': "track.jpeg"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for image in simages:
        # File to open
        filename = path / image['file']  # file with path

        # Image open return PIL image object
        img_object = Image.open(filename)

        # Python Image Library operations
        image['format'] = img_object.format
        image['mode'] = img_object.mode
        image['size'] = img_object.size

        # Hacks here for images https://www.tutorialspoint.com/python_pillow/index.htm
        # use the open img_object!!!
        img_object = img_object.rotate(0)
        image['base64'] = image_formatter(img_object, image['format'])
        # end for loop for pixels

    # end for loop for images
    return simages


