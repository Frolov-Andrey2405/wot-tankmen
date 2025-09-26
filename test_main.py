import pytest
from PIL import Image

from main import (
    resize_and_rename_images,
)


def create_test_image(path, size=(200, 200), color=(255, 0, 0)):
    """Helper to create a dummy image for testing."""
    img = Image.new("RGB", size, color)
    img.save(path)


def test_resize_and_rename_images(tmp_path):
    # Setup: create input folder and some images
    input_folder = tmp_path / "input"
    input_folder.mkdir()
    for i in range(3):
        create_test_image(input_folder / f"image{i + 1}.png")

    # Output folders
    small_output_folder = tmp_path / "small"
    big_output_folder = tmp_path / "big"
    barracks_output_folder = tmp_path / "barracks"

    country_list = ["usa", "germany"]

    # Call the function
    resize_and_rename_images(
        str(input_folder),
        str(small_output_folder),
        str(big_output_folder),
        str(barracks_output_folder),
        country_list,
    )

    # Assertions: check that output folders exist
    for folder in [small_output_folder, big_output_folder, barracks_output_folder]:
        assert folder.exists()

    # Check that resized images exist for each country
    for index in range(1, 4):
        for country in country_list:
            small_file = small_output_folder / f"{country}-{index}.png"
            big_file = big_output_folder / f"{country}-{index}.png"
            barracks_file = barracks_output_folder / f"{country}-{index}.png"

            for f, expected_width in [
                (small_file, 100),
                (big_file, 188),
                (barracks_file, 100),
            ]:
                assert f.exists()
                with Image.open(f) as img:
                    assert img.width == expected_width


if __name__ == "__main__":
    pytest.main()
