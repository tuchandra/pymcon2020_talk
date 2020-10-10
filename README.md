# Learning Bayesian Statistics with Pokemon GO
![talk_screenshot.png](talk_screenshot.png)

This repo contains the materials for my [PyMCon](pymc-devs.github.io/pymcon/) talk, *Learning Bayesian Statistics with Pokemon GO*.

## Included materials
**Notebooks**: these are cleaned up versions of what I live coded in the talk. 
They also include snippets of code (mostly plotting!) that didn't make it into the final video.

 * `1_rayquaza.ipynb`: suppose we got 2 shinies in 44 encounters; what do we think the shiny rate is?
 * `2_silph.ipynb`: given a sequence of events, how does our understanding of the shiny rate change over time?
 * `3_dragon_week.ipynb`: did the chance of hatching a Deino change in the middle of the Dragon Week event?

**Data**: There are two CSV files: `rates.csv` for the second model and `dragon_week.csv` for the third.

**Other**: The `environment.yml` file can reproduce my conda environment in which I ran all of the code.
