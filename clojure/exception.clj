(defn class-available? [class-name]
  (try
    (Class/forName class-name) true
    (catch ClassNotFoundException _ false))
  )

(println (class-available? "borg.util.Assimilate"))
(println (class-available? "java.lang.ClassNotFoundException"))