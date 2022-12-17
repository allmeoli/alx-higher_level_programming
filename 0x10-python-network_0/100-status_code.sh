#!/bin/bash
# this script rautomize git add commit and push 
# with one code
if [ $# == 0 ] 
then  
      # If variable less than 10    
      git add .
      git commit -m "hot_fix"
      git push 
elif [ $# == 1 ] 
then  
      # If variable less than 25  
      git add "$1"
      git commit -m "hot_fix"
      git push 
else
     # If variable is greater than 25   
     git add "$1"
     git commit -m "$2"
     git push
fi