(use '[clojure.xml :only (parse)])

(parse (java.io.File "compositions.xml"))

(for [x (xml-seq(parse (java.io.File. "examples/sequences/compositions.xml"))):when (= :composition (:tag x))] (println (:composer (:attrs x))))