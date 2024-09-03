#!/bin/bash

input_file="bumpsheet.obj"

output_dir="./result"

tetgen -pq1.2a0.1g $input_file

base_name=$(basename $input_file .off)

mv ${base_name}.1.* $output_dir