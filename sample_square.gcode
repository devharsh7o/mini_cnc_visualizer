; Sample G-code: Draws a 20x20 mm square
G21         ; Set units to millimeters
G90         ; Absolute positioning

G0 X0 Y0    ; Rapid move to start point
G1 X20 Y0 F500 ; Linear move to (20,0) at feedrate 500
G1 X20 Y20     ; Linear move to (20,20)
G1 X0 Y20      ; Linear move to (0,20)
G1 X0 Y0       ; Linear move back to start

G0 Z5       ; Raise tool
M30         ; Program end
