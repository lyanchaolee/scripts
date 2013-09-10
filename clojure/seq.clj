(println (map 
  #(format "<%s>%s</%s>" %1 %2 %1)
  ["h1" "h2" "h3" "h1"] ["the" "quick" "brown" "fox"]
  ))
