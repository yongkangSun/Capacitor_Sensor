#!/bin/bash

input_file="sheet2.off"

output_dir="./result2"

tetgen -pq2.2a0.01g $input_file

base_name=$(basename $input_file .off)

mv ${base_name}.1.* $output_dir