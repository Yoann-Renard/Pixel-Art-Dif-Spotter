from PIL import Image

def spot_dif(first_img, second_img, size) -> list(tuple()):
    difs = []
    for x in range(size[0]):
        for y in range(size[1]):
            if first_img[x, y] != second_img[x,y]:
                difs.append((x,y))
    print(f"{len(difs)} differences spoted !")
    """
    for coor in difs:
        print(f"x = {coor[0]} | y = {coor[1]}\n")
    """
    return difs

def show_dif(difs, first_img, size) -> None:
    new_img = Image.new(
        mode='RGBA',
        size=size
    )
    new_img_px = new_img.load()
    for x in range(size[0]):
        for y in range(size[1]):
            if first_img[x, y][3] - 150 < 0:
                opacity = 0
            else:
                opacity = first_img[x, y][3] - 150
            new_img_px[x, y] = (
                first_img[x, y][0],
                first_img[x, y][1],
                first_img[x, y][2],
                opacity
                )

    for dif in difs:
        new_img_px[dif[0], dif[1]] = (255,0,0,255)
    else:
        new_img.show()

def save_dif(difs) -> None:
    import json
    for dif in difs:
        dif = list(dif)
    dif_json = {
        "differences":difs
    }
    with open("differences.json", "w") as f:
        f.write(json.dumps(dif_json))
    print("differences.json created !")

if __name__ == "__main__":
    while True:
        first_file_path = input("""Path of the first image ?
        >> """)
        second_file_path = input("""Path of the second image ?
        >> """)

        try:
            with Image.open(first_file_path) as img:
                first_img_size = img.size
                first_img_px = img.load()
            with Image.open(second_file_path) as img:
                second_img_size = img.size
                second_img_px = img.load()
        except Exception as e:
            print(f"{e}\n")
        else:
            break

    if first_img_size != second_img_size:
        raise Exception("Both image must have the same resolution.")

    difs = spot_dif(first_img_px, second_img_px, first_img_size)

    if input("""do you want to display the differences (y/n) ?
    >> """) == "y":
        show_dif(difs, first_img_px, first_img_size)

    if input("""do you want to save the differences in a .json ? (y/n) ?
(differences.json will be overwrited if it already exist)
    >> """) == "y":
        save_dif(difs)

    input("""Thanks, see you next time !
Press 'ENTER' to leave.""")
    exit(0)

