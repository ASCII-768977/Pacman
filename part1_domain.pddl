(define
    (domain pacman_simple)
    (:requirements :strips :typing :equality :adl)

    (:predicates
        ;;which room pacman in
        (at-pacman ?room)
        ;;which room ghost in                     
        (at-ghost ?room)
        ;;which room food in                      
        (at-food ?room)         
        ;;if the room are connected              
        (connected ?start ?end)            
    )

    (:action move                               
        :parameters (?from ?to)          
        :precondition
        (and
            ;;pacman at from
            (at-pacman ?from)                    
            (connected ?from ?to)    
            :;cannot got to the room with ghost           
            (not(at-ghost ?to))
        )
        :effect
        (and
            ;;change pacman location of room and food                            
            (at-pacman ?to)                        
            (not(at-pacman ?from))
            (not(at-food ?to))
        )
    )
)