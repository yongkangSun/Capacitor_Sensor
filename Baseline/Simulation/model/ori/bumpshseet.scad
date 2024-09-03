mold_size = [100, 50, 2];

bump_size = 1.5;
bump_spacing = 5;
base = [20, 0, 2];

cube(mold_size);
    
for (i=[1:1:11]) {
        for (j=[1:1:9]) {
            translate(base + [i * bump_spacing, j * bump_spacing, 0])
                cube(bump_size, center = true);
        }
    };