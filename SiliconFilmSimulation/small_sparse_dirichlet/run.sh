#!/bin/bash

input_file="parameter.json"
output_dir="result"

rm -rf ./$output_dir/*
PolyFEM_bin -j $input_file -o $output_dir