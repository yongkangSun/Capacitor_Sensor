#!/bin/bash

target_dir="20x20_sparse/dirichlet_y"
input_file="parameter.json"
output_dir="result"

rm -rf ./$target_dir/$output_dir/*
PolyFEM_bin -j ./$target_dir/$input_file -o ./$target_dir/$output_dir