(import '(java.util Random Locale)
        '(java.text MessageFormat))

(def rnd (new Random))
(println (. rnd nextInt 10000))

(defn painstakingly-create-array[]
  (let [arr (make-array String 5)]
    (aset arr 0 "Painstaking")
    (aset arr 1 "to")
    (aset arr 2 "fill")
    (aset arr 3 "in")
    (aset arr 4 "arrays")
    arr
    ))
(println (aget (painstakingly-create-array) 0))
(println (alength (painstakingly-create-array)))

(println (to-array ["Easier" "array" "creation"]))

(println (String/format "Training Week: %s Mileage: %d" (to-array [2 26])))

(println (into-array String ["Easier", "array", "creation"]))
(println (into-array ["TT", "YY", "FF"]))