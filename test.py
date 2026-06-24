org_list = ["tile_1", "tile_2"]
load_list = ["tile_1", "tile_2", "tile_3", "tile_4"]

for i, tile in enumerate(load_list):

    if i > len(org_list) - 1:
        org_list.append(tile)
    else:
        org_list[i] = tile

print(org_list)

