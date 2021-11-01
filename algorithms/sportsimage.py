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
            {'pic': "Football", 'file': "connorfootball2.jpg"},
            {'pic': "Field Hockey", 'file': "NatalieFieldHockey.jpg"},
            {'pic': "Basketball", 'file': "basketball.jpeg"},
            {'pic': "Volleyball", 'file': "volleyball.jpeg"},
            {'pic': "Soccer", 'file': "soccer.jpg"},
            {'pic': "Dance", 'file': "dance.jpeg"}
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


