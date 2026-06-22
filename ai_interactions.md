# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative numbers | "1- Please verify whether the game can handle those three potential 'edge case' inputs: negative numbers, decimals, or extremely large values. 2- Invalid input should not cost an attempt." | `test_parse_guess_rejects_negative` | PASSED | I chose this edge case because the correct guess is always a number that is constantly between 1 and 100, or between 1 and 20, which means that any number below 1 should be irrelevant for this game. |
| Decimals | (Same prompt as above.) | `test_parse_guess_rejects_decimals_outright` | PASSED | I chose this edge case because the correct guess is always a whole number, and thus any decimal after the number should be irrelevant. |
| Extremely large values | (Same prompt as above.) | `test_parse_guess_rejects_extremely_large_values` | PASSED | I chose this edge case because the correct guess never exceeds 100 (or 20 for Easy mode), and thus any values larger than those numbers should be irrelevant. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
