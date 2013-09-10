(println (:darwin {:sundance "spaniel", :darwin "beagle"}))
(println (:snoopy {:sundance "spaniel", :darwin "beagle"}))

(def score {:stu nil :joey 100})
(println (:stu score))

(println (contains? score :stu))
(println (get score :stu :score-not-found))
(println (get score :aaron :score-not-found))

(def song {:name "Agnus Dei"
           :artist "Krzysztof Penderecki"
           :album "Polish Requiem"
           :genre "Classical"
           })

(println (assoc song :kind "MPEG Audio File"))
(println (dissoc song :genre))

(println (select-keys song [:name :artist]))
(println (merge song {:size 8118166, :time 507245}))

(println (merge-with
           concat
           {:rubble ["Barney"], :flintstone ["Fred"]}
           {:rubble ["Betty"], :flintstone ["Wilma"]}
           ))