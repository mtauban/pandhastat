# Pandhastat

## Overview

Pandhastat is a poorly written Python script supposed to monitor the temperature in my flat. It runs on a Raspberry Pi 2 B+, acquires the temperature throug a 1-wire MAXIM temperature sensor and sends action to the boiler using a cheap RF 433MHz board. The boiler side is controlled by an Arduino card, connected to a relay and a cheap RF 433MHz receiver. 

## Quick and Dirty

Pandhastat was formerly based on bash scripts and therefore relies on text files for status storing, temperature setting and logging. The aim of making it a Python app was to move on a more sexy solution involving high tech fancy for data storing. 
It is supposed to integrate a thermal model in order to account for inertia (http://mathieutauban.fr/blog/2014/12/un-modele-thermique-de-mon-appartement/) but this has not been implemented yet. 
