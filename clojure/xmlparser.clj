(use '[clojure.xml :only (parse)])

(parse (java.io.File "compositions.xml"))

(for [x (xml-seq