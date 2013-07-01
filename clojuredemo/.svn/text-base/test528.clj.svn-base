(defn date
  [person1 person2 & personn]
  (println person1 "and" person2 "and" (count personn) "other people")
  )
  
 (date "lyc" "ycl")
 (date "lyc" "ycl" "xxxy")
 
 (defn indexable-word? [word]
   (> (count word) 2)
   )
 
 (use '[clojure.contrib.str-utils :only (re-split)])
 (println (filter indexable-word? (re-split #"\W+" "A fine day it is")))
 
 (println (filter (fn[w] (> (count w) 2)) (re-split #"\W+" "A fine day")))
          
 (println (filter #(> (count %) 2) (re-split #"\W+" "A fine day it is")))