(ns com.my-company.clojure.examples.my-utils
(:import java.util.Date)
(:use [clojure.contrib.def :only (defvar-)])
(:require [clojure.contrib.shell-out :as shell])
)
(defvar- greetings
  {:english "Hello"
   :german "Guten Tag"
   :french "Bonjour"
   "Map from language to greeting"
   }
  )
(defn- user-prop
  "Returns the system property for user.<key>"
  [key]
  (System/getProperty(str "user." key))
  )
(defn greeting
  "Returns a greeting for the current user. The greeting is in English by default, or optionally in another language: :german or :french"
  ([]
    (greeting :english)
    )
  ([language]
    (str (greetings language))
  )
  )
(defn user-files
  "Reuturns a seq of the file names in the current user's home directory"
  []
  (seq (.split(shell/sh "ls" (user-prop "home")) "\n"))
  )

(defn print-report
  "Prints a report containing some info about the current user"
  []
  (println (greeting))
  (println "These are some of your files as of" (str (Date.)))
  (doseq [file (take 10 (user-files))]
    (println file)
    )
  )
(print-report)


