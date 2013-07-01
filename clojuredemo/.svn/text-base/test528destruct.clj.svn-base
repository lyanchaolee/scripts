(defn greet-author-1[author]
  (println "Hello," (:first-name author))
  )

(greet-author-1{:last-name "Vinge" :first-name "Vernor"})

(defn greet-author-2[{fname :first-name}]
  (println "Hello," fname)
  )
(greet-author-2 {:last-name "Vinge" :first-name "Vernor"})

(let [[x y] [1 2 3]]
  [x y])

(let [[_ _ z][1 2 3]]
  z)

(let [[x y :as coods][1 2 3 4 5 6]]
  (println (str "x:" x ", y: "y ", total dimesions" (count coods))))


(use '[clojure.contrib.str-utils :only(re-split str-join)])
(defn ellipsize [words]
  (let [[w1 w2 w3](re-split #"\s+" words)]
    (str-join " " [w1 w2 w3 "..."])
    )
  )

(println (ellipsize "The quick brown fox jumps over the lazy dog."))