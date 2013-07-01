(defn sum-to [n]
  (loop [i 1 sum 0]
    (if (<= i n)
      (recur (inc i)(+ i sum))
      sum
      )
    )
  )

(println (sum-to 10))
(dotimes [_ 5] (time (sum-to 10000)))


(defn integer-sum-to [n]
  (let [n (int n)]
    (loop [i (int 1) sum (int 0)]
      (if(<= i n)
        (recur (inc i)(+ i sum))
        sum
        )
      )
    )
  )
(println (integer-sum-to 10))
(dotimes [_ 5] (time (integer-sum-to 10000)))


(defn unchecked-sum-to[n]
  (let[n (int n)]
    (loop[i (int 1) sum (int 0)]
      (if (<= i n)
        (recur (inc i)(unchecked-add sum i))
        sum
        )
      )
    )
  )

(println (unchecked-sum-to 10))
(dotimes [_ 5] (time (unchecked-sum-to 10000)))


(defn better-sum-to[n]
  (reduce + (range 1 (inc n)))
  )

(println (better-sum-to 10))
(dotimes [_ 5] (time (better-sum-to 10)))

(defn best-sum-to[n]
  (/ (* n (inc n)) 2)
  )
(println (best-sum-to 10))
(dotimes [_ 5] (time (best-sum-to 10)))


(defn describe-class[#^Class c]
  {:name (.getName c) :final (java.lang.reflect.Modifier/isFinal (.getModifiers c))}
  )

(println (describe-class java.lang.reflect.Modifier))