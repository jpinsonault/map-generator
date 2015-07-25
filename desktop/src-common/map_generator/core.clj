(ns map-generator.core
  (:require [play-clj.core :refer :all]
            [play-clj.ui :refer :all]))

(defscreen main-screen
  :on-show
  (fn [screen entities]
    (update! screen :renderer (stage))
    [(label "Hello world!" (color :white))
     ; create a green and red rectangle

     ; create a green rectangle at 10,10 and rotate it 45 degrees
     (bundle
       (assoc (shape :filled
                :set-color (color :green)
                :rect 0 0 10 30)
         :x 10
         :y 10
         :angle 45)
       (assoc (shape :filled
                :set-color (color :green)
                :triangle 100 100 200 200 100 200)
         :x 0
         :y 0
         :a-thing "stuff"))])

  :on-render
  (fn [screen entities]
    (clear!)
    (render! screen entities)))

(defgame map-generator-game
  :on-create
  (fn [this]
    (set-screen! this main-screen)))
