(def mult
  (fn this
    ([] 1)
    ([x] x)
    ([x y] (* x y))
    ([x y & more]
      (apply this (this x y) more)
      )
    )
  )
(println (mult 1))
(println (mult 1 2))
(println (mult 1 2 3 4))

(defn constrained-sqr[x]
  {:pre [(pos? x)]
   :post [(> % 16),(< % 225)]
   }
   (* x x)
  )
(println "5 sqr is"(constrained-sqr 5))
(println "10 sqr is"(constrained-sqr 10))

(println "error will occurs in 4 sqr")
(constrained-sqr 4)