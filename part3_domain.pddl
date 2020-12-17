(define
    (domain pacman_hard)
    (:requirements :strips :typing :equality :adl)


    (:predicates
        ;;which room pacman in
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
        ;;step1
        (battery1)
        ;;step2
        (battery2)
    )
    (:action move
        :parameters (?from ?to)
        :precondition
        (and
            ;;pacman at from
            (at-pacman ?from)
            (connected ?from ?to)
            ;;cannot eat ghost or superman can eat
            (or
                (not(at-ghost ?to))
                (battery2)
                (battery1)
            )
        )

        :effect 
        (and
            ;; change pacman location of room
            (at-pacman ?to)                      
            (not(at-pacman ?from))
            ;;when eat capsule then become superman, with a battery2
            (when   (at-capsule ?to)
                    (and
                        (battery2)
                        (not(at-capsule ?to))
                    )
            )
            ;; eat food
            (when   (at-food ?to)
                    (not(at-food ?to))
            )
            ;;when food exist pacman must eat ghost
            (when   (exists (?to)
                            (at-food ?to)
                    )
                    (not(at-ghost ?to))
            )
            ;;when battery2 then reduce to battery1
            (when   (battery2)
                    (and
                        (battery1)
                        (not(battery2))
                    )
            )
            ;;when battery1 then cannot eat ghost
            (when   (battery1)
                    (and
                        (not(battery1))
                    )
            )
        )
    )
)