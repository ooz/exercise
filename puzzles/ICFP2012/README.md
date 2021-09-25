# ICFP 2012

http://icfpcontest2012.wordpress.com/

Lightning entry:

 * Nothing special so far: just testing submission process:
    - A*, moving to closest lambda first (greedy), avoid dying at all costs
    - Algorithm ignores any flood information, so drowing is very likely

Plan:

 * Always remember a lift connection
 * Lambda cluster detection (getting greedy on clusters instead of single lambdas)
    - maybe: find optional "extraction point" for cluster
 * actively moving rocks, avoid final path blocking
 * maybe: evolutionary optimization of some parameters
 * MapImpact: classify actions that strongly (block paths) alter the map

 * Explicit earth clearing to move a rock


Malfunctioning robots:

 * Eve: let the robot write "EVE?" and run around in circles till he's out of moves
   if map too small: just move rocks and walk around
 * Highlander: Find a pile of rocks or build a pile of rocks and wait on top of it

