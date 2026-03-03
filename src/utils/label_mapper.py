LABEL_MAP = {
    "hamburger": "cheeseburger",
    "hot_dog": "hotdog",
    "french_fries": "fries"
    # add more mappings as needed
}

def normalize_label(dish_name):
    # Maps model output labels to supported dish names.
    return LABEL_MAP.get(dish_name, dish_name)