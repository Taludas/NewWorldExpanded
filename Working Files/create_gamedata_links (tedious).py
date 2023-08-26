import os

def generate_textfile_content(x, y, z, a, b, extension):
    if extension == 'ctt':
        content = f"data/sessions/islands/pool/moderate/{x}/_gamedata/{x}_river_01/{y}/{z}/{a}x{b}.ctt"
    else:
        content = f"data/sessions/islands/pool/moderate/{x}/_gamedata/{x}_river_01/{y}/{z}/{a}x{b}.dds"
    return content

def create_textfiles(x, y, z_values, a_b_ranges):
    for z in z_values:
        subfolder_path = os.path.join(y, z)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        if z in a_b_ranges:
            (a_start, a_end), b_start_dict, b_end_dict = a_b_ranges[z]

            for a in range(a_start, a_end + 1):
                b_start = b_start_dict.get(a, 0)
                b_end = b_end_dict.get(a, 0)
                for b in range(b_start, b_end + 1):
                    extension = 'ctt' if y == 'normalmaps' else 'dds'
                    filename = os.path.join(subfolder_path, f"{a}x{b}.{extension}.lnk")
                    content = generate_textfile_content(x, y, z, a, b, extension)
                    with open(filename, 'w') as file:
                        file.write(content)

def main():
    x = input("Enter the value for x (island_name): ")

    z_start = int(input("Enter the start value for z: "))
    z_end = int(input("Enter the end value for z: "))
    z_values = list(map(str, range(z_start, z_end + 1)))

    a_b_ranges = {}
    for z in z_values:
        a_start = int(input(f"Enter the start value for a with z={z}: "))
        a_end = int(input(f"Enter the end value for a with z={z}: "))
        
        b_start_dict = {}
        b_end_dict = {}
        for a in range(a_start, a_end + 1):
            b_start = int(input(f"Enter the start value for b with a={a} and z={z}: "))
            b_end = int(input(f"Enter the end value for b with a={a} and z={z}: "))
            b_start_dict[a] = b_start
            b_end_dict[a] = b_end
        
        a_b_ranges[z] = ((a_start, a_end), b_start_dict, b_end_dict)

    for y in ['normalmaps', 'tintmaps']:
        create_textfiles(x, y, z_values, a_b_ranges)
    
    print("Text files generated successfully!")

if __name__ == "__main__":
    main()
