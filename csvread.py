import json
import csv


def print_json(title, obj):
    print("------------------")
    print(title)
    print("------------------")
    print(json.dumps(obj, indent=4))


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def conv_nums(line):
    for k, v in line.items():
        if line[k].isdigit():
            line[k] = int(line[k])
        elif isfloat(line[k]):
            line[k] = float(line[k])
    return line


def get_list(filename):
    f = open(filename, 'rb')
    reader = csv.DictReader(f, delimiter=',', quotechar='"')
    res_list = []
    for line in reader:
        line = conv_nums(line)
        res_list.append(line)
    f.close()
    return res_list


def album_by_id(a_albums, a_id):
    for a_album in a_albums:
        if a_album["Id"] == a_id:
            return a_album
    return None


people = get_list('inputs/people.csv')
albums = get_list('inputs/albums.csv')
people_albums = get_list('inputs/people_albums.csv')

print_json("PEOPLE", people)
print_json("ALBUMS", albums)
print_json("PEOPLE_ALBUMS", people_albums)

joined = []
for person in people:
    joined_person = {
        "Id":           person["Id"],
        "Firstname":    person["Firstname"],
        "Secondname":   person["Secondname"],
        "Albums":       []
    }

    for people_album in people_albums:
        if person["Id"] == people_album["PersonId"]:
            album = album_by_id(albums, people_album["AlbumId"])
            joined_person["Albums"].append(album)

    joined.append(joined_person)


print_json("EXPANDED", joined)


final_json = {
    "people": joined
}

print_json("EXPANDED_WITH_PROP", final_json)
