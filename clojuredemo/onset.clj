(use '[clojure.set] '[clojure.xml])
(def languages #{"java" "c" "d" "clojure"})
(def letters #{"a" "b" "c" "d" "e"})
(def beverages #{"java" "chai" "pop"})
(println (union languages beverages))

(println (difference languages beverages))
(println (intersection languages beverages))
(println (select #(= 1 (.length %)) languages))