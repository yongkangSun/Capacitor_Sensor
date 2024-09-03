#!/bin/bash

input_file="cross_remesh_2.off"

output_dir="./result2"

tetgen -pq1.2a0.1g $input_file

base_name=$(basename $input_file .off)

mv ${base_name}.1.* $output_dir