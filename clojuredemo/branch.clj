(defn is-small?[number]
  (if(< number 100) "yes" "nop")
  )

(println (is-small? 50))
(println (is-small? 100))
(println (is-small? 10000))

(defn is-small2?[number]
  (if(< number 100)
    "yes"
    (do
      (println "Saw a big number" number)
      "no"
      )
    )
  )

(println (is-small2? 50))
(println (is-small2? 100))
(println (is-small2? 10000))

(defn looprectest[y]
(loop[result [] x y]
  (if (zero? x)
     result
     (recur (conj result x) (dec x)) 
    )
  )
)
(println (looprectest 5))

(defn countdown [result x]
  (if (zero? x)
    result
    (recur (conj result x)(dec x))
    )
  )

(println (countdown [] 5))







