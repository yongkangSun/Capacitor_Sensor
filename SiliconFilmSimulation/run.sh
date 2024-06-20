#!/bin/bash

target_dir="100x100x0.5_sparse/0_scale1e-3"
input_file="parameter.json"
output_dir="result"

rm -rf ./$target_dir/$output_dir/*
PolyFEM_bin -j ./$target_dir/$input_file -o ./$target_dir/$output_dir