(define
    (problem pacman-level-1)
    (:domain pacman_simple)

;; problem map
;;  | 1 | 2 | 3 |
;; -|---|---|---|
;; a| P | G | F | 
;; b| _ | _ | _ | 
;;  |---|---|---| 

    (:objects
		a1 b1 a2 b2 a3 b3
	)
	
	(:init
		(connected a1 b1)
		(connected b1 a1)

		(connected a2 b2)
		(connected b2 a2)

		(connected a3 b3)
		(connected b3 a3)

		(connected a1 a2)
		(connected a2 a1)
		(connected a2 a3)
		(connected a3 a2)

		(connected b1 b2)
		(connected b2 b1)
		(connected b2 b3)
		(connected b3 b2)

		(at-pacman a1)
		(at-ghost a2)
		(at-food a3)
	)

    (:goal
    	(and
			(not(at-food a3))
		)
	)
)