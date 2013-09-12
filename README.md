bbox
====

plugin for Quantum GIS which reports current bounding box and zooms to user-entered bounding box.

status
------

currently at 0.2, it works but is buggy.

usage
-----

the dialog box has an *input field,* a button to *update map* and a button to *close.*

the *input field* updates automatically to the bounding box of the map as you pan/zoom.

If you enter a bounding box into the *input field* and then click on *update map* the map pans/zooms to the specified bounding box.

The bounding box should be in the format:

  minX,minY:maxX,maxY
  
that is, the x,y coordinates of the bottom-left corner, then the x,y coordinates of the top-right corner.
