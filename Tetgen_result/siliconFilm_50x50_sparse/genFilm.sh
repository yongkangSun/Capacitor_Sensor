#!/bin/bash

input_file="film.poly"

output_dir="./result"

tetgen -pq1.2a0.5g $input_file

base_name=$(basename $input_file .poly)

mv ${base_name}.1.* $output_dir