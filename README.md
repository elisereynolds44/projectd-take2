# Fast Food Isn't That Bad! 

Overview:

This project is a playful but purposefully misleading Dash dashboard built around the topic of fast food and obesity. While it showcases real data from the CDC and Kaggle, the goal was to challenge the assumptions we often hold—and to explore how easily data storytelling can be twisted.

This README outlines the source material, dashboard structure, design decisions, and what makes each visualization deceptively persuasiv

------

# Pre-Reading Material

Title: CDC - Fast Food Intake Among Children and Adolecents in the United States, 2015-2018 

Link: https://www.cdc.gov/nchs/products/databriefs/db375.htm

Summary Thesis (Truth): 

Fast food is a contributing factor in obesity, but lifestyle and broader dietary habits play an equally, if not, more immportant role. 

Pre-reading questions: 

1. How often do you think the average teen eats fast food?
2. What percent of a child’s daily calories do you think comes from fast food?
3. Do you think fast food habits vary significantly between age groups?
4. Do children eat fast food more now than in previous decades?
5. What’s the difference between “eating fast food occasionally” and “relying on it”?
6. Do fast food restaurants offer healthy options for kids today?

------

# Misleading Thesis

"Fast food has been unfairly blamed for obesity - when in reality, other lifestyle factors matter more."

This thesis is misleading because it **downplays** fast food's contribution, implying it is not a cause at all. 

------

## Dashboard Structure 

Tabs: 

1. Overview
    - frames the convo with an open-ended but suggestive vibe
    - Quote: "Spoiler: it's not just the fries"
2. "How Bad Is It Really?"
    - misleads by comparing avg fast food calories to other meals.
    - design trick: colors + comparison bars make fast food seem normal.
3. "It's About Lifestyle, Not Food"
    - dropdown to show how other factors (exercise, water, snacking) influence obestiy class.
    - Misleading by omission: it doesnt show all interactions or confounding variables. 
4. Game Tab: "Can You Guess the Class?"**
    - users see lifestyle traits (like snacking, water, fast level) and guess obesity class
    - feedback highlights suprising answers where fast food != high obesity 
    - reinforces the message that fast food isnt the main culprit

------

## Misleading visuals: what & why 


**Bar chart - avg fast food calories**
- why misleading: no context for how often its eaten or by whom 
- Visual trick: makes fast food bars look unremarkable with narrow y-axis scaling 

**Comparison Chart  - other meals**
- why misleading: no info on portion size or frequency of consumption
- Visual trick: uses similar colors to suggest equivalence

**Line graphs - lifestlye factors**
- why misleading: highlights weak correlations as if they're strong
- Visual trick: smooth curves and upward/downward slants create illusion of cause-effect

**Game**
- why misleading: cherry-picked examples with surprising obesity levels
- Visual trick: makes people question their bias against fast food

------

## Correction + True Conclusion 

Despite the dashboard's message, fast food remains a huge contributor to excess calorie intake, poor nutrition, and long-term obesity risk. But it exits
alongside other factors like exercise, snacking, and hydration. 

"Obesity isn't what we eat - it's about how we live"

The truth is more nuanced, and this project aims to show how easily that nuance can be lost. 

------

## Acknowledgements 

Obesity dataset
- https://www.kaggle.com/datasets/suleymansulak/obesity-dataset

Fastfood nutrition
- https://www.kaggle.com/datasets/ulrikthygepedersen/fastfood-nutrition

CDC: 
- https://www.cdc.gov/nchs/products/databriefs/db375.htm

