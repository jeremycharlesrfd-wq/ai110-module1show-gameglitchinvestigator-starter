# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I ran it for the first time, I put 50 as a guess since it is a number between 0 and 100. So far, everything seemed to work
fine. Then, the game suggested me to go lower, and for everytime I put a lower number even when I wrote down 0, the game kept on telling me
to guess a lower number. Finally, when the game ended (one round before it was supposed to) they said that the expected answer was 65, which
doesn't make sense since the hints were constantly telling me to go lower when my guesses were already below 65. Moreover, I was unable to
launch a new game afterwards and I had to reload the page to restart playing.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1 - The hints were backwards and didn't help to bring me closer to the actual number.
2 - The game won't restart even if I click the "New game" button.
3 - I was out of attempts already even when I could clearly see on the screen that I had 1 attempt left.
4 - I was able to write a number below 0 and still receive a hint telling me to go lower.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess | "Too high" hint    | "Too low" hint |          none          |
| of 50 |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|
|submit-|Receiving feedback | no feedback     |          none          |
| -ted  |ex.Lower or Higher | received        |                        |
|a guess|                   |                 |                        |
| after |                   |                 |                        |
|running|                   |                 |                        |
| a new |                   |                 |                        |
| game  |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|
|Guess  | Negative input    | Negative output |          none          |
|of -5  | should not be     | are allowed     |                        |
|       | allowed           |                 |                        |
|-------|-------------------|-----------------|------------------------|
|Tried 7| One more attempt  |The final answer |------------------------|
|attempt| before the final  |is directly      |------------------------|
|out of |answer is revealed |revealed before. |------------------------|
|8      |                   |the last attempt |------------------------|
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude suggested that the reason why the game tells me to go lower when I should actually go higher was because the hint messages were reversed. For example, instead of returning "Too High", "📈 Go HIGHER!", it returned "Too Low", "📉 Go LOWER!". The suggestion was correct because fixing that issue helped me to actually play the game properly. I verified that the code was fixed by launching a new game and I managed to win by following the hints.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One AI suggestion that seemed misleading was when Claude told me that when it comes to round float numbers to a whole number, it doesn't necessarily round it in a way that is expected mathematically. For example 2.9 rounds to 2 instead of 3. So CLaude suggested to change that but I think that it was misleading because in this specific game, I believe that what matters the most is the non decimal part of the number. To verify that this behavior didn't change, I tried to add .7 after my expected correct guess to see if it would still be considered as the correct answer. eg. if the correct answer is 23, I wrote 23.7. And it worked so my result is verified.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I considered that a bug was fixed when all the tests related to that bug passed and when the bug was not apparent in the game anymore.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test that I ran checked what happens when the user;s unput is 60 and the correct answer is 50. The test asserted that the outcome should be considered as "TOO HIGH" and the game should display a hint indicating to go "LOWER". This test confirmed that the code indicates the correct hint that would bring the player closer to the expected answer when their guess is off.

- Did AI help you design or understand any tests? How?

Claude helped me to understand what the test called "test_string_secret_is_compared_numerically" is supposed to check. It explained me in the chat that this test is there to check whether the case that used to flip lexicographically passes. I didn't understand what it meant at the beginning but Claude explained me that if we compare the string "100" and "93", "93" will be greater than "100" because python compares each single character from the left to the right and since "1" in "100" is smaller than "9" in "93", this small detail used to make the game work abnormally.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit basically restarts the whole program on every click. Anything I need it to remember (the score, the target number, etc.) has to go in st.session_state, otherwise it disappears once the script reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I think that this habit of running the code and finding out for yourself what went wrong is a great way to figure out what should be fixed by the programmer and the AI. Indeed, it was important for me to remember that the first step to fix a problem is to find out what is the exact problem.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I will work with AI, I will make sure to separate the different inquiry in different AI chats to make sure that I can go back to each chats when I need to review some information without having to scroll through irrelevant prompts.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project made me realise that writing code with AI is a bit like driving a car. It can make what you want it to do but you need to indicate specifically what you want. For example, you need to be specific about which file and which lines you want to modify and explain the intent behind that modification.    
