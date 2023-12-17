# IELTS-Speaking-Simulator
A GPT offers an authentic practice experience, helpful for anyone preparing for IELTS.

[中文版本介绍](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/README.md)

# Introduction
[IELTS Speaking Simulator](https://chat.openai.com/g/g-uGueIrCsT-ielts-speaking-simulator) is a GPT based on ChatGPT. It accurately simulates the IELTS speaking test, choosing questions from the latest question bank. It assesses and refines your responses after the conversation, offering a more realistic practice than doing it solo.

![IELTS Speaking Simulator](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/IELTS%20Speaking%20Simulator_Interface.jpg)

# How to Use
1. Get the official ChatGPT app from the AppStore or Google Play, then sign up and log in.
2. Subscribe to ChatGPT Plus.
3. Visit https://chat.openai.com/g/g-uGueIrCsT-ielts-speaking-simulator
4. Open it in ChatGPT and click the headphone icon at the bottom right to start.

As it's based on GPT-4, you can send 40 messages every 3 hours, which is enough for a complete practice session.


# Tips for Using the Tool

## Getting Started
1. Make sure you have enough usage quota for GPT-4, or you might get a message saying you've reached your limit. If this happens, just click the headphone button again after your quota is refreshed.
2. I usually start with "Let's do a full IELTS speaking simulation today" to simulate a complete speaking test. If you only need to simulate Part 1 or Part 2 & 3, just inform it.
3. Don’t worry if you hear squeaking sounds after starting the conversation - it’s just Python picking questions randomly. If it doesn’t work and you get the same questions, give it another go. Also, it's normal to hear the squeaking sound twice and be asked your name twice - I'm not sure why, but it happens.

## While Chatting
1. If you miss a question, feel free to ask for it to be repeated, just like in a real test.
2. A notable issue is that if you hesitate in the conversation, it may interrupt due to ChatGPT's voice conversation capabilities. Although I've included prompts to encourage finishing unanswered questions, it often skips ahead. Try to keep the conversation flowing.
3. During Part 2, it won't remind you when the 1-minute preparation time is up, so keep an eye on the time.
4. Sometimes, the questions in Parts 1 and 3 are limited; you might want to give it another try if that happens.

## Wrapping Up
1. Use the assessment score as a guideline but don't stress over it too much. Currently, it can't give detailed feedback on pronunciation, and the feedback is based on the text after voice recognition.
2. After completing the practice, I switch to the computer and ask it to further analyze and improve the conversation content. My most common prompt is:
   > Please arrange a comprehensive, enhanced, and detailed response that aligns with my words and avoids complex terminology, focusing on the topic and questions mentioned. You can start by structuring Part 1.
  
  Then, modify Part 2 and 3 accordingly. If you're not satisfied with the improved text, you can retry or specify your needs.

(Feel free to share your own prompts for organizing and summarizing after conversations!)


# Thoughts During Learning
1. I've tried other speaking practice GPTs, but they often revolve around familiar topics. However, for IELTS practice, a framework with clear standards seems more suitable, even though I don't currently need it for IELTS.
2. Memorization or sticking to specific topics isn't necessary for IELTS speaking preparation. Treating it as spontaneous practice works better. For topics that are difficult to explain, just remembering the framework and keywords afterwards is enough.
3. Honestly, this is the best GPT I've used so far. Considering the cost of individual speaking practice, paying $20 or more per month offers great value. I hope consistent practice will help reduce my conversation anxiety. This is just a start, and I might explore GPTs for behavioral interviews next year.
4. A friend once said any method works for learning English, as long as you stick with it. Seeking efficiency might be a trap if you want fluency. This insight comes from my last preparation experience. Here's an article I wrote previously: "[Expectation vs. Reality: A Deep Dive into AI-Assisted Language Learning](https://hubeiqiao.notion.site/Expectation-vs-Reality-A-Deep-Dive-into-AI-Assisted-Language-Learning-2ebf7d1fc3224e9486b3be81f48d25ab?pvs=4)"

# Sharing the Making Process
1. I've attached [the current instructions](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/IELTS-Speaking-Simulator_Instructrion_20231215.txt) for this GPT in an attachment. You can copy them to create your own GPTs and customize the process or question bank.
2. The biggest challenge in creating this GPT was figuring out how to enable it to randomly select questions from the question bank. Despite many prompt modifications, it wasn't random but followed a fixed cycle. Fortunately, with [@goldengrape](https://twitter.com/goldengrape)'s hint, I realized that Knowledge can upload Python scripts for execution with the Code Interpreter, which solved the issue. I also considered using Actions to connect to external interfaces, but using external Actions on a GPT prevents it from being used on mobile, thereby losing the voice conversation feature.
3. Other similar GPT experiences usually present all questions under a Topic. Initially, I encountered the same issue, but after numerous modifications, I managed to somewhat resolve it (not guaranteed, retry if needed).
4. The question bank is from IELTS Brother's collection for September-December, and it will be updated with the January-April 2024 questions.

# Why share
1. This GPT is for my use and exploring possibilities, and it's all still very new. Practicing daily, I've come to think of it as the best in its category, silently admiring its capabilities. Since I've created it, I figured why not let friends with similar interests benefit from it too.
2. More frankly, there's nothing to hide, as the Instructions can be obtained through Prompt skills(I didn't consider adding protection to the Prompt, as there are always ways to get around it). So, it's better to make it public for everyone.
3. From a product perspective, with hundreds of users now, I need to be more careful with updates. Sharing it publicly allows everyone to tweak it to their needs and provide feedback for improvements.
4. It's not just about conversation practice. What's equally important is the organized learning afterwards. Seeing different methods of use and discovering new content or skills that I'm unaware of would be fantastic.
5. ChatGPT is like a big toy right now. But, in language learning, it shows immense promise. I hope this inspires developers to create even better products.

---
Besides this speaking GPT, I've also created GPTs for reading and writing. For reference.
- [IELTS Reading Tutor](https://chat.openai.com/g/g-vYk0G1CPU-ielts-reading-tutor): Please provide the Reading article, questions, and your thoughts or concerns, so that I can offer detailed feedback and explanations.
- [IELTS Writing Mentor](https://chat.openai.com/g/g-vG4GIq3DH-ielts-writing-mentor): Get personalized IELTS writing assistance, focusing on in-depth analysis and enhancement of both Task 1 and Task 2. Simply paste your task and essay to receive expert guidance.

---

Finally, a big thank you to Sam and OpenAI(["A Year with ChatGPT: Personal Reflections and Transformation"](https://hubeiqiao.notion.site/A-Year-with-ChatGPT-Personal-Reflections-and-Transformation-a69865a83beb4a4d8bbaf2adde71ab0d?pvs=4). I never imagined I could create such a product so quickly on my own. It indirectly shows how Artificial General Intelligence (AGI) will revolutionize society in the coming years. For ordinary people like us, the most practical advice is to experience these products in real scenarios. This is just the beginning and requires more patience.
