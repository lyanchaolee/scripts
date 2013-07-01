(defn unless1 [expr form]
  (if expr nil form)
  )

(unless1 false (println "this should print"))
(unless1 true (println "this should not print"))

(defmacro unless [expr form]
  (list 'if expr nil form)
  )

(unless false (println "this should print"))
(unless true (println "this should not print"))

(println (macroexpand-1 '(unless false (println "this should print"))))

(println (macroexpand '(unless false (println "this should print"))))

(defmacro when-not [test & body]
  (list 'if test nil (cons 'do body))
  )

(defmacro chain
  ([x form] '(. ~x ~form))
  ([x form & more] '(chain (. ~x ~form) ~more))
  )

(defmacro bench [expr]
  '(let [start# (System/nanoTime)
         result# ~expr]
     {:result result# :elapsed (- (System/nanoTime) start#)}
     )
  )

