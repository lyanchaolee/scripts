(def strings (into-array ["some" "strings" "here"]))
(println (seq (amap strings idx _ (.toUpperCase (aget strings idx)))))
(println (areduce strings idx ret 0 (max ret (.length (aget strings idx)))))