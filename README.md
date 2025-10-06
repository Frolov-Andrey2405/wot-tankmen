# World of Tanks - Tankmen

This script automates the resizing and renaming of crew member images for World of Tanks modding. It processes all images in the specified input folder, resizes each image to three different widths, and saves them in corresponding output folders for each country.

## Features

- **Batch Processing:** Automatically processes all PNG, JPG, and JPEG images in the input folder.
- **Multiple Sizes:** Resizes each image to three widths: 100px (small), 188px (big), and 100px (barracks).
- **Country Variants:** Generates copies for every country in the provided country list.
- **Automatic Directory Creation:** Ensures output directories exist before saving images.
- **Consistent Naming:** Output files are named in the format `{country}-{index}.png`.

## Folder Structure

```cmd
crew/                          # Input folder with original images
gui/maps/icons/tankmen/icons/  # Output folders for resized images
    ├── small/
    ├── big/
    └── barracks/
```

## Usage

1. **Prepare Images:**

    - Place your crew member images in the `crew` folder. Supported formats: PNG, JPG, JPEG.

2. **Install Dependencies:**

    - Install all required Python packages using:

        ```cmd
        pip install -r requirements.txt
        ```

    - The main dependency for image processing is [Pillow](https://pillow.readthedocs.io/en/stable/?badge=latest).

3. **Run the Script:**

    - Execute the script:

        ```cmd
        python main.py
        ```

4. **Result:**

    - Resized and renamed images will be saved in the respective output folders:
        - `gui/maps/icons/tankmen/icons/small`
        - `gui/maps/icons/tankmen/icons/big`
        - `gui/maps/icons/tankmen/icons/barracks`

## Installation

Copy the "gui" folder to `World_Of_Tanks/res_mods/x.x.x.x/` (x - current patch number).

## Configuration

You can change the input and output folder paths or the list of countries by editing the following variables in `main.py`:

```python
input_folder = "crew"
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
```

## Example Output

For each image in `crew/`, the script will generate files like:

- `china-1.png`, `china-2.png`, ..., `china-46.png`
- `czech-1.png`, `czech-2.png`, ..., `czech-46.png`
- ...for each country in the list.

Each file will be present in all three output folders, resized accordingly.
