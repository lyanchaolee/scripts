(let [m (re-matcher #"\w+" "the quick brown fox")]
  (loop [match (re-find m)]
    (when match
      (println match)
      (recur (re-find m))
      )
    )
  )


(use '[clojure.contrib.duck-streams :only (reader)])
(defn non-blank? [line] (if (re-find #"\S" line) true false))

(defn not-svn? [file] (not (.contains (.toString file) ".svn")))

(defn clojure-source? [file] (.endsWith (.toString file) ".clj"))

(defn clojure-loc [base-file]
  (reduce
    +
    (for [file (file-seq base-file) 
          :when (and (clojure-source? file) (not-svn? file))]
      (with-open [rdr (reader file)]
        (count (filter non-blank? (line-seq rdr)))
        )
      )
  )
 )

(println (clojure-loc (java.io.File "/Users/lyc/")))



