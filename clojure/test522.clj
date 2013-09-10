(defn greeting
  "Returns a greeting of the form 'Hello, username.' Default username is 'world'."
  ([](greeting "world"))
  ([username](str "Hello, " username))
  )

(println(greeting))
(println(doc greeting))