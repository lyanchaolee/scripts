(ns lancet.step-1-repl)

(def 
  ant-project
  (let [proj (org.apache.tools.ant.Project.)
        logger (org.apache.tools.ant.NoBannerLogger.)]
    (doto logger
      (.setMessageOutputLevel org.apache.tools.ant.Project/MSG_INFO)
      (.setOutputPrintStream System/out)
      (.setErrorPrintStream System/err)
      )
    (doto proj
      (.init)
      (.addBuildListener logger)
      )
    )
  )
(defn instantiate-task [project name]
  (let [task (.createTask project name)]
    (doto task
      (.init)
      (.setProject project)
      )
    )
  )


(use '[clojure.contrib.except :only(thow-if)])
(defn safe-instantiate-task [project name]
  (let [task (.createTask project name)]
    (thow-if (nil?task)
             IllegalArgumentException (str "No Task name" name)
             )
    (doto task
      (.init)
      (.setProject project)
      )
    )
  )


(println (bean ant-project))
(println (keys (bean ant-project)))





