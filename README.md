# IELTS-Speaking-Simulator
A GPT offers an authentic practice experience, helpful for anyone preparing for IELTS.

[English Version](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/README_EN.md)


## 介绍
[IELTS Speaking Simulator](https://chat.openai.com/g/g-uGueIrCsT-ielts-speaking-simulator) 是基于 ChatGPT 的一款 GPT，它不仅完整模拟了雅思口语考试流程，并能随机抽取最新题库。对话结束后，除了提供评估外，还可以根据对话内容整理并改善文本。与单独练习相比，这种方式更贴近真实场景。

![IELTS Speaking Simulator](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/IELTS%20Speaking%20Simulator_Interface.jpg)


## 如何使用
1. 在 AppStore/Google Play 中下载 ChatGPT 官方应用，注册并登录（需要非国区的应用市场）。
2. 订阅 ChatGPT Plus。如果 iOS/Android 上无法支付，推荐使用 WildCard 一条龙服务：https://bewildcard.com/i/BEIQIAO
3. 访问 https://chat.openai.com/g/g-uGueIrCsT-ielts-speaking-simulator
4. 选择在 ChatGPT 中打开，点击右下角的耳机按钮即可开始使用。

GPTs 是基于 GPT-4 的，因此按照目前的限制，每 3 小时可以发 40 条，也足够一次完整的练习了。


## 使用技巧
### 对话开始
1. 确保有足够的 GPT-4 使用额外额度，否则可能在练习过程中被告知达到了上限。即便真到了上限，有额度后可以再次点击耳机按钮继续练习。
2. 我通常第一句话会讲“Let's do a full IELTS speaking simulation today.” 来模拟一次完整的口语考试。如果只有模拟 Part 1 或者 Part 2&Part 3 的需求，直接告知它即可。
3. 开始对话后，听到有吱吱声是正常的，说明它正在使用 Python 随机抽取题库。如果没有运行导致出现固定题目的情况，可以重试一次。除此之外，有一定几率你会听到两次吱吱声以及询问两遍你的名字（我也不知道这是什么问题导致的），也是正常的。


### 对话进行中
1. 对话过程中，如果没听清楚问题，可以要求其再重复一遍（在真实考试中也可以这样）。
2. 目前有一个显著的问题是，如果对话中你卡壳了，则基于 ChatGPT 语音对话的能力，会中断对话。虽然我在 Prompt 中加入了类似没有回答完问题的话会鼓励回答的说明，但实际很多时候会直接跳过。总之还是保持流畅度吧。
3. Part 2 部分，实际不会在 1 分钟准备时间到时提示你，这个自己看下时间就好了。
4. 有时候 Part 1 和 Part 3 问的问题会很少，可以重新再来一次。


### 对话结束后
1. 评估的分数作为参考就好，不要太当真。目前版本无法对发音提供详细反馈，整个反馈都是基于语音识别后的文本。
2. 在练习完成后，我会切换到电脑上，要求其针对对话的内容进行进一步的分析以及改进。我最常用的 Prompt 是：
   > Please arrange a comprehensive, enhanced, and detailed response that aligns with my words and avoids complex terminology, focusing on the topic and questions mentioned. You can start by structuring Part 1.
   
   然后再以此改造 Part 2、Part 3。如果对改善后的文本不满意，可以重试或者明确的指出你的需求。

（也欢迎大家分享对话结束后整理、总结的相关 Prompt。）


## 学习途中的想法碎片
1. 我也尝试过其他口语练习 GPTs，但往往只围绕我熟悉的话题。虽然我没有即刻的雅思考试需求，但我仍然觉得，使用这种具有明确标准的练习框架更为合适。
2. 同时也不需要像以前准备雅思口语一样刻意去背诵或者套题，就当作是即时的练习就好了。遇到中文也说不清楚的话题，完成后记住框架和关键词就好了。
3. 实话讲，这是我用过的最好 GPTs，相比一对一口语陪练的费用，每月支付 20 美元甚至更多对我来说是物超所值的。希望在长时间的坚持练习后能够帮助我克服对话焦虑的恐惧。当然，这只是个开始，估计明年我会再找行为面试相关的 GPTs。
4. 曾经有朋友告诫我，无论采用什么方式，都能够学好英语，关键在于能否坚持下去。如果最终要熟练使用语言的话，效率至上大概率是陷阱。这是我从上一次准备中学习到的。这是我上次写的文章：[《期望与现实：有关 ChatGPT 辅助语言学习的暴论》](https://hubeiqiao.notion.site/ChatGPT-d9336f61a18f48aebbb9dd23d39bc326)


## 制作过程分享
1. 我在 [附件](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/IELTS-Speaking-Simulator_Instructrion_20231215.txt) 中附上了这个 GPT 当前的 Instructions，你可以复制一份创建属于你自己的 GPTs 以及针对性改造其中的流程或者题库。
2. 在制作这个 GPT 时，遇到的最大困难是不知道如何让其能够做到随机抽取题库。修改测试了多次 Prompt 后都依旧做不到随机，都是固定循环。幸运的是，在 [@goldengrape](https://twitter.com/goldengrape) 的提示下，我意识到 Knowledge 除了可以上传文本文件外，还可以上传 Python 脚本让其使用 Code Interpreter 执行。若干次调试后，总算解决了问题。曾经也考虑过使用 Actions 来对接外部接口，但当前的 GPTs 一旦使用外部 Actions 后，就没办法在手机上用了，也就无法使用语音对话功能了。
3. 体验的其他类似 GPT，大多都会把该 Topic 下的所有问题都扔出来。一开始我也遇到了类似问题，经过多次尝试修改后才勉强解决问题（并不能保证完全解决，如果遇到了就重试一次吧）。
4. 题库取自雅思哥整理的 9-12 月题库，等 2024 年 1-4 月的出来后会跟随更新。


## 为什么要分享出来
1. 这个 GPT 只是我自己用以及探索可能性的，现在一切都还是太早了。在每天练习后，我都会不由感叹这真是太棒了，并暗自称赞这是目前同类中最好的 GPT。想着反正都做出来了，不如让更多有类似需求的朋友来使用。
2. 更坦诚地讲，没什么要隐藏的，因为通过 Prompt 技巧是可以把我的 Instructions 给拿到的（我也没想过增加保护 Prompt，因为始终会有方式弄出来）。既然如此，不如直接公开出来给大家。
3. 产品上，现在的使用者至少有几百位了，因此我需要更谨慎的来做改动。既然如此，不如公开分享出来，让大家都有基于自己需求修改的可能性  以及搜集大家的反馈来改进这个小工具。
4. 对话练习只是其中一个部分。我觉得同等重要的是练习后的整理。如果能够看到大家不同的使用技巧，发现我不知道自己不知道的内容或者技巧就更好了。
5. ChatGPT 目前依旧是个大玩具。但至少从语言学习的场景看，是大有可为的。希望可以启发相关开发者，设计出更好的产品。

---

除了这个口语 GPT 外，我也创建了阅读和写作的 GPTs，供参考。
- [IELTS Reading Tutor](https://chat.openai.com/g/g-vYk0G1CPU-ielts-reading-tutor): Please provide the Reading article, questions, and your thoughts or concerns, so that I can offer detailed feedback and explanations.
- [IELTS Writing Mentor](https://chat.openai.com/g/g-vG4GIq3DH-ielts-writing-mentor): Get personalized IELTS writing assistance, focusing on in-depth analysis and enhancement of both Task 1 and Task 2. Simply paste your task and essay to receive expert guidance.

---

最后，由衷的感谢 Sam 和 OpenAI([《ChatGPT 发布一周年个人随想》](https://hubeiqiao.notion.site/ChatGPT-0f9698e081dc4a1ca647293ec8c783ea?pvs=4))。我从未想过自己一个人不是那么耗时的就能够做出这样的产品，这也间接说明了 Artificial General Intelligence(AGI) 将会在未来的年份里彻底革新整个社会。对于我们这样的普通人，当下最务实的建议就是在真实场景中去实际体验这些产品。这仅仅只是个开始，需要更多耐心。
