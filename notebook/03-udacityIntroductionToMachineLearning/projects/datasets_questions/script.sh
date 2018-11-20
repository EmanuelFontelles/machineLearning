#/bin/bash
cat '../final_project/poi_names.txt' | awk '{print $1";", $3" "$2}' | sed 's/,*\r*$//' > 'new_poi_names.txt'
