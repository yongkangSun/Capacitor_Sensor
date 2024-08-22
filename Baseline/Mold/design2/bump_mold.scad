plate_size = [18, 15, 0.3];
mold_size = [10, 5, 0.2];
mold_coord = [4, 7, 0.2];

bump_size = 0.2;
bump_spacing = 0.5;
base = [6, 7, 0.2];

difference() {
    
    difference() {
        cube(plate_size);
        translate(mold_coord)
            cube(mold_size);
    };

    for (i=[1:1:11]) {
        for (j=[1:1:9]) {
            translate(base + [i * bump_spacing, j * bump_spacing, 0])
                cube(bump_size, center = true);
        }
    };
}