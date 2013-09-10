(defstruct message
  :sender
  :text
  )

(struct message "stu" "test message")
(def messages (ref ()))

(defn naive-add-message [msg]
  (dosync
    (ref-set messages (cons msg @messages))
    )
  )

(defn add-message [msg]
  (dosync
    (alter messages conj msg)
    )
  )

(add-message (struct message "user 1" "hello"))
(add-message (struct message "user 2" "howdy"))

(println @messages)

(def x (map #(get % :sender) @messages))

(def y (reduce str x))

(println x)
(println y)