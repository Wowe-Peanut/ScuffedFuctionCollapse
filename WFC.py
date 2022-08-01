from PIL import Image
import os
import imageio
import random


class Tilemap:
    def __init__(self, tileset_name, size):

        
        
        #Read-in all images from tileset ----------------------------------------------------------------------------------------------------------------------------------
        self.tile_images = []
        directory = os.path.join(r"C:\Users\Peanu\OneDrive\Desktop\WFC\ScuffedFuctionCollapse\Tilesets", tileset_name)
        for filename in os.listdir(directory):
            image = Image.open(os.path.join(directory, filename))

            for s in range(int(filename[filename.index("-")+1])):
                self.tile_images.append(image.rotate(s*90))

        self.tile_size = self.tile_images[0].size[0]
        self.size = size

        #Create Adjacency Rules -------------------------------------------------------------------------------------------------------------------------------------------
        self.valid_neighbors = []
        tl = self.tile_size-1

        #Bottom, Left, Top, Right
        #3 Points per edge: (1, midpoint (floored), length-1)
        # Left to right for top and bottom, Top to bottom for left and right
        edges = [[[tl, 0],[tl, (tl+1)//2],[tl, tl]], [[0, 0],[(tl+1)//2,0],[tl,0]], [[0, 0],[0, (tl+1)//2],[0, tl]], [[0, tl],[(tl+1)//2, tl],[tl, tl]]][::-1]
        
        
        for current in range(len(self.tile_images)):
            current_valid_neighbors = []
            current_image_pixels = self.tile_images[current].load()

            for d in range(4):
                direction_valid_neighbors = []
            
                for comparison in range(len(self.tile_images)):
                    comparison_image_pixels = self.tile_images[comparison].load()

                    #Check if all three edge points match
                    valid = True
                    for edge in range(3):
                        if current_image_pixels[edges[d][edge][0], edges[d][edge][1]] != comparison_image_pixels[edges[(d+2)%4][edge][0], edges[(d+2)%4][edge][1]]:
                            valid = False

                    if valid:
                        direction_valid_neighbors.append(comparison)
                
                current_valid_neighbors.append(direction_valid_neighbors)
            

            self.valid_neighbors.append(current_valid_neighbors)
                    

        #Initialize Bitmap (Each position will have a superposition: A list of possible positions): A map of tile indexes or possible indexes -----------------------------
        self.bitmap = [[[i for i in range(len(self.tile_images))] for c in range(size[1])] for r in range(size[0])]


        #Variables for keeping track of progress
        self.total_tiles = self.size[0]*self.size[1]
        self.tiles_collapsed = 0

        #The bitmaps of each step are logged to be turned into 
        self.frames = []
    
    
    #Returns image formed from the bitmap using tile_images as a key-------------------------------------------------------------------------------------------------------               
    def get_bitmap_image(self, scale=5):
        output = Image.new("RGB", (self.size[1]*self.tile_size, self.size[0]*self.tile_size))

        for r in range(self.size[0]):
            for c in range(self.size[1]):
                if len(self.bitmap[c][r]) != 1:
                    continue
                    
                output.paste(self.tile_images[self.bitmap[c][r][0]], (c*self.tile_size, r*self.tile_size))

        return output.resize((output.size[0]*scale, output.size[1]*scale), Image.Resampling.NEAREST)


    #Return (x,y) of tile with the lowest entropy; choose randomly if values are tied -------------------------------------------------------------------------------------
    def lowest_entropy(self):

        min_entropy = float('inf')
        min_positions = []

        for r in range(len(self.bitmap)):
            for c in range(len(self.bitmap[0])):
                val = self.bitmap[r][c]
                if len(val) <= 1:
                    continue
                
                elif len(val) < min_entropy:
                    min_entropy = len(val)
                    min_positions = [(r,c)]
                    
                elif len(val) == min_entropy:
                    min_positions.append((r,c))

        
        return None if len(min_positions) == 0 else random.choice(min_positions)
        
            

    #Recursively propagates cells with constraints; Only called on a space when its superposition changes/collapses ------------------------------------------------------
    def propagate(self, r, c):
        
        #Removes all tiles in current superposition if they don't have a valid neighbor in each direction
        current = self.bitmap[r][c]
        directions = [[r,c+1], [r-1,c], [r, c-1], [r+1, c]]
        invalid_tiles = []

        #Identify Invalid Tiles
        for cur in current:
            for i, d in enumerate(directions):
                if 0 <= d[0] < self.size[0] and 0 <= d[1] < self.size[1]:
                    
                    #For each valid neighbor of current space, check if it has at least 1 in this direction
                    valid = False
                    for valid_neighbor in self.valid_neighbors[cur][i]:
                        if valid_neighbor in self.bitmap[d[0]][d[1]]:
                            valid = True
                            break

                    if not valid:
                        invalid_tiles.append(cur)
                        break
        #Remove Invalid Tiles
        for tile in invalid_tiles:
            if tile in self.bitmap[r][c]:
                self.bitmap[r][c].remove(tile)

        #If collapsed, incriment counter and save current bitmap
        if len(self.bitmap[r][c]) == 1:
            self.tiles_collapsed += 1
            self.frames.append(self.get_bitmap_image(3))

        #If current superposition updated or is already collapsed:
        if len(invalid_tiles) > 0 or len(current) == 1:

            #Propogate each surrounding cell if it is not already collapsed
            for d in directions:
                if 0 <= d[0] < self.size[0] and 0 <= d[1] < self.size[1]:
                    
                    if len(self.bitmap[d[0]][d[1]]) > 1:
                        self.propagate(d[0], d[1])
                    

    #Creates gif of self.frames and the "imageio" library -----------------------------------------------------------------------------------------------------------------
    def create_gif(self):

        #Add some buffer frames
        self.frames += [self.frames[-1] for i in range(20)]

        #Combine frames to gif and save to desktop with random name
        imageio.mimsave(r"C:\Users\Peanu\OneDrive\Desktop\{0}.gif".format(random.randint(0, 2**31-1)), self.frames, duration=0.01)

    
    #Runs the algorithm until it finishes or until it hits a contradiction ------------------------------------------------------------------------------------------------   
    def run(self):
        while self.tiles_collapsed < self.total_tiles:
            target = self.lowest_entropy()


            if not target:
                break
            #Collapse unit with lowest entropy (or tied for it)
            self.bitmap[target[0]][target[1]] = [random.choice(self.bitmap[target[0]][target[1]])]
            
    
            #Reflect changes in surrounding tiles and possibily collapse some
            self.propagate(target[0], target[1])
        
        
    
    
    
tilemap = Tilemap("Knots", (30, 30))
tilemap.run()
tilemap.get_bitmap_image(5).show()
tilemap.create_gif()







