bias = 0.2;
screw_bias = 0.15;

module base() {
    screw_r = 2.4 + bias;
    screw_x = (28.26 - 4.8) / 2;
    screw_z = (46 - 4.8) / 2;
    
    
    difference() {
        cube([70, 16, 66], center = true);
        
        translate([screw_x, 0, screw_z])
            rotate([90, 0, 0])
            cylinder(h = 16 + 0.002, r=2.4 + bias, center = true);
        
        translate([screw_x, 0, -screw_z])
            rotate([90, 0, 0])
            cylinder(h = 16 + 0.002, r=2.4 + bias, center = true);
        
        translate([-screw_x, 0, -screw_z])
            rotate([90, 0, 0])
            cylinder(h = 16 + 0.002, r=2.4 + bias, center = true);
        
        translate([-screw_x, 0, screw_z])
            rotate([90, 0, 0])
            cylinder(h = 16 + 0.002, r=2.5 + bias, center = true);
    };
    
    translate([-35, -27, -17])
        cube([70, 35, 34]);
    
    translate([0, -16, 0])
        cube([12.26, 16, 66], center = true);
    
    translate([-28.87, -16, 0])
        cube([12.26, 16, 66], center = true);
    
    translate([28.87, -16, 0])
        cube([12.26, 16, 66], center = true);
    
}

module case() {
    difference () {
    cube([62 + 0.001, 30 + 0.001, 22]);
        
    translate([0 - 0.001, 0, 12])
        cube([62 + 0.002, 20, 10]);
    };
}


difference() {
    base();
    
    translate([-27, -27.001, -5.2])
        case();
}