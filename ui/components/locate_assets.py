import os

def locate_assets_dir():
    # Get the directory of the current file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Potential candidates for the assets directory
    candidates = [
        os.path.join(base_dir, "assets"),
        os.path.join(os.getcwd(), "assets")
    ]

    # Check the candidates first
    for c in candidates:
        if os.path.isdir(c):
            return c
    
    # If not found, traverse upwards to find "assets" directory
    current_dir = base_dir
    while True:
        assets_dir = os.path.join(current_dir, "assets")
        if os.path.isdir(assets_dir):
            return assets_dir
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            break
        current_dir = parent_dir
    # If not found, return None    
    return None

def asset_path(*parts):
    """
    Helper to get a file inside the discovered assets directory.
    Returns a path (string). If assets dir not found, joins relative to base_dir.
    """
    dir_ = locate_assets_dir()
    if dir_:
        return os.path.join(dir_, *parts)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", *parts)