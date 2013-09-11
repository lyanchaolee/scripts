#!/bin/bash

i=5
m_cnt=5
c_cnt=20
j=1

while [ "$i" -le "$m_cnt" ]; do
	
	while [ "$j" -le "$c_cnt" ]; do
		echo "http://administrator:hellop4p@hz-p4p-solr"$i".hst.xyi.en.alidc.net:8080/p4pkwsolr"$j"/update/json? -H \"Content-Type: text/json\"  --data-binary '{\"optimize\": { \"waitFlush\":false, \"waitSearcher\":false }}'"| xargs curl

		echo "hz-p4p-solr"$i".hst.xyi.en.alidc.net:8080/p4pkwsolr"$j" done"
		j=$((j+1))	
	done
	j=1	
	i=$((i+1))
done
