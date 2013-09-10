(def stu{:name "Stu" :email "stu@thinkrelevance.com"})
(def serializable-stu (with-meta stu{:serializable true}))

(println (= stu serializable-stu))
(println (identical? stu serializable-stu))

(println (meta stu))
(println (meta serializable-stu))

(def stu-with-address (assoc serializable-stu :state "NC"))

(println (meta stu-with-address))
(println (:state stu-with-address))