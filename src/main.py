from func import *

json_load = open_json()

sort_ex = sorting_by_executed(json_load)

sort_five = sorting_by_five_last_string(sort_ex)

#print(sort_five)

print(len(sort_five))

out_trans = output_trans(sort_five)
#format_list = format_data(sort_five)
#print(format_list)
#print(output_trans)

for i in out_trans:
    print(i)