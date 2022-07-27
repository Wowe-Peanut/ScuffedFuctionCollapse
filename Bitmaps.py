from PIL import Image
import os




class Tilemap:
    def __init__(self, tileset_name, size):

        #Read-in all images from tileset
        self.tile_images = []
        directory = os.path.join(r"C:\Users\Peanu\OneDrive\Desktop\WFC\ScuffedFuctionCollapse\Tilesets", tileset_name)
        for filename in os.listdir(directory):
            image = Image.open(os.path.join(directory, filename))

            for s in range(int(filename[filename.index("-")+1])):
                self.tile_images.append(image.rotate(s*90))

        self.tile_size = self.tile_images[0].size[0]
        self.size = size
        print(len(self.tile_images))
        #Create Adjacency Rules
        self.valid_neighbors = []
        tl = self.tile_size
        edges = [[tl-1, tl//2],[tl//2, 0],[0, tl//2],[tl//2, tl-1]]
        
        for current in range(len(self.tile_images)):
            current_valid_neighbors = []
            current_image_pixels = self.tile_images[current].load()

            for d in range(4):
                direction_valid_neighbors = []
            
                for comparison in range(len(self.tile_images)):
                    comparison_image_pixels = self.tile_images[comparison].load()
                    
                    if current_image_pixels[edges[d][0], edges[d][1]] == comparison_image_pixels[edges[(d+2)%4][0], edges[(d+2)%4][1]]:
                        direction_valid_neighbors.append(comparison)
                
                current_valid_neighbors.append(direction_valid_neighbors)
            

            self.valid_neighbors.append(current_valid_neighbors)
                    

        #Initialize Bitmap (Each position will have a superposition: A list of possible positions): A map of tile indexes or possible indexes
        self.bitmap = [[[i for i in range(len(self.tile_images))] for c in range(size[1])] for r in range(size[0])]
        

                               
    def draw(self, scale=5):
        output = Image.new("RGB", (self.size[0]*self.tile_size, self.size[1]*self.tile_size))

        for r in range(len(self.bitmap)):
            for c in range(len(self.bitmap[0])):
                if type(self.bitmap[r][c]) != int:
                    continue
                    
                output.paste(self.tile_images[self.bitmap[r][c]], (r*self.tile_size, c*self.tile_size))

        output.resize((output.size[0]*scale, output.size[1]*scale), Image.Resampling.NEAREST).show()

knots = Tilemap("Knots", (13, 13))

knots.draw(5)




