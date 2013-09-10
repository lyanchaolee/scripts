(defn len [x]
  (.length x)
  )
(defn len2[^String x]
  (.length x)
)
(println(time(reduce + (map len(repeat 1000000 "asdf")))))
(println(time(reduce + (map len2(repeat 1000000 "asdf")))))