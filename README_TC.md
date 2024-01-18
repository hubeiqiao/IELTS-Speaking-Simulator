# IELTS-Speaking-Simulator
A GPT offers an authentic practice experience, helpful for anyone preparing for IELTS.

[English Version](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/README_EN.md)

[简体中文版本](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/README.md)

## 介紹
[IELTS Speaking Simulator](https://chat.openai.com/g/g-uGueIrCsT-ielts-speaking-simulator) 是一款基於 ChatGPT 的工具，它不僅完整模擬了雅思口語考試流程，還能隨機抽取最新的題庫。對話結束後，除了提供評估外，還可以根據對話內容進行整理並改善文本。與單獨練習相比，更接近真實場景。

![IELTS Speaking Simulator](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/IELTS%20Speaking%20Simulator_Interface.jpg)

## 如何使用
1. 在 AppStore/Google Play 中下載 ChatGPT 官方應用，註冊並登入。
2. 訂閱 ChatGPT Plus。如果 iOS/Android 上無法支付，推薦使用 WildCard 一條龍服務：https://bewildcard.com/i/BEIQIAO
3. 訪問 https://chat.openai.com/g/g-uGueIrCsT-ielts-speaking-simulator
4. 選擇在 ChatGPT 中打開，選擇對應要模擬的模塊，等待腳本運行完畢，點擊右下角的耳機按鈕即可開始對話。

GPTs 是基於 GPT-4 的，因此按照目前的限制，每 3 小時可以發 40 條，也足夠一次完整的練習了。

## 使用技巧
### 對話開始
1. 確保有足夠的 GPT-4 使用額度，否則可能在練習過程中被告知達到了上限。即便真到了上限，有額度後可以再次點擊耳機按鈕繼續練習。
2. 由於在語音模式下腳本運行不太穩定，並且失敗後反覆重試會不斷消耗 GPT-4 的使用額度，截止 2024/01/18，規避手段是先在文本模式下選擇對應需要模擬的模塊「Part 1」、「Part2&Part3」或者「A Full Simulation」，等待腳本運行完成後再進入語音模式開啟語音對話。

### 對話進行中
1. 對話過程中，如果沒聽清楚問題，可以要求其再重複一遍（在真實考試中也可以這樣）。
2. 截止 2023/12/27，可以通過在輸入時長按的方式來規避對話中斷的問題。
3. Part 2 部分，實際不會在 1 分鐘準備時間到時提示你，這個自己看下時間就好了。
4. 有時候 Part 1 和 Part 3 問的問題會很少，可以重新再來一次。

### 對話結束後
1. 評估的分數作為參考就好，不要太當真。目前版本無法對發音提供詳細反饋，都是基於語音識別後的文本。
2. 在練習完成後，我會切換到電腦上，要求其針對對話的內容進行進一步的分析以及改進。我最常用的 Prompt 是：
   > Could you please organize the full, improved and detailed answer(but just match my words; do not use complex words) based on the above topic and questions? You can first organize Part 1.
    
   然後再以此改造 Part 2、Part 3。如果對改善後的文本不滿意，可以重試或者明確的指出你的需求。

### 學習途中的想法碎片
1. 我也嘗試過其他口語練習 GPTs，但往往只圍繞我熟悉的話題。雖然我沒有即刻的雅思考試需求，但我仍然覺得，使用這種具有明確標準的練習框架更為合適。
2. 同時也不需要像以前準備雅思口語一樣刻意去背誦或者套題，就當作是即時的練習就好了。遇到中文也說不清楚的話題，完成後記住框架和關鍵詞就好了。
3. 實話講，這是我用過的最好 GPTs，相比一對一口語陪練的費用，每月支付 20 美元甚至更多對我來說是物超所值的。希望在長時間的堅持練習後能夠幫助我克服對話焦慮的恐懼。當然，這只是個開始，估計明年我會再找行為面試相關的 GPTs。
4. 曾經有朋友告誡我，無論採用什麼方式，都能夠學好英語，關鍵在於能否堅持下去。如果最終要熟練使用語言的話，效率至上大概率是陷阱。這是我從上一次準備中學習到的。這是我上次寫的文章：《期望與現實：有關 ChatGPT 輔助語言學習的暴論》

## 製作過程分享
1. 我在 [附件](https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/IELTS-Speaking-Simulator_Instructrion_20231215.txt) 中附上了這個 GPT 當前的 Instructions（Python 腳本也補上了），你可以複製一份創建屬於你自己的 GPTs 以及針對性改造其中的流程或者題庫。
2. 在製作這個 GPT 時，遇到的最大困難是不知道如何讓其能夠做到隨機抽取題庫。修改測試了多次 Prompt 後都依舊做不到隨機，都是固定循環。幸運的是，在 [@goldengrape](https://twitter.com/goldengrape) 的提示下，我意識到 Knowledge 除了可以上傳文本文件外，還可以上傳 Python 腳本讓其使用 Code Interpreter 執行。若干次調試後，總算解決了問題。曾經也考慮過使用 Actions 來對接外部接口，但當前的 GPTs 一旦使用外部 Actions 後，就沒辦法在手機上用了，也就無法使用語音對話功能了。
3. 體驗的其他類似 GPT，大多都會把該 Topic 下的所有問題都扔出來。一開始我也遇到了類似問題，經過多次嘗試修改後才勉強解決問題（並不能保證完全解決，如果遇到了就重試一次吧）。
4. 附件中題庫取自雅思哥整理的 9-12 月題庫。當前 GPT 中的題庫已更新至 2024 年 1-4 月的題庫。

## 為什麼分享出來
1. 這個 GPT 只是我自己用以及探索可能性的，現在一切都還是太早了。在每天練習後，我都會不由感嘆這真是太棒了，並暗自稱讚這是目前同類中最好的 GPT。想著反正都做出來了，不如讓更多有類似需求的朋友來使用。
2. 更坦誠地講，沒什麼要隱藏的，因為通過 Prompt 技巧是可以把我的 Instructions 給拿到的（我也沒想過增加保護 Prompt，因為始終會有方式弄出來）。既然如此，不如直接公開出來給大家。
3. 產品上，現在的使用者至少有幾百位了，因此我需要更謹慎的來做改動。既然如此，不如公開分享出來，讓大家都有基於自己需求修改的可能性以及搜集大家的反饋來改進這個小工具。
4. 對話練習只是其中一個部分。我覺得同等重要的是練習後的整理。如果能夠看到大家不同的使用技巧，發現我不知道自己不知道的內容或者技巧就更好了。
5. ChatGPT 目前依舊是個大玩具。但至少從語言學習的場景看，是大有可為的。希望可以啟發相關開發者，設計出更好的產品。

---

除了這個口語 GPT 外，我也創建了閱讀和寫作的 GPTs，供參考。
- [IELTS Reading Tutor](https://chat.openai.com/g/g-vYk0G1CPU-ielts-reading-tutor): Please provide the Reading article, questions, and your thoughts or concerns, so that I can offer detailed feedback and explanations.
- [IELTS Writing Mentor](https://chat.openai.com/g/g-vG4GIq3DH-ielts-writing-mentor): Get personalized IELTS writing assistance, focusing on in-depth analysis and enhancement of both Task 1 and Task 2. Simply paste your task and essay to receive expert guidance.

---

最後，由衷的感謝 Sam 和 OpenAI([《ChatGPT 发布一周年个人随想》](https://hubeiqiao.notion.site/ChatGPT-0f9698e081dc4a1ca647293ec8c783ea?pvs=4))。我從未想過自己一個人不是那麼耗時的就能夠做出這樣的產品，這也間接說明了 Artificial General Intelligence(AGI) 將會在未來的年份裡徹底革新整個社會。對於我們這樣的普通人，當下最務實的建議就是在真實場景中去實際體驗這些產品。這僅僅只是個開始，需要更多耐心。
