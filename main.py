"""
This script resizes and renames crew member images for World of Tanks modding
"""

import os
from PIL import Image


def resize_and_rename_images(
    input_folder,
    small_output_folder,
    big_output_folder,
    barracks_output_folder,
    country_list,
):
    """
    Resizes and renames images from the input folder for each country.
    - Creates output directories if they do not exist.
    - Processes all PNG, JPG, and JPEG images in the input folder.
    - For each image, resizes to three widths (100, 188, 100 pixels).
    - Saves resized images for each country with the format '{country}-{index}.png'.
    - Prints a message for each saved image.
    """
    # Ensure all output folders exist
    for folder in [small_output_folder, big_output_folder, barracks_output_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Get list of image files in the input folder
    images = [
        f
        for f in os.listdir(input_folder)
        if f.lower().endswith(("png", "jpg", "jpeg"))
    ]
    images.sort()

    # Process each image
    for index, image_name in enumerate(images, start=1):
        input_path = os.path.join(input_folder, image_name)

        with Image.open(input_path) as img:
            # Resize image to each target width and save for each country
            for width, output_folder in [
                (100, small_output_folder),
                (188, big_output_folder),
                (100, barracks_output_folder),
            ]:
                width_percent = width / float(img.width)
                new_height = int(float(img.height) * width_percent)
                img_resized = img.resize((width, new_height), Image.LANCZOS)

                # Save files for each country
                for country in country_list:
                    output_path = os.path.join(output_folder, f"{country}-{index}.png")
                    img_resized.save(output_path, format="PNG")
                    print(
                        f"{country}-{index}.png saved in {output_folder}: {width}x{new_height}"
                    )


if __name__ == "__main__":
    input_folder = "crew"  # Path to the folder with images
    small_output_folder = "gui/maps/icons/tankmen/icons/small"
    big_output_folder = "gui/maps/icons/tankmen/icons/big"
    barracks_output_folder = "gui/maps/icons/tankmen/icons/barracks"
    country_list = [
        "china",
        "czech",
        "france",
        "germany",
        "italy",
        "japan",
        "poland",
        "sweden",
        "UK",
        "usa",
        "ussr",
    ]
    resize_and_rename_images(
        input_folder,
        small_output_folder,
        big_output_folder,
        barracks_output_folder,
        country_list,
    )
