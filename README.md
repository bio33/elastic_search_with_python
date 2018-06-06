# elastic_search_with_python
ETL process with elasticsearch API

# Querying the inserted Data

Link : http://52.15.143.94:9200/tweets6/_search
BODY : {
		"size":100,
    "query" : {
        "match_all" : {}	
		},
	"sort":{"_id":"asc"}
}

# Script.sh
This script takes about 10 minutes to run because of limited amount of ram preprocessing the tweets takes about 7-8 minutes alone.
