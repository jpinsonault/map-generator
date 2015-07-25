(ns map-generator.core.desktop-launcher
  (:require [map-generator.core :refer :all])
  (:import [com.badlogic.gdx.backends.lwjgl LwjglApplication]
           [org.lwjgl.input Keyboard])
  (:gen-class))

(defn -main
  []
  (LwjglApplication. map-generator-game "map-generator" 800 600)
  (Keyboard/enableRepeatEvents true))
