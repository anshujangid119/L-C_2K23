import csv, math
def read_input_file(filename):
    csv_data = []
    with open(csv_file, newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_data.append(row)
    return csv_data

def haversine_distance(center_x,center_y,point_x,point_y):
    latitude1 = center_x*math.pi/180
    longitude1 = center_y*math.pi/180
    latitude2 = point_x*math.pi/180
    longitude2 = point_y*math.pi/180
    distance_latitude = latitude2 - latitude1
    distance_longitude = longitude2 - longitude1
    haversine_angle = math.sin(distance_latitude / 2)**2 + math.cos(latitude1) * \
    math.cos(latitude2) * math.sin(distance_longitude / 2)**2
    angle = 2 * math.asin(math.sqrt(haversine_angle))
    distance = earth_radius * angle
    return distance

def cluster_mapping(csv_data,clusters):
    cluster_number = 1
    for data in csv_data:
        assigned = False
        for cluster in clusters:
            center_x, center_y = float(cluster[1]), float(cluster[2])
            point_x, point_y = float(data[1]), float(data[2])
            distance = haversine_distance(center_x,center_y,point_x,point_y)
            if distance <= radius:
                cluster.append(data[0])
                assigned = True
                break
        if not assigned:
            cluster_number += 1
            cluster_name = "clusters" + str(cluster_number)
            clusters.append([cluster_name, float(data[1]), float(data[2]), data[0]])
    return clusters

if __name__ == "__main__":
    earth_radius = 6371 
    radius_in_degrees = 10
    radius = (2 * math.pi * earth_radius * radius_in_degrees) / 360
    csv_file = "world_country_and_usa_states_latitude_and_longitude_values.csv"
    csv_data = read_input_file(csv_file)
    clusters = []
    first_cluster = csv_data[0]
    cluster_name = "cluster1"
    clusters.append([cluster_name, float(first_cluster[1]), float(first_cluster[2]), first_cluster[0]])
    csv_data.remove(first_cluster)
    final_clusters  = cluster_mapping(csv_data,clusters)  
    print("Total clusters are ",len(clusters))
    for data in final_clusters:
        print(data[0],":",data[3:])
        print("-"*100)