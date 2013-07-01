(import '(org.xml.sax InputSource)
        '(org.xml.sax.helpers DefaultHandler)
        '(javax.xml.parsers SAXParserFactory)
        '(java.io StringReader))


(def print-element-handler
  (proxy [DefaultHandler][]
    (startElement
      [uri local qname attrs]
      (println (format "Saw element: %s" qname))
      )
    )
  )

(defn demo-sax-parse [source handler]
  (.. SAXParserFactory newInstance newSAXParser
    (parse (InputSource. (StringReader. source)) handler)
    )
  )

(demo-sax-parse "<foo><bar>Body of bar</bar></foo>" print-element-handler)
(.start (Thread. (proxy [Runnable] [] (run[] (println "I ran!")))))

(dotimes [i 5]
  (.start
    (Thread.
      (fn[]
        (Thread/sleep (rand 500))
        (println (format "Finished %d on %s" i (Thread/currentThread)))
        ))
    )
  )