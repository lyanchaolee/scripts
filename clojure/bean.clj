(import '(java.security MessageDigest))

(bean (MessageDigest/getInstance "SHA"))

(println (:digestLength (bean (MessageDigest/getInstance "SHA"))))