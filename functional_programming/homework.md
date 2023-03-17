I would rate coding in Racket as a 2, maybe. I can certainly see the advantage and maybe I just need more time with the language, but it doesn't feel as intuitive as OOP languages such as python. Simply doing math feels mor complex. People naturally read math as 2 + 5, so it's weird to write + 2 5. I also am not a fan of the lack of commas. Most programming languages consider whitesoace to be meaningless, so it is a tad frustrating to be required to place spaces into your code.

(define (ack m n)
  (cond ((= m 0) (+ n 1))
        ((and (> m 0) (= n 0)) (ack (- m 1) 1))
        (else (ack (- m 1) (ack m (- n 1))))))
(ack 1 2)
(ack 2 3)
(ack 3 4)

