# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                       | Expected Behavior             | Actual Behavior | Console Output / Error |
|---------------------------  |-------------------------------|-----------------|------------------------|
| 100.                        |   Go lower!                   |    Go higher!   |      none              |
| 140.                        |   Go lower!                   |.   Go lower!    |      none              |
|new game -> submit guess     |tells me to go high or low     | no response!!!  |      none              |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used GPT-5 mini in order to generate bug fixes and run tests for said bug fixes. Then there was a loop of trying out the game and finding and catching any new bugs I didnt see beforehand and correcting it as it came, perfecting the code.

  One correct suggestion was to remove the alternating str() conversion — keep secret as an int always.
  One incorrect suggestion was how the import statements should be changed (I didn't find that necessary).
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  AI helped designed the pytests that tested things like numeric vs string conparisons to check if the alternating string bug was really fixed or not. The main manual test was actually trying out the game itself a couple times and testing the edgecases (like going above and below the range) and unexpected submitted answers to see if things are working properly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
 I suppose you could describe it as launching a fully designed UI interface with the game logic in a browser tab via the terminal. I did learn that Streamlit is a pain to install dur to a very weird error of python enviornments that I don't understand very well.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  A habit that's beneficial to reuse for future labs or projects is to read the mark down documents carefully in advance so you know what to look out for in the future.

- What is one thing you would do differently next time you work with AI on a coding task?

  I would verify (if i could and if time allows for both us) with a human partner who is familar with programming game logic

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  As expected, AI code goes for optimal and intentionally design choices at the expense of readability or reusability unless we spend a long time going back and forth with it to cater it to a different outcome.


