(defprotocol P
  (foo[x])
  (bar-me[x][x y])
  )

(deftype Foo[a b c]
  P
  (foo[x] a)
  (bar-me[x] b)
  (bar-me[x y](+ c y))
  )

(println(bar-me(Foo. 1 2 3)42))