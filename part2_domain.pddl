(define
    (domain pacman_mid)
    (:requirements :strips :typing :equality :adl)


    (:predicates
        ;;which room at-pacman in
        (at-pacman ?room)
        ;;which room ghost in                     
        (at-ghost ?room)
        ;;which room food in                      
        (at-food ?room)
        ;;which room capsule in
        (at-capsule ?room)
        ;;if the room are connected       
        (connected ?start ?end)
        ;;if the pac man is superman
        (superman)
    )


    (:action move
        :parameters (?from ?to)
        :precondition 
        (and
            ;;pacman at from
            (at-pacman ?from)                      
            (connected ?from ?to)    
            ;;cannot eat ghost or superman can eat ghost 
            (or
                (not(at-ghost ?to))
                (superman)
            )
        )
        :effect
        (and
            ;;change pacman location of room
            (at-pacman ?to)                      
            (not(at-pacman ?from))
            ;;when eat capsule then become superman, remove capsule
            (when (at-capsule ?to)
                  (and 
                      (not(at-capsule ?to))
                      (superman)
                  )
            )
            ;;eat food
            (when (at-food ?to)
                  (not(at-food ?to))
            )
            ;;when superman eat ghost
            (when(superman)
                 (not(at-ghost ?to))
            )
        )
    )
)
