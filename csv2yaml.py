#!/usr/bin/python3
import sys, os

def convert(from_file, model_name):
    try:
        in_file = open(from_file, "r")
        try:
            out_file = open(from_file.rstrip('.csv') + ".yaml", "w")
            fields = []
            line = 0
            for row in in_file:
                data = list(c.strip() for c in row.rstrip("\n").split(","))
                if line == 0:
                    fields.extend(data)
                else:
                    out_file.write("- model: {model_name}\n  pk: {pk}\n  fields:\n".format(model_name=model_name, pk=line))
                    for index in range(len(data)):
                        out_file.write("    {field_name}: {field_value}\n".format(field_name=fields[index], field_value=data[index]))
                    out_file.write("\n")
                line += 1
            in_file.close()
            out_file.close()
        except IOError:
            print("Error creating output file.")
    except IOError:
        print("Error reading CSV file. Make sure path is correct")


if len(sys.argv) != 3:
    print("usage: python csv2yaml.py <path-to-csv> <model-name>")
else:
    convert(sys.argv[1], sys.argv[2])
