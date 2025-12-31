from PIL import Image
import os

def extract_colours(input_file):
    with Image.open(input_file) as img:
        
        #Find all unique colours
        colours = set()
        for pixel in img.getdata():
            colours.add(pixel)
        
        #Sorting to be neat
        sorted_colours = sorted(colours)
        
        #Might as well print the results
        print("\nColours:")
        print("#" * 30)
        for i, colour in enumerate(sorted_colours):
            hex_value = f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}"
            print(f"Colour {i+1:3d}: RGB({colour[0]:3d}, {colour[1]:3d}, {colour[2]:3d}) | HEX({hex_value})")

        #RGB output
        with open('resultrgb.txt', 'w') as rgb_file:
            for colour in sorted_colours:
                rgb_file.write(f"{colour[0]}, {colour[1]}, {colour[2]}\n")
        
        #HEX output
        with open('resulthex.txt', 'w') as hex_file:
            for colour in sorted_colours:
                hex_value = f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}"
                hex_file.write(f"{hex_value}\n")
    
    print(f"Processed {input_file}")
    print(f"Found {len(sorted_colours)} unique colours")
    print("RGB results saved to resultrgb.txt and HEX results saved to resulthex.txt")

if __name__ == "__main__":
    #Path to input
    input_file = input("Path to PNG: ").strip()
    
    #Verify
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
    elif not input_file.lower().endswith('.png'):
        print("Error: Needs to be in PNG format")
    else:
        extract_colours(input_file)