bias = 0.1;

module base() {
    translate([13, 0, 0])
        cube([50, 50, 22.5]);
    translate([0, -10, 22.5 - 0.001])
        cube([50, 70, 52]);
}

module case() {
    difference () {
    cube([30 + 0.001, 62 + 0.001, 22]);
        
    translate([10, 0 - 0.001, 12])
        cube([20, 62 + 0.002, 10]);
    };
}


difference() {
    base();
    translate([20, -10 - 0.001, 33.5])
        case();
}