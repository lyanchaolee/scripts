(use '[clojure.contrib.str-utils :only (re-split)])
(defn indexable-words[text]
  (let[indexable-words? (fn[w] (> (count w) 2))]
  (filter indexable-words? (re-split #"\W+" text))
  ))
(println (indexable-words "how d do you see china's development in recent years?!"))

(defn make-greeter[greeting-prefix]
  (fn[username] (str greeting-prefix ", " username))
  )
(def hello-greeting(make-greeter "Hello"))
(def alopha-greeting(make-greeter "Aloha"))
(println (hello-greeting "world"))
(println (alopha-greeting "world"))
(println ((make-greeter "Howdy") "pardner"))