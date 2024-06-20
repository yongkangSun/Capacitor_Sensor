#!/bin/bash

input_file="film.poly"

output_dir="./result"

rm -rf $output_dir/* 

tetgen -pq4.0a1.25g $input_file

base_name=$(basename $input_file .poly)

mv ${base_name}.1.* $output_dir