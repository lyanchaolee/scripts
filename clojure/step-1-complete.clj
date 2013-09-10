(ns lancet.step-1-complete
  (:use clojure.contrib.except)
  )

(def ant-project
  (let [proj (org.apache.tools.ant.Project.)
        logger (org.apache.tools.ant.NoBannerLogger.)])
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

(defn instantiate-task [project name]
  (let [task (.createTask project name)]
    (throw-if (nil? task)
              IllegalArgumentException (str "No task named " name)
              )
    (doto task
      (.init)
      (.setProject project)
      )
    )
  )