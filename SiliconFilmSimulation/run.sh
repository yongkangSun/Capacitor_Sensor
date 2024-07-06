#!/bin/bash

target_dir="arvi_0624"
input_file="parameter.json"
output_dir="result_sheet1"

rm -rf ./$target_dir/$output_dir/*
PolyFEM_bin -j ./$target_dir/$input_file -o ./$target_dir/$output_dir