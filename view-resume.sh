#!/bin/bash

google-chrome --headless --print-to-pdf="./wes-galbraith-resume.pdf" wes-galbraith-resume.html;
gnome-open wes-galbraith-resume.pdf
