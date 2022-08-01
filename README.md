# ScuffedFuctionCollapse

  My attempt at a simple python version of mxgmn's "Wave Function Collapase" algorithm (see citations for link.) All code is completely my own and I didn't reference the code of the original github or any similar projects. Tilesets were the only thing taken directly from the original github (I'm no good at art.) Given a tileset labeled with the amount unique rotations each tile in the tileset has, the program is able to create a random image of a given size using the tiles in ways that they all connect logically to one another. The "speading" nature of the WFC algorithm reduces the chances of running into a tile contradiction much, much lower than if you were to simplely choose valid tiles randomly. The program has no functionality for taking a sample and subdividing it into NxN tiles to create a new image as the original github does. Nor does it have any sort of weighted random when choosing tiles which results in some images having strange distributions.



<h2>Examples</h2> (Again, tilesets are not my own, see citations):

<p float="left">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/knots.PNG" width="400">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/resizedKnotsGif.gif" width="400">
</p>

<p float="left">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/circuit.PNG" width="400">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/CircuitGif.gif" width="400">
</p>

<p float="left">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/FloorPlan.PNG" width="400">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/floorPlanGif1.gif" width="400">
</p>

<p float="left">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/rooms.PNG" width="400">
<img src="https://github.com/Wowe-Peanut/ScuffedFuctionCollapse/blob/main/Images%20and%20Gifs/RoomGif.gif" width="400">
</p>




<h1>Citations:</h1>

Python Libraries used: PILLOW, imageio, os, random

Original WFC Repo by Maxim Gumin: https://github.com/mxgmn/WaveFunctionCollapse

Explanitory Video by Martin Donald: https://www.youtube.com/watch?v=2SuvO4Gi7uY&t=492s&ab_channel=MartinDonald

All Tilesets used are from the Original WFC Repo






