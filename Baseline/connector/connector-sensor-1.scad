bias = 0.18;

module case() {
    difference () {
        difference () {
            translate([bias, bias, bias])
                cube([30 - 2 * bias, 69.5 - 2 * bias, 22 - 2 * bias]);
                
            translate([10 - bias, 0 - bias, 10 - bias])
                cube([20 + bias, 69.5 + 2 * bias, 12 + bias]);
        };
        
        translate([10 - bias, 3 - bias, 9.4 - bias])
            cube([20 + 2 * bias, 63.5 + 2 * bias, 1 + 2 * bias]);
    };
}

translate([-bias, -bias, -bias])
    case();

translate([-30, 0, 0])
    cube([20 - bias, 69.5 - 2 * bias, 2]);