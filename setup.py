import geolocation
import GeoAdd

# data of the form
# keys: building_stack, field_stack
# each has a triple nested list
# first nest useless, second nest houses each geo structures
# third nest describes structure in {'lat': ..., 'lng': ... } format (4x)
def handle_zone_data(info):
    keys = ['building_stack', 'field_stack']

    geostruct_list = []
    geo_corners = []
    geo_tiles = []

    for k in keys:
        if k not in info:
            continue
        info[k] = info[k][0]
        for structure in info[k]:
            if k == 'building_stack':
                geostruct_list.append('building')
            else:
                geostruct_list.append('field')
            points = []
            tiles = []
            for lat_lng_dict in structure:
                lat = lat_lng_dict['lat']
                lng = lat_lng_dict['lng']
                xt, yt = geolocation.deg_to_tile(lat, lng, zoom=18)
                points.append([lat, lng])
                tiles.append([xt, yt])
        geo_corners.append(points)
        geo_tiles.append(tiles)

    # list of length n which gives id for each
    GeoAdd.addAllGeo(geostruct_list, geo_corners, geo_tiles)

    return geo_corners[0][0] # to take the user to
