#!/bin/bash

input_file="sheet_5_remesh.off"

output_dir="./result_5"

tetgen -pq2.2a0.01g $input_file

base_name=$(basename $input_file .off)

mv ${base_name}.1.* $output_dir