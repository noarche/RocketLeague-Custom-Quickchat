import time
import os
import pyautogui
import pygame
from random import sample
import speech_recognition as sr


main_logo = '''
 [91m_[0m[93m_[0m[92m_[0m[96m_[0m            [94m_[0m        [95m_[0m   [91m_[0m                                
[93m|[0m  [92m_[0m [96m\[0m [94m_[0m[95m_[0m[91m_[0m   [93m_[0m[92m_[0m[96m_[0m[94m|[0m [95m|[0m [91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m|[0m [91m|[0m[93m_[0m[92m|[0m [96m|[0m    [94m_[0m[95m_[0m[91m_[0m  [93m_[0m[92m_[0m [96m_[0m  [94m_[0m[95m_[0m [91m_[0m [93m_[0m   [92m_[0m  [96m_[0m[94m_[0m[95m_[0m 
[91m|[0m [93m|[0m[92m_[0m[96m)[0m [94m/[0m [95m_[0m [91m\[0m [93m/[0m [92m_[0m[96m_[0m[94m|[0m [95m|[0m[91m/[0m [93m/[0m [92m_[0m [96m\[0m [94m_[0m[95m_[0m[91m|[0m [93m|[0m   [92m/[0m [96m_[0m [94m\[0m[95m/[0m [91m_[0m[93m`[0m [92m|[0m[96m/[0m [94m_[0m[95m`[0m [91m|[0m [93m|[0m [92m|[0m [96m|[0m[94m/[0m [95m_[0m [91m\[0m
[93m|[0m  [92m_[0m [96m<[0m [94m([0m[95m_[0m[91m)[0m [93m|[0m [92m([0m[96m_[0m[94m_[0m[95m|[0m   [91m<[0m  [93m_[0m[92m_[0m[96m/[0m [94m|[0m[95m_[0m[91m|[0m [93m|[0m[92m_[0m[96m_[0m[94m|[0m  [95m_[0m[91m_[0m[93m/[0m [92m([0m[96m_[0m[94m|[0m [95m|[0m [91m([0m[93m_[0m[92m|[0m [96m|[0m [94m|[0m[95m_[0m[91m|[0m [93m|[0m  [92m_[0m[96m_[0m[94m/[0m
[95m|[0m[91m_[0m[93m|[0m [92m\[0m[96m_[0m[94m\[0m[95m_[0m[91m_[0m[93m_[0m[92m/[0m [96m\[0m[94m_[0m[95m_[0m[91m_[0m[93m|[0m[92m_[0m[96m|[0m[94m\[0m[95m_[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m|[0m[95m\[0m[91m_[0m[93m_[0m[92m|[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m\[0m[96m_[0m[94m_[0m[95m_[0m[91m|[0m[93m\[0m[92m_[0m[96m_[0m[94m,[0m[95m_[0m[91m|[0m[93m\[0m[92m_[0m[96m_[0m[94m,[0m [95m|[0m[91m\[0m[93m_[0m[92m_[0m[96m,[0m[94m_[0m[95m|[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m|[0m
                                              [95m|[0m[91m_[0m[93m_[0m[92m_[0m[96m/[0m            
  [94m_[0m[95m_[0m[91m_[0m[93m_[0m          [92m_[0m                  
 [96m/[0m [94m_[0m[95m_[0m[91m_[0m[93m|[0m   [92m_[0m [96m_[0m[94m_[0m[95m_[0m[91m|[0m [93m|[0m[92m_[0m [96m_[0m[94m_[0m[95m_[0m  [91m_[0m [93m_[0m[92m_[0m [96m_[0m[94m_[0m[95m_[0m  
[91m|[0m [93m|[0m  [92m|[0m [96m|[0m [94m|[0m [95m/[0m [91m_[0m[93m_[0m[92m|[0m [96m_[0m[94m_[0m[95m/[0m [91m_[0m [93m\[0m[92m|[0m [96m'[0m[94m_[0m [95m`[0m [91m_[0m [93m\[0m 
[92m|[0m [96m|[0m[94m_[0m[95m_[0m[91m|[0m [93m|[0m[92m_[0m[96m|[0m [94m\[0m[95m_[0m[91m_[0m [93m\[0m [92m|[0m[96m|[0m [94m([0m[95m_[0m[91m)[0m [93m|[0m [92m|[0m [96m|[0m [94m|[0m [95m|[0m [91m|[0m
 [93m\[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m\[0m[93m_[0m[92m_[0m[96m,[0m[94m_[0m[95m|[0m[91m_[0m[93m_[0m[92m_[0m[96m/[0m[94m\[0m[95m_[0m[91m_[0m[93m\[0m[92m_[0m[96m_[0m[94m_[0m[95m/[0m[91m|[0m[93m_[0m[92m|[0m [96m|[0m[94m_[0m[95m|[0m [91m|[0m[93m_[0m[92m|[0m
                                   
  [96m_[0m[94m_[0m[95m_[0m        [91m_[0m      [93m_[0m        [92m_[0m           [96m_[0m   
 [94m/[0m [95m_[0m [91m\[0m [93m_[0m   [92m_[0m[96m([0m[94m_[0m[95m)[0m [91m_[0m[93m_[0m[92m_[0m[96m|[0m [94m|[0m [95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m|[0m [95m|[0m[91m_[0m[93m_[0m   [92m_[0m[96m_[0m [94m_[0m[95m|[0m [91m|[0m[93m_[0m 
[92m|[0m [96m|[0m [94m|[0m [95m|[0m [91m|[0m [93m|[0m [92m|[0m [96m|[0m[94m/[0m [95m_[0m[91m_[0m[93m|[0m [92m|[0m[96m/[0m [94m/[0m [95m_[0m[91m_[0m[93m|[0m [92m'[0m[96m_[0m [94m\[0m [95m/[0m [91m_[0m[93m`[0m [92m|[0m [96m_[0m[94m_[0m[95m|[0m
[91m|[0m [93m|[0m[92m_[0m[96m|[0m [94m|[0m [95m|[0m[91m_[0m[93m|[0m [92m|[0m [96m|[0m [94m([0m[95m_[0m[91m_[0m[93m|[0m   [92m<[0m [96m([0m[94m_[0m[95m_[0m[91m|[0m [93m|[0m [92m|[0m [96m|[0m [94m([0m[95m_[0m[91m|[0m [93m|[0m [92m|[0m[96m_[0m 
 [94m\[0m[95m_[0m[91m_[0m[93m\[0m[92m_[0m[96m\[0m[94m\[0m[95m_[0m[91m_[0m[93m,[0m[92m_[0m[96m|[0m[94m_[0m[95m|[0m[91m\[0m[93m_[0m[92m_[0m[96m_[0m[94m|[0m[95m_[0m[91m|[0m[93m\[0m[92m_[0m[96m\[0m[94m_[0m[95m_[0m[91m_[0m[93m|[0m[92m_[0m[96m|[0m [94m|[0m[95m_[0m[91m|[0m[93m\[0m[92m_[0m[96m_[0m[94m,[0m[95m_[0m[91m|[0m[93m\[0m[92m_[0m[96m_[0m[94m|[0m                                                      
          **********************
          [91mX[0m[93mB[0m[92mO[0m[96mX[0m [94mC[0m[95mO[0m[91mN[0m[93mT[0m[92mR[0m[96mO[0m[94mL[0m[95mL[0m[91mE[0m[93mR[0m [92mV[0m[96mE[0m[94mR[0m[95mS[0m[91mI[0m[93mO[0m[92mN[0m
          **********************
    https://github.com/noarche/RocketLeague-Custom-Quickchat
    
    [91mL[0m[93me[0m[92ma[0m[96mv[0m[94me[0m [95mt[0m[91mh[0m[93mi[0m[92ms[0m [96mw[0m[94mi[0m[95mn[0m[91md[0m[93mo[0m[92mw[0m [96mo[0m[94mp[0m[95me[0m[91mn[0m [93mi[0m[92mn[0m [96mt[0m[94mh[0m[95me[0m [91mb[0m[93ma[0m[92mc[0m[96mk[0m[94mg[0m[95mr[0m[91mo[0m[93mu[0m[92mn[0m[96md[0m[94m.[0m [95mU[0m[91ms[0m[93me[0m [92mC[0m[96mT[0m[94mR[0m[95mL[0m[91m+[0m[93mC[0m [92mt[0m[96mo[0m [94me[0m[95mx[0m[91mi[0m[93mt[0m[92m.[0m
    [91mT[0m[93mh[0m[92mi[0m[96ms[0m [94mw[0m[95mo[0m[91mr[0m[93mk[0m[92ms[0m [96mb[0m[94me[0m[95ms[0m[91mt[0m [93mw[0m[92mi[0m[96mt[0m[94mh[0m [95mX[0m[91mB[0m[93mO[0m[92mX[0m [96mO[0m[94mN[0m[95mE[0m [91mC[0m[93mo[0m[92mn[0m[96mt[0m[94mr[0m[95mo[0m[91ml[0m[93ml[0m[92me[0m[96mr[0m[94ms[0m [95mc[0m[91mo[0m[93mn[0m[92mn[0m[96me[0m[94mc[0m[95mt[0m[91me[0m[93md[0m [92mt[0m[96mo[0m [94mP[0m[95mC[0m[91m.[0m
    \033[95mDeveloper Discord: @00001337\033[0m
    
    \033[92mTip or donate for faster development:\033[0m
    \033[94m(BTC) address bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j
    \033[94m(ETH) address 0x94FcBab18E4c0b2FAf5050c0c11E056893134266
    \033[94m(LTC) address ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx


'''
print("\033[95m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print("\033[94m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print("\033[95m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print("\033[94m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print(main_logo)
print("\033[94m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print("\033[95m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print("\033[94m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")
print("\033[95m°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°\033[0m")


print("\033[91m\n\nWaiting for controller connection...\033[0m")

# -------------------------------------------    Go to the "edit" section below to edit quickchats, macros, etc.    -----------------------------------------------------------



# Create your own word variations and format them like this (see examples on how to use them in the "edit" section below)

variations = {
    'thanks': [
        "Thanks a Million!",
        "Appreciate Your Support!",
        "Big Thanks To You!",
        "Appreciate It",
        "Thanks a Bunch!",
        "O Happy Day!",
        "Much Appreciated!",
        "Many Many Thanks!",
        "Thanks Forever Much!",
        "Thanks 2 Ton!",
        "Gracias!",
        "Clutch!",
        "Many Thanks, Indeed!",
        "Big Thanks, Friend!",
        "Appreciate Your Kindness!",
        "Thank You Kindly!",
        "Thanks a Gazillion!",
        "Thanks Three Million Times!",
        "Cheers, Much Appreciated!",
        "Cheers!",
        "Many Thanks!",
        "Appreciate It!",
        "Your kindness doesn't go unnoticed!",
        "Your play doesn't go unnoticed!",
        "Bless your game!",
        "Thanks for the assist.",
        "Big Thanks!",
        "Thank you, I Appreciate It!",
        "Cheers!",
        "You're too kind!",
        "I'm flattered!",
        "You're so sweet!",
        "So kind of you, thank you!",
        "Thanks, you're too generous!",
        "Thanks for making my day brighter!",
        "Thanks, that really made my day!",
        "Thanks For The Big Encouragement!",
        "Im Honored, Many Thanks!",
        "Thats really nice of you, thank you!",
        "Consider me eternally grateful, like a vampire with a lifetime supply of blood bags.",
        "I'll be forever in your debt, like a character in a loan shark's novel.",
        "Superior Teamwork! Thanks",
        "You're amazing, thank you!",
        "I am profoundly grateful.",
        "Thank you profusely.",
        "I owe you a debt of gratitude.",
        "Your kindness is appreciated immensely.",
        "I am eternally grateful.",
        "My gratitude knows no bounds.",
        "I am indebted to you.",
        "Your generosity is commendable.",
        "I am obliged to you.",
        "I am in your debt.",
        "Your assistance is invaluable.",
        "I am deeply appreciative.",
        "Your support means the world.",
        "I can't thank you enough!",
        "I owe you one, thanks!",
        "You've been incredibly kind, thank you!",
        "I'm truly thankful for your help!",
        "I'm deeply thankful!",
        "You've made my day, thanks!",
        "I'm overwhelmed with gratitude, thank you!",
        "You're a lifesaver, thank you!",
        "Thanks from the bottom of my heart!",
        "Thank you so much!",
        "What a joyful day!",
        "Today is simply wonderful!",
        "Thanks!"
    ],
    'staypositive': [
        "Stay optimistic.",
        "Don't lose hope.",
        "Keep believing.",
        "Hang in there.",
        "Stay positive.",
        "Consider this feedback as a stepping stone to greatness",
        "Embrace these suggestions as the secret ingredients to elevate your performance to the next level.",
        "Think of this feedback as a compass guiding you towards the peak of your potential.",
        "Consider these suggestions as the missing pieces of the puzzle that will complete your picture of success.",
        "Consider these suggestions as the finishing touches that will elevate your work to a whole new level of excellence.",
        "Think of this feedback as the final brushstrokes that will transform your canvas into a masterpiece.",
        "Keep your chin up.",
        "Remain hopeful.",
        "Don't give up.",
        "Keep the hope alive.",
        "Hold onto hope.",
        "Stay encouraged.",
        "Keep the dream alive.",
        "Stay upbeat.",
        "Keep the optimism flowing.",
        "Hold onto optimism.",
        "Keep the spark alive.",
        "Stay resilient.",
        "Keep the light shining.",
        "Embrace the chaos and find your inner calm.",
        "Embrace the unknown, for therein lies adventure.",
        "Today's struggle is tomorrow's strength.",
        "Every setback is a setup for a comeback.",
        "Shine bright, even on the darkest days.",
        "Be the reason someone smiles today.",
        "Find beauty in the journey, not just the destination.",
        "Your potential is limitless; believe it, achieve it.",
        "Embrace the journey of self-discovery with open arms.",
        "The smallest steps lead to the greatest accomplishments.",
        "Believe in yourself, even when nobody else does.",
        "The difference between who you are and who you want to be is what you do.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Your time is now. Seize the day and make it yours.",
        "Embrace challenges as opportunities for growth and greatness.",
        "Every accomplishment starts with the decision to try.",
        "The only way to do great work is to love what you do.",
        "Dream big, work hard, stay focused, and surround yourself with good people.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "You are the architect of your destiny; build it with purpose.",
        "Success is not determined by how many times you fall, but by how many times you rise.",
        "We'll bounce back, Stay confident",
        "Shake it off, Keep your head up.",
        "We've faced tougher challenges, Believe in the comeback.",
        "It's just a goal.",
        "Stay focused.",
        "Happiness is not a destination, but a journey of gratitude.",
        "Success is not measured by wealth, but by the impact we leave on others.",
        "In the end, we only regret the chances we didn't take.",
        "True strength lies not in brute force, but in resilience and adaptability.",
        "The greatest wisdom often comes from the silence of listening.",
        "Life is too short to dwell on the opinions of others; follow your own path.",
        "Kindness is a language that everyone understands; speak it often.",
        "Forgiveness is not a sign of weakness, but of strength and liberation.",
        "In the storm of life, find peace in the calm within yourself.",
        "The quality of our thoughts determines the quality of our lives.",
        "Success is not avoiding failure but learning from it and persevering.",
        "The beauty of simplicity often hides in the complexity of understanding.",
        "The journey of self-discovery begins with self-acceptance.",
        "We find true wealth not in possessions, but in the richness of our experiences.",
        "The power of love transcends all boundaries and transforms lives.",
        "The greatest wisdom often lies in admitting what we do not know.",
        "Time is our most precious commodity; spend it wisely.",
        "The seeds of success are sown in the soil of hard work and dedication.",
        "The strongest bonds are forged in the fires of adversity.",
        "The art of happiness lies in finding joy in the present moment.",
        "The path to enlightenment is paved with self-awareness and compassion.",
        "Life's greatest treasures are often found in the most unexpected places.",
        "The pursuit of perfection is a journey with no end; embrace imperfection and find beauty in the flaws.",
        "The key to unlocking the mysteries of the universe lies within the depths of our own consciousness.",
        "In the dance of life, the music is within you; listen and follow your rhythm.",
        "Patience is not the ability to wait, but the ability to keep a positive attitude while waiting.",
        "The smallest act of kindness can ignite the brightest light in the darkest of times.",
        "Cultural differences invite us to question our own beliefs and biases.",
        "The existence of consciousness prompts questions about the nature of existence itself.",
        "The fragility of time and mortality encourages reflection on how we spend our days.",
        "Ethical dilemmas force us to examine our values and principles.",
        "Laughter is contagious and can boost your immune system.",
        "Random acts of kindness, no matter how small, have a ripple effect of positivity.",
        "Live with intention, not reaction.",
        "Forgive freely, for resentment only poisons the soul.",
        "The ego is the greatest obstacle to enlightenment.",
        "Find joy in simplicity and contentment in abundance.",
        "May all beings be happy, may all beings be free from suffering.",
        "The journey to wisdom begins with the humility to acknowledge that there is always more to learn.",
        "True understanding arises from observing without judgment and listening without interruption.",
        "The mind is a vast landscape; tend to it like a gardener, cultivating seeds of compassion and wisdom.",
        "In the silence between thoughts lies the gateway to profound insight.",
        "Gratitude is the currency of the wise; cherish each moment as a precious gift.",
        "The path to enlightenment is not a destination but a perpetual journey of self-discovery.",
        "Seek not to possess knowledge, but to embody wisdom through compassionate action.",
        "The greatest teacher is life itself; pay attention to its lessons, for they are abundant and profound.",
        "Remember, the journey is as important as the destination.",
        "In the depths of silence, discover the vastness of your inner being.",
        "The greatest wealth lies in contentment with what is.",
        "Find liberation in letting go of the need to control.",
        "Silence speaks volumes in the language of the soul.",
        "Each step on the journey is a sacred dance with existence.",
        "Release the burden of judgment and embrace acceptance.",
        "The answer lies not in seeking, but in being.",
        "Cultivate a mind like clear water, reflecting truth without distortion.",
        "Find harmony in the balance between action and stillness.",
        "Trust in the natural rhythm of life's cycles.",
        "The path to enlightenment begins with self-awareness.",
        "With each breath, find peace in the present moment.",
        "Let go of attachment and embrace the flow of impermanence.",
        "In stillness, find the wisdom of the universe.",
        "The present moment is all we truly have.",
        "Compassion is the purest form of love.",
        "Find peace within, and you will find peace in the world.",
        "Let go of attachments, for they are the root of suffering.",
        "Seek wisdom in silence and stillness.",
        "Every action is an opportunity for mindful awareness.",
        "True freedom comes from mastering the mind.",
        "Plenty of game left, make it count.",
        "Stay determined, it's not over yet.",
        "We're still in this, Stay resilient.",
        "Don't let up now, we're still in this.",
        "It's not over, keep fighting.",
        "We're still in this fight, Stay hungry",
        "Stay strong, Hold the line.",
        "Practice gratitude daily; it shifts your focus from lack to abundance.",
        "Remember, life is a journey, not a destination; enjoy the ride.",
        "Let go of what you cant control; focus on what you can change.",
        "Read more; its the ultimate form of time travel and knowledge acquisition.",
        "Travel often; getting lost will help you find yourself.",
        "Love fiercely; its the most powerful force in the universe.",
        "Be mindful; the present moment is where true happiness resides.",
        "Embrace change; its the only constant in life.",
        "Stay curious; life is a never-ending journey of discovery.",
        "Be resilient; setbacks are temporary roadblocks, not permanent dead-ends.",
        "Learn to forgive; holding onto grudges only poisons your own soul.",
        "Cherish friendships; they are the anchors that keep you grounded through lifes storms.",
        "Enjoy your body; use it every way you can.",
        "Be kind to your knees; youll miss them when theyre gone.",
        "Remember compliments you receive; forget the insults.",
        "Dont be reckless with other peoples hearts.",
        "Dont worry about the future.",
        "Do one thing every day that scares you.",
        "The real troubles in your life are apt to be things that never crossed your worried mind.",
        "Dont compare your journey to others; everyones path is unique.",
        "Be yourself; authenticity is magnetic.",
        "Embrace failure as a stepping stone to success.",
        "Practice gratitude daily; it changes perspectives.",
        "Take care of your physical and mental health; theyre your greatest assets.",
        "Step out of your comfort zone; growth happens there.",
        "Live in the present moment; its the only one guaranteed.",
        "Surround yourself with positive, supportive people.",
        "Prioritize experiences over possessions; memories last a lifetime.",
        "Accomplishing goals provides a sense of satisfaction and pride.",
        "Being in nature has been shown to improve mental well-being and overall happiness.",
        "Acts of kindness create joy for both the giver and receiver.",
        "Laughter releases endorphins, reducing stress and boosting mood.",
        "Keep the faith, it's not over yet.",
        "Toxic behavior can manifest in various forms, including manipulation and gaslighting.",
        "Being toxic often stems from unresolved personal issues or insecurities.",
        "Toxic individuals may exhibit jealousy and competitiveness towards others.",
        "Toxic people may struggle with empathy and lack genuine concern for others' feelings.",
        "Toxic people often engage in passive-aggressive communication tactics.",
        "Toxic people often struggle with accepting responsibility for their actions.",
        "Toxicity can hinder personal growth and development.",
        "Toxic individuals may isolate themselves or push others away due to their behavior.",
        "Toxicity can be subtle and difficult to detect initially.",
        "It's essential to set boundaries with toxic individuals to protect your mental health.",
        "Removing toxic influences from your life can lead to greater happiness and fulfillment.",
        "Every decision we make has the potential to shape our destiny.",
        "Time is a mysterious force that marches relentlessly forward.",
        "Life's greatest lessons often come from unexpected places.",
        "In the depths of the ocean lie secrets waiting to be discovered.",
        "In the vast expanse of the universe, we are but a tiny speck of dust.",
        "The pursuit of knowledge is an endless journey, fueled by desire to understand the unknown.",
        "The brain consumes a significant amount of energy, about 20% of the body's energy expenditure.",
        "The subconscious mind processes vast amounts of information, shaping our perceptions and decisions.",
        "Toxic behavior can be unlearned through self-awareness and therapy.",
        "Keep fighting, you're not alone.",
        "Keep on keeping on, because giving up is too mainstream.",
        "It's impressive how consistently average you are.",
        "Keep pushing yourself, within your limited capabilities.",
        "You're doing great, in your own peculiar way.",
        "Your perseverance is truly... something.",
        "Don't worry about excelling, just keep participating.",
        "Your dedication to average is unmatched.",
        "Your perseverance is truly... something.",
    ],
    'facts': [
        "Historical events raise questions about the cyclical nature of human behavior and societal progress.",
        "Tell your momma I said to follow and friend on snap, twitter, telegram, kik.",
        "The mysteries of the human brain compel us to explore the depths of our own minds.",
        "The concept of infinity stretches the limits of our comprehension.",
        "Scientific discoveries, such as quantum entanglement, raise questions about interconnectedness and non-locality.",
        "The concept of free will prompts debate about the extent of our control over our own destinies.",
        "Moral dilemmas challenge us to weigh the consequences of our actions.",
        "The origins of the universe spark curiosity about what existed before the Big Bang.",
        "The phenomenon of deja vu raises intriguing questions about memory and perception.",
        "The fastest speed in a jet-propelled go-kart is 112.29 mph.",
        "A man named David Adamovich holds the record for the most whip cracks in one minute, with 278 cracks.",
        "The oldest known message in a bottle was found in 2018, dating back to 1886.",
        "In 2013, scientists discovered a cave in Vietnam so large it has its own river and jungle.",
        "A man named Graham Barker collected his belly button lint every day for 26 years.",
        "The worlds largest rubber band ball weighs over 9,000 pounds.",
        "I can hear voices in my head, but they're not real. They're just thoughts that sound like people talking.",
        "Whenever I see a clock or watch, time seems to slow down and speed up at the same time.",
        "The other day, I was walking down the street.",
        "The longest officially recorded marriage lasted 86 years.",
        "The worlds largest collection of garden gnomes is over 8,000 located in UK.",
        "A man named Steve Gatorwolf holds the record for the largest collection of vacuum cleaners.",
        "The worlds first speeding ticket was issued in 1902 in Ohio, for driving 12mph in an 8mph zone.",
        "The first car was invented in 1885 by Karl Benz",
        "The most popular car model ever sold is the Toyota Corolla, with over 44 million units sold worldwide.",
        "The first car radio was invented in 1929 by Paul Galvin.",
        "The worlds first traffic light wasin Ohio in 1914.",
        "The longest traffic jam in history occurred in China in 2010, stretching over 60 miles and lasting for 12 days.",
        "The average American spends about 38 hours a year stuck in traffic.",
        "The Lamborghini company started as a tractor manufacturer before venturing into sports cars.",
        "The Porsche 911 has been in production since 1964, one of the oldest sports cars in production.",
        "The Toyota Prius, introduced in 1997, was the worlds first mass-produced hybrid car.",
        "The first electric car was built in the 1830s by Scottish inventor Robert Anderson.",
        "The average car in the United States is parked about 95% of the time.",
        "The majority of Earths volcanic activity occurs underwater.",
        "Underwater archaeologists have discovered ancient submerged cities.",
        "Less than 5% of the Earths oceans have been explored.",
        "Velcro was inspired by burrs sticking to a dogs fur.",
        "Potato chips were invented by a chef who was irritated by a customer complaining that his fries were too thick.",
        "Bubble wrap was originally invented to be used as textured wallpaper.",
        "Play-Doh was initially invented as a wallpaper cleaner.",
        "Coca-Cola was originally green in color.",
        "The electric chair was invented by a dentist.",
        "Maine is the closest U.S. state to Africa.",
        "Honeybees can recognize human faces.",
        "Rogue Waves are unusually large and powerful waves that can suddenly appear, often catching beachgoers by surprise.",
        "The worlds whitest sand beach is Hyams Beach in Jervis Bay, Australia.",
        "Some beaches are known for their unique features, such as bioluminescent plankton that glow in the dark when disturbed.",
        "Beaches cover about 71% of the Earths surface, making them the most common type of shoreline.",
        "Carry a whistle, flashlight, and emergency signaling device for use in case of emergencies.",
        "The most remote national park in the United States is Gates of the Arctic National Park.",
        "The largest national park in the world is Northeast Greenland National Park.",
        "The greatest snowfall in a single storm occurred in Italy when 256 cm of snow fell in just 18 hours.",
        "The longest lightning bolt ever recorded stretched for 321 kilometers.",
        "The highest wind speed ever recorded on Earth was 231 miles per hour in Austrailia.",
        "The most rainfall in a single day occurred in France where 182.5 cm of rain fell in 24 hours.",
        "The lowest temperature ever recorded on Earth was -89.2 degrees Celsius",
        "The highest temperature ever recorded on Earth was 56.7  degrees Celsius",
        "The Great Wall of China is not visible from space with the naked eye.",
        "Theres a secret apartment at the top of the Eiffel Tower.",
        "Theres a town in Norway called Hell, and it freezes over during winter.",
        "Lake Hillier is bright pink due to the presence of algae and bacteria that thrive in its high-salinity environment.",
        "The toothbrush as we know it today was invented in 1938.",
        "The invention of modern soap is attributed to the Babylonians around 2800 BC.",
        "The first toothpaste was used by the ancient Egyptians over 5,000 years ago.",
        "The concept of personal hygiene has been recognized since ancient times.",
        "Dark matter and dark energy make up the majority of the universes mass-energy content",
        "The Sun is a relatively average-sized star, but its still incredibly large.",
        "A teaspoon of neutron star material would weigh about a billion tons on Earth",
        "The universe is estimated to be about 13.8 billion years old.",
        "Humans are the only animals capable of blushing.",
        "The strongest muscle in the human body relative to its size is the masseter.",
        "The human body produces about one liter of saliva per day.",
        "Humans are the only animals capable of shedding emotional tears.",
        "The human eye is capable of discerning approximately 10 million dif colors",
        "Your nose can remember 50,000 different scents.",
        "The Amazon Rainforest produces more than 20% of the worlds oxygen.",
        "The peacock mantis shrimp has one of the most complex visual systems in the animal kingdom.",
        "The Dark Triad traits are believed to have evolutionary roots.",
        "Dark Triad refers to 3 personality traits: Machiavellianism, narcissism, and psychopathy.",
        "Gravity is a fundamental force that shapes the universe.",
        "The universe is governed by fundamental laws of physics.",
        "Summer storms, including thunderstorms and hurricanes, are common in certain areas.",
        "Venus is the only planet in our solar system that rotates clockwise.",
        "The worlds largest beaver dam is located in Alberta Canada.",
        "Lake Maracaibo that experiences more lightning than any other place on Earth.",
        "Archaeologists have found pots of honey in tombs over 3,000 yrs old still perfectly edible.",
        "In ancient Egypt, servants were smeared with honey to attract flies away from the pharaoh.",
        "The Eiffel Tower can be 15 cm taller during the summer months due to thermal expansion. ",
        "Octopuses have three hearts.",
        "The worlds largest desert is not the Sahara but Antarctica.",
        "In botanical terms, Bananas are berries, while strawberries are not."
    ],
    'compliment': [
        "Stellar!",
        "Bravo!",
        "POG",
        "WHOMP WHOMP WAHH!",
        "Nailed it, well played!",
        "Incredible shot, truly impressive!",
        "Outstanding performance, surpassed expectations!",
        "Well done, a rockstar!",
        "Impressive shot truly talented!",
        "Excellent shot, knocked it out!",
        "Terrific Shot - Inspirational Precision!",
        "Amazing shot - Simply Phenomenal!",
        "Outstanding shot - You are the one!",
        "Brilliant shot - Truly Outstanding!",
        "The net might need some extinguishing after that!",
        "Just raised the temperature on the scoreboard!",
        "Phenomenal Shot - Absolutly Remarkable!",
        "Cant Touch This",
        "Hammer-Time",
        "Cant Stop Wont Stop",
        "Careful - Someone just got Burnt!",
        "Thats called the Scorcher!",
        "Crispy!",
        "Whoa!",
        "Perfection!",
        "Super Shot!",
        "Impressive Shot!",
        "Superb!",
        "Superior Skills, Super Shot!",
        "Nice!",
        "Nice Shot!",
        "Beautiful shot, nice one!",
        "Perfect timing, well done!",
        "That's how it's done, well played!",
        "Nice one, great execution!",
        "Well played, top performance!",
        "Excellent play, well done!",
        "Fantastic shot, well played!",
        "What a Goal!",
        "Smooth Shot!",
        "Nailed it!",
        "Impressive play, well done!",
        "Terrific play, well done!",
        "Unbelievable! You nailed it!",
        "Incredible! Great job.",
        "Amazing!",
        "Incredible!",
        "Fantastic!",
        "Epic! Well done.",
        "Stunning! That was perfect.",
        "That was pure gold!",
        "Good as gold!",
        "Outstanding move, well played!",
        "Bloody brilliant, fantastic play!",
        "Incredible shot, well done!",
        "Absolutely fantastic, well done!",
        "Amazing play, well done!",
        "Brilliant move, well played!",
        "Stellar performance, well done!",
        "Sensational shot, fantastic!",
        "Hit Was Spot On!",
        "Your acumen is truly impressive.",
        "That was a masterful display of your abilities.",
        "Your ingenuity is truly commendable.",
        "Your performance was nothing short of exceptional.",
        "Your work demonstrates a remarkable degree of sophistication. ",
        "Your analysis was both incisive and astute.",
        "That was a truly inspired piece of work. ",
        "You have an uncanny ability to grasp complex concepts.",
        "Your eloquence is truly captivating.",
        "You're like a magician, but with less rabbits and more awesomeness!",
        "Your talent is so blinding, I need sunglasses!",
        "That was so good, it should come with a warning label.",
        "It's getting hot in here!",
        "Perfect - Solid Contact!",
        "Terrific Point!",
        "Great aim!",
        "Awesome aim!",
        "Top-notch!",
        "Fantastic!",
        "Right on the money!",
        "That was slick!",
        "Wear Sunscreen.",
        "Dont forget to wear sunscreen.",
        "Always wear sunscreen.",
        "Brilliant!",
        "Outstanding!",
        "Spectacular!",
        "Phenomenal!",
        "Marvelous!",
        "Nice work!",
        "Great job!",
        "Well done!",
        "You Nailed It!",
        "Perfect Execution!",
        "Simply Outstanding!",
        "Exceptional performance!",
        "Brilliant job!",
        "Your skills are off the charts!",
        "You're making it look easy!",
        "You're the king of the field!",
        "That's some serious skill, buddy.",
        "Nice one, top stuff!",
        "Well done, you're a natural.",
        "Great job, you're on fire!",
        "Well played, you're a beast.",
        "That's some real talent, my friend.",
        "Your skills are almost too much to handle.",
        "I'm not sure how you do it, but keep it up.",
        "I can't believe how naturally talented you are.",
        "It's almost unfair how good you are at this.",
        "I'm not sure if I should be jealous or just impressed.",
        "You're on fire today!",
        "Splendid!",
        "You're a one-man highlight reel, pal!",
        "Amazing work!",
        "Truly exceptional!",
        "Exceptional skills!",
        "Superbly done!",
        "Remarkable Shot!",
        "Perfect Aim - Exceptional Shot!",
        "Flawless Execution - Excellent Shot!",
        "Picture-perfect Shot - Phenomenal!",
        "Masterful Shot - Brilliant Execution!",
        "Clinical Strike - Impeccable Aim!",
        "Precision Shot - Top-notch!",
        "Spot on - Brilliant Strike!",
        "Textbook Finish - Outstanding Accuracy!",
        "Remarkable play!",
        "Magnificent Shot!",
        "Superb play!",
        "Fantastic Goal!",
        "Excellent Shot!",
        "Amazing Goal!",
        "Heeeee Shoots! He SCORES!"
    ],
    'insult': [
        "You're so bad at that game, it looks like you're trying to swat flies with a fishing net.",
        "If I had to guess, I'd say you're the reason they added a tutorial.",
        "Your skills are so bad, I think you need a tutorial just to play a tutorial.",
        "Your skills are so bad, I think the game is trying to punish me for playing with you.",
        "You're not just bad at this game, you're actually making the game worse by playing it with such incompetence.",
        "You're so bad at this game, the only way to win is to cheat like you do in high school.",
        "Your skills are so bad, I think the controller is trying to kill you.",
        "Oh, don't worry, I'm sure you'll figure it out eventually.",
        "Well, at least you're trying, right?",
        "Keep up the good work, maybe one day it'll pay off.",
        "Wow, impressive effort... for you.",
        "Congratulations on almost getting it right.",
        "A for effort, but maybe aim a little higher next time.",
        "You're doing great... compared to someone who isn't.",
        "Oh, you're so close to getting it, I can almost taste it.",
        "Keep going, who knows, you might accidentally stumble upon success.",
        "Don't let anyone tell you otherwise, mediocrity suits you.",
        "It's adorable how you keep trying despite everything.",
        "WHOMP WHOMP WAHH!",
        "WHOMP WHOMP WAHH!!",
        "WHOMP WHOMP WAHH!!!",
        "WHOMP WHOMP WAHH!!!!",
        "You're so bad at this game, it looks like you're playing with your feet.",
        "Your skills are so bad, they make me question whether you have a pulse.",
        "I've seen NPCs with more personality than your gameplay. Do you need cheat codes for charisma?",
        "Playing with you is like watching a tutorial on How Not to Play.",
        "Impressive how consistently you can make the wrong choices.",
        "Your strategy is so outdated, even the retro games are embarrassed to have you as a player.",
        "If stupidity were a currency, you'd be the richest gamer in the world.",
        "Congratulations on leveling up in the art of failure.",
        "I didn't know button mashing was a legitimate gaming strategy until I saw you play.",
        "I've seen toddlers with better hand-eye coordination.",
        "Did you learn to play games by watching a cat try to catch a laser pointer?",
        "Your aerial skills are so non-existent, I'm pretty sure your car's tires are allergic to leaving the ground.",
        "I've seen more teamwork in a game of solitaire than in your Rocket League matches.",
        "I didn't realize Rocket League had a D.U.I. mode until I saw you play.",
        "Are you playing Rocket League or Bumper Cars for Beginners?",
        "You play like my grandma after she's had a couple glasses of wine.",
        "I've seen scarecrows with better coordination than you on the field!",
        "Watching you play is like witnessing a one-man circus act... with no talent.",
        "Did you mistake the ball for a hot potato? Because you sure drop it fast!",
        "Even the grass refuses to grow where you've been playing, probably out of embarrassment.",
        "You move slower than a sloth on tranquilizers!",
        "Wear Sunscreen.",
        "Dont forget to wear sunscreen.",
        "Always wear sunscreen."
        "Your wit is as sharp as a spoon.",
        "Just keep doing what you're doing, eventually, someone might notice.",
        "Your determination is... inspiring, in its own unique way.",
        "You're really mastering the art of almost getting it right.",
        "Keep going, I'm sure someone out there appreciates your efforts.",
        "Do you need a GPS to find the goal, or are you just allergic to scoring?",
        "You dribble like a turtle with a sprained ankle!",
        "I've seen more strategic thinking in a game of tic-tac-toe!",
        "It's like you've turned losing into an art form.",
        "Your winning streak is as elusive as a unicorn in a desert.",
        "It's like you're trying to hit a bullseye blindfolded with a spoon.",
        "You couldn't escape a paper bag if the map was drawn on the inside.",
        "Your attempts at scoring goals are as successful as a fish trying to climb a tree!",
        "If this were a puzzle, you'd be the missing piece... permanently lost.",
        "You hit the ball with such precision... it's like you're aiming for the stands.",
        "Your skills are like a bad soap opera – full of drama but lacking any real direction.",
        "I've seen toddlers with more finesse in a sandbox than you have on the field!",
        "Are you aiming for the goal or just giving the grass a gentle massage with the ball?",
        "You move on the field like a lost penguin trying to find its way back to Antarctica!",
        "You're not just bad at this game, you're actually making it worse by playing.",
        "You play like a grandma trying to text with her left hand.",
        "Your skills are so bad they make me question whether you have thumbs or not."
    ],
    'badshot': [
        "That shot was so off-target, it's probably orbiting the moon by now.",
        "I've seen better accuracy from a blindfolded archer.",
        "Next time, try aiming for the net.",
        "Well, it seems the goal moved unexpectedly. Or maybe it's just your aim.",
        "Even the wind couldn't be bothered to assist your shot – it took one look and went on vacation.",
        "If hitting the moon was your goal, consider it a celestial bullseye.",
        "That ball must have been allergic to the goal, given how desperately it avoided it.",
        "Is your GPS broken? Because you seem to have missed the goal by a mile."
    ],
    'excuse': [
        "The goalpost moved. I swear.",
        "I was testing the aerodynamics of the ball.",
        "I was conserving energy for the victory dance.",
        "Well, it seems the goal moved unexpectedly.",
        "The sun was in my eyes... ",
        "I was trying to set up a dramatic comeback narrative for the team.",
        "I decided to let the goalie feel useful for a change.",
        "I was recalibrating my GPS to locate the actual goal.",
        "My skills are so advanced the game can't keep up!",
        "I was conserving my scoring prowess for the after-match celebrations.",
        "I was trying to prove a point that goals are just a social construct.",
        "I was too busy contemplating the meaning of life, goals seemed trivial in comparison.",
        "I figured scoring was overrated, wanted to keep the suspense alive.",
        "I was aiming for the stands, thought they could use a souvenir.",
        "A team of professional comedians were performing, I was too busy laughing to defend.",
        "I was giving the ball a chance to socialize with the sideline.",
        "I was under the impression we were playing reverse soccer.",
        "A swarm of butterflies was distracting me.",
        "A naked woman suddenly burst into my room and demanded my attention!",
        "A naked woman walked in and asked me to help her escape from her captors!",
        "I was so focused on my latest podcast that I completely forgot about the hole in the wall!",
        "I was distracted by the beauty of your wheels, momentarily forgetting the goal.",
        "I was demonstrating the importance of sportsmanship by giving the opposition a sense of false hope.",
        "A flock of seagulls distracted me."
    ],
    'obvious': [
        "Oh wow, congratulations on your extraordinary ability to state the painfully obvious.",
        "You must be the Einstein of stating the blatantly apparent.",
        "Your knack for pointing out the sky is blue is truly awe-inspiring.",
        "It's a real gift you have there, enlightening us with your groundbreaking revelations.",
        "Astounding! You've mastered the art of stating the obvious with such finesse.",
        "Please, tell me more about the revolutionary concept of water being wet.",
        "Your expertise in stating what's already common knowledge is unmatched.",
        "Your ability to state the obvious is truly awe-inspiring.",
        "Please enlighten us all with more of your groundbreaking insights.",
        "How original. I've never heard that one before.",
        "You must be a true genius to come up with such profound observations.",
        "Your talent for stating things that everyone already knows is truly remarkable.",
        "Thanks for sharing your unparalleled wisdom with us mere mortals.",
        "Aren't you just a fountain of endless wit and charm?",
        "You must be a real expert in stating the obvious.",
        "I'm on the edge of my seat waiting for your next profound revelation.",
        "Bravo! You've reached new heights in the field of stating the utterly predictable.",
        "Oh, the sheer brilliance of your talent for stating the mundane. Truly, I'm in awe.",
        "Thank you, Captain Obvious, for gracing us with your unsurpassed insight once again.",
        "Alert the Nobel committee! We've found someone who can state the sunrise happens in the morning.",
        "You must be the Sherlock Holmes of stating what's already glaringly evident.",
        "Oh, please, share more of your profound wisdom about the grass being green.",
        "Wow, I'm floored by your ability to tell us the sky is above us. Truly groundbreaking.",
        "Your talent for stating the self-evident is rivaled only by a parrot repeating phrases.",
        "I bow to your unparalleled skill in stating things that even rocks could figure out.",
        "I'm in awe of your ability to state the obvious as if it were breaking news.",
        "Hold onto your seats, folks! We've got a genius here who knows the sky is blue.",
        "Your talent for stating the obvious should be preserved for future generations.",
        "Step aside, Newton! We've found our own genius who knows that apples fall from trees.",
        "Thank you, Captain Obvious, your insight knows no bounds.",
        "And here I was, living in ignorance until you enlightened me with your profound observation.",
        "Alert the press! We have a modern-day Einstein in our midst.",
        "Oh, you're good! Did you figure that out all by yourself?",
        "In other news, water is wet and the sky is blue. Keep the revelations coming!",
        "Don't hurt yourself with the mental gymnastics required to state such groundbreaking facts."
    ],
    'kicker': [
        "I got it!",
        "KICKING!",
        "GOT IT!",
        "I'm taking the kickoff!",
        "I'll handle the kickoff!",
        "Kickoff's mine, I'm on it!",
        "I'll lead the kickoff charge!",
        "Let me handle the kickoff!",
        "I'm going for the ball!",
        "Making a play for the ball!",
        "I'll initiate the kickoff!",
        "I'm stepping up for the kickoff!",
        "I'll start us off with the kickoff!",
        "Kickoff's mine, here I go!",
        "I'm going in for the kickoff!",
        "I'll get us started with the kickoff!",
        "I'm taking the lead on the kickoff!",
        "Charging towards the ball!",
        "Going all out for the ball!",
        "Making a dash for possession!",
        "Eyeing the ball, ready to seize it!",
        "Going in for the challenge!",
        "Setting my sights on the ball!",
        "Determined to win the ball!",
        "Going for it!"
    ],
    'goalie': [
        "Defending!",
        "I'll Defend!",
        "I'll protect our goal!",
        "I'll focus on defense!",
        "I'm defending our territory!",
        "I'll guard our goal!",
        "I'll stay back and defend!",
        "Defense is my responsibility!",
        "I'll take care of the defense!",
        "I'll handle the defensive end!",
        "I'll defend our goal!",
        "I'm on defense duty!",
        "I'll hold down the fort!",
        "I've got defense!",
        "I'll cover defense!",
        "I'll hang back and cover our defense",
        "I'll stay here and make sure our goal stays safe",
        "You can count on me to be back here, defending our turf.",
        "I've got our backline covered, I'll be defending.",
        "I'll be holding down the fort defensively, ready for anything.",
        "Protecting the net!",
        "Securing the goal!",
        "Guarding the posts!",
        "Maintaining a strong defensive stance!",
        "Locking down the goal!",
        "Fortifying the goal line!",
        "Standing strong in defense!",
        "Defending goal!"
    ],
    'goodpass': [
        "Perfect Pass!",
        "Amazing Pass!",
        "Solid Pass!",
        "Perfect Assist!",
        "Impressive Teamwork!",
        "Team Effort!",
        "Solid Teamwork!",
        "That was a dime!",
        "Beautiful pass!",
        "Right on the money!",
        "That was slick!",
        "What a pass!",
        "Incredible pass!",
        "Excellent Setup!",
        "Perfect Assist!",
        "Outstanding Pass!",
        "Remarkable Pass!"
    ],
    'notinuse5': [
        "",
        "",
        "",
        ""
    ],
    'notinuse3': [
        "",
        "",
        "",
        ""
    ],
    'taste': [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ]
}


# PNG images for autoclicker
#disableSafeModeButtonImage = 'dsm.png'
#cosmeticsTabImage = 'cosmetics_tab.png'
#ballTextureDropdownImage = 'ball_texture_dropdown.png'
#ballSelectionImage = 'ball_selection.png'
#xButton = 'x.png'

#autoclickAttemptsPerImage = 20

# Adjusts chat typing speed (seconds per character) ...
typingDelay = .006          # 0 makes chats type out instantly (but will cut off long chats)
                            # .001 will allow long chats (but occasionally goes too fast for RL, causing typos)
                            # .002 seems to be slow enough for the RL chat box to reliably keep up (no typos)

# Time interval between spammed chats (0.2 seconds).... change as you please
chatSpamInterval = .4

# Time window given to read button sequence macros (1.1 seconds).... you can change this as you please
macroTimeWindow = 0.8

# Edit these if necessary
chatKeys = {
    'lobby': 't',
    'team': 'y',
    'party': 'u'
}

# Xbox 360 controller button mappings for pygame.... these may be incorrect because I dont own an Xbox controller  (refer to https://www.pygame.org/docs/ref/joystick.html)
buttons = {
    'a': 0,
    'b': 1,
    'x': 2,
    'y': 3,
    'LB': 4,
    'RB': 5,
    'back': 6, 
    'start': 7,
    'RS2': 9,
    'LS2': 8,
    'up': (0, 1), 
    'down': (0, -1), 
    'left': (-1, 0), 
    'right': (1, 0) 
}

firstButtonPressed = {
    'button': None,
    'time': 420
}

macrosOn = True

# Triggers on simultaneous button/hat presses
def combine(button1, button2):
    if type(buttonPressed) is list:
        button1Value = buttons[button1]
        button2Value = buttons[button2]
        if (button1Value in buttonPressed) and (button2Value in buttonPressed):
            return True
        else: return False
    else: return False

# Triggers on successive button/hat presses (buttons pressed in a specific order)
def sequence(button1, button2):
    if not type(buttonPressed) is list:
        global firstButtonPressed
        functionCallTime = time.time()
        if firstButtonPressed['button'] == None:
            if buttonPressed == buttons[button1]:
                firstButtonPressed['time'] = functionCallTime
                firstButtonPressed['button'] = button1
                return False
            else: return False
        else:
            if functionCallTime > (firstButtonPressed['time'] + macroTimeWindow):
                if buttonPressed == buttons[button1]:
                    firstButtonPressed['time'] = functionCallTime
                    firstButtonPressed['button'] = button1
                    return False
                else:
                    resetFirstButtonPressed()
                    return False
            else:
                if buttonPressed == buttons[button2]:
                    if button1 == firstButtonPressed['button']:
                        if (functionCallTime > (firstButtonPressed['time'] + 0.05)):
                            resetFirstButtonPressed()
                            return True
                        else: return False
                    else: return False   
                else: return False
    else: return False

# Reads button presses
def detectButtonPressed():
    for key in buttons:
        buttonVal = buttons[key]
        if controllerHasHats:
            if buttonPressedIsHat:
                if type(buttonVal) is tuple:
                    if controller.get_hat(0) == buttonVal:
                        for otherKey in buttons:
                            if not (otherKey == key):
                                otherButtonVal = buttons[otherKey]
                                if type(otherButtonVal) is tuple:
                                    if controller.get_hat(0) == otherButtonVal:
                                        return [buttonVal, otherButtonVal]
                                else:
                                    if controller.get_button(otherButtonVal):
                                        return [buttonVal, otherButtonVal]
                        return buttonVal
                    else: continue
                else: continue
            else:
                if type(buttonVal) is int:
                    if controller.get_button(buttonVal):
                        for otherKey in buttons:
                            if not (otherKey == key):
                                otherButtonVal = buttons[otherKey]
                                if type(otherButtonVal) is tuple:
                                    if controller.get_hat(0) == otherButtonVal:
                                        return [buttonVal, otherButtonVal]
                                else:
                                    if controller.get_button(otherButtonVal):
                                        return [buttonVal, otherButtonVal]
                        return buttonVal
                    else: continue
                else: continue
        else:
            if not type(buttonVal) is tuple:
                if controller.get_button(buttonVal):
                    for otherKey in buttons:
                        if not (otherKey == key):
                            otherButtonVal = buttons[otherKey]
                            if not type(otherButtonVal) is tuple:
                                if controller.get_button(otherButtonVal):
                                    return [buttonVal, otherButtonVal]                                    
                    return buttonVal
    return None 

def resetFirstButtonPressed():
    firstButtonPressed['button'] = None     
    firstButtonPressed['time'] = 420

def checkIfPressedButtonIsHat(event):
    if event.type == pygame.JOYHATMOTION:
        return True
    else: return False

def quickchat(thing, chatMode='lobby', spamCount=1):
    if not thing: 
        print('quickchat failed.. (there was nothing to quickchat)\n')
        return
    try:
        for i in range(spamCount):
            pyautogui.press(chatKeys[chatMode])
            pyautogui.write(thing, interval=typingDelay)
            pyautogui.press('enter')
            print(f'[{chatMode}]    {thing}\n')
            time.sleep(chatSpamInterval)
    except Exception as e:
        print(e)

def toggleMacros(button):
    global macrosOn
    if not type(buttonPressed) is list:
        buttonValue = buttons[button]
        if buttonValue == buttonPressed:
            macrosOn = not macrosOn
            if macrosOn:
                print('\033[32m°°°·.°·..·°¯°·._.· Macros Toggled ON ·._.·°¯°·.·° .·°°°\n\033[0m')
            else:
                print('\033[31m°°°·.°·..·°¯°·._.· Macros Toggled OFF ·._.·°¯°·.·° .·°°°\n\033[0m')
            time.sleep(.2)

def shuffleVariations(key=''):
    if not (key == ''):
         lastWordUsed = shuffledVariations[key]['randomizedList'][len(variations[key]) - 1]
         secondLastWordUsed = shuffledVariations[key]['randomizedList'][len(variations[key]) - 2]
         while True:
            shuffledList = sample(variations[key], len(variations[key]))
            if not (shuffledList[0] == lastWordUsed) and (shuffledList[1] == secondLastWordUsed):
                shuffledVariations[key]['randomizedList'] = shuffledList
                shuffledVariations[key]['nextUsableIndex'] = 0
                break
    else:
        for key in variations:
            shuffledVariations[key] = {
                'randomizedList': sample(variations[key], len(variations[key])),
                'nextUsableIndex': 0
            }

def variation(key):
    global shuffledVariations
    index = shuffledVariations[key]['nextUsableIndex']
    if not len(variations[key]) > 2:
        print(f'The "{key}" variation list has less than 3 items..... it cannot be used properly!! Please add more items (words/phrases)')
        return '-- "' + key + '" variation list needs more items --'
    else:
        if index < (len(variations[key])):
            randWord = shuffledVariations[key]['randomizedList'][index]
            shuffledVariations[key]['nextUsableIndex'] += 1
            return randWord
        else:
            shuffleVariations(key)
            randWord = shuffledVariations[key]['randomizedList'][0]
            shuffledVariations[key]['nextUsableIndex'] += 1
            return randWord

#def speechToText(microphone):
#    try:
#        with microphone as source:
#            print('speak now...\n')
#            audio = r.listen(source, timeout=5)
#    except sr.WaitTimeoutError:
#        print(' -- Listening timed out while waiting for phrase to start -- (you didnt speak within 5s, or your mic is muted)')
#        return None
#    startInterpretationTime = time.time()
#    response = {
#        "success": True,
#        "error": None,
#        "transcription": 'my speech recognition failed :(',
#        "interpretation time": None
#    }
#    try:
#        response["transcription"] = r.recognize_google(audio)
#        response["interpretation time"] = time.time() - startInterpretationTime
#        print(f'({round(response["interpretation time"], 2)}s interpretation)\n')
#    except sr.RequestError:
#        # API was unreachable or unresponsive
#        response["success"] = False
#        response["error"] = "API unavailable"
#        print(response)
#    except sr.UnknownValueError:
#        # speech was unintelligible
#        response["error"] = "Unable to recognize speech"
#        print(response)
#    except Exception as e:
#        print(e)
#        return
#    return response['transcription'].lower()
#
#def clickThing(image, confidence=0.9, grayscale=True, region=None):
#    noRegion = not region
#    lastResort = round(0.6 * autoclickAttemptsPerImage) # last resort will start after 60% of attempts have failed
#    for i in range(autoclickAttemptsPerImage):
#        try:
#            imageCoords = pyautogui.locateCenterOnScreen(image, confidence=confidence, grayscale=grayscale) \
#                if (noRegion) else pyautogui.locateCenterOnScreen(image, confidence=confidence, grayscale=grayscale, region=region)
#            pyautogui.moveTo(imageCoords[0], imageCoords[1])
#            pyautogui.mouseDown()
#            time.sleep(.05)
#            pyautogui.mouseUp()
#            return imageCoords
#        except Exception as e:
#            print(e)
#            if (i >= lastResort and i < autoclickAttemptsPerImage - 1):
#                print(f'\n[attempt {i+1}] ... couldn\'t find "{image}" by searching entire screen (slower)')
#                noRegion = True
#            elif (i < lastResort and i < autoclickAttemptsPerImage - 1):
#                if noRegion:
#                    print(f'\n[attempt {i+1}] ... couldn\'t find "{image}" by searching entire screen (slower)')
#                else:
#                    print(f'\n[attempt {i+1}] ... couldn\'t find "{image}" in specified region')
#            else:
#                print(f'\n[attempt {i+1}] couldn\'t locate "{image}" on screen :(')
#                print(f'\nCheck this guide for a potential fix:\nhttps://github.com/smallest-cock/RL-Custom-Quickchat/#autoclicker-isnt-working-correctly\n')

#def enableBallTexture():
#    startTime = time.time()
#    time.sleep(.4)
#    pyautogui.move(50, 50)
#    try:
#        # find and click 'disable safe mode' button
#        disableSafeModeButtonCoords = clickThing(disableSafeModeButtonImage)
#        time.sleep(.2)

        # find and click cosmetics tab
        # (start searching 175px above located 'disable safe mode' button, looking in a 150px region beneath)
#        cosmeticsTabCoords = clickThing(cosmeticsTabImage, confidence=0.8, region=(0, disableSafeModeButtonCoords[1] - 175, screenWidth, 150))

        # find and click ball texture dropdown
        # (start searching 100px below located cosmetics tab, looking in a 250px region beneath)
#        dropdownCoords = clickThing(ballTextureDropdownImage, region=(0, cosmeticsTabCoords[1] + 100, screenWidth, 250))

        # find and click ball texture 
        # (start searching 15px below located dropdown menu (to avoid false positive in dropdown menu), looking in a 275px region beneath)
#        ballSelectionCoords = clickThing(ballSelectionImage, region=(0, dropdownCoords[1] + 15, screenWidth, 275))

        # find and click 'x' button to exit
        # (start searching 250px above located ball texture, looking in a 150px region beneath)
#        clickThing(xButton, region=(0, ballSelectionCoords[1] - 250, screenWidth, 150))
    
#        print(f'\n<<<<<  Enabled ball texture in {round((time.time() - startTime), 2)}s  >>>>>\n')
#    except TypeError:
#        return
#    except Exception as e:
#        print('Error:', e)

# change working directory to script directory (so .png files are easily located)
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

screenWidth, screenHeight = pyautogui.size()
pyautogui.FAILSAFE = False
shuffledVariations = variations.copy()
shuffleVariations()
pygame.init()
clock = pygame.time.Clock()
controllerHasHats = False

# speech recognition init
#r = sr.Recognizer()
#mic = sr.Microphone()
#with mic as source:
#    r.adjust_for_ambient_noise(source) # <--- adjusts mic sensitvity for background noise based on a 1s sample of mic audio

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEREMOVED:
                print('\033[94m*** Controller disconnected ***\033[0m\n')
                controller.quit()
            elif event.type == pygame.JOYDEVICEADDED:
                print('[91m°[0m[93m°[0m[92m°[0m[96m·[0m[94m.[0m[95m°[0m[91m·[0m[93m.[0m[92m.[0m[96m·[0m[94m°[0m[95m¯[0m[91m°[0m[93m·[0m[92m.[0m[96m_[0m[94mC[0m[95mo[0m[91mn[0m[93mt[0m[92mr[0m[96mo[0m[94ml[0m[95ml[0m[91me[0m[93mr[0m [92mc[0m[96mo[0m[94mn[0m[95mn[0m[91me[0m[93mc[0m[92mt[0m[96me[0m[94md[0m')
                pygame.joystick.init()
                controller = pygame.joystick.Joystick(0)
                if controller.get_numhats() > 0:
                    controllerHasHats = True
                if controller.get_init() == True:
                    print(
                        f"\n\n\033[94m~~~~~~\033[0m [91mC[0m[93mo[0m[92mn[0m[96mn[0m[94me[0m[95mc[0m[91mt[0m [93mt[0m[92mo[0m \033[92m {controller.get_name()} \033[0m [91mS[0m[93mu[0m[92mc[0m[96mc[0m[94me[0m[95ms[0m[91ms[0m[93mf[0m[92mu[0m[96ml[0m[94ml[0m[95my[0m \033[94m ~~~~~~\033[0m\n\n[91mW[0m[93ma[0m[92mi[0m[96mt[0m[94mi[0m[95mn[0m[91mg[0m [93mf[0m[92mo[0m[96mr[0m [94mQ[0m[95mu[0m[91mi[0m[93mc[0m[92mk[0m[96mc[0m[94mh[0m[95ma[0m[91mt[0m [93mI[0m[92mn[0m[96mp[0m[94mu[0m[95mt[0m[91ms[0m [93m/[0m [92mM[0m[96mo[0m[94mn[0m[95mi[0m[91mt[0m[93mo[0m[92mr[0m[96mi[0m[94mn[0m[95mg[0m [91mc[0m[93mo[0m[92mn[0m[96mt[0m[94mr[0m[95mo[0m[91ml[0m[93ml[0m[92me[0m[96mr[0m [94mf[0m[95mo[0m[91mr[0m [93mh[0m[92mo[0m[96mt[0m[94mk[0m[95me[0m[91my[0m[93ms[0m[92m.[0m[96m.[0m[94m.[0m[95m.[0m\n\n")
            elif (event.type == pygame.JOYBUTTONDOWN) or (event.type == pygame.JOYHATMOTION):
                buttonPressedIsHat = checkIfPressedButtonIsHat(event)
                buttonPressed = detectButtonPressed()

# ---------------------------------    Edit the code below to change quickchats, macros, spam amounts, chat modes, variations, etc.    --------------------------------------------------



                toggleMacros('RS2') # <-- 'RS2' is the button used to toggle on/off macros (Xbox Right Stick Press)..... change as you please

                if macrosOn:
                    

                    if combine('x', 'up'):
                        quickchat(variation('thanks'))
                        break
                    
                    if combine('x', 'down'):
                        quickchat(variation('excuse'))
                        break

                    if combine('x', 'right'):
                        quickchat(variation('goodpass'))
                        break
                    
                    elif sequence('up', 'up'):
                        quickchat(variation('compliment'))
                        break                                       
                    
                    if combine('a', 'left'):
                        quickchat(variation('facts'))
                        break
                    
                    if combine('a', 'right'):
                        quickchat(variation('staypositive'))
                        break

                    if combine('a', 'down'):
                        quickchat(variation('badshot'))
                        break
                    
                    if combine('a', 'up'):
                        quickchat(variation('obvious'))
                        break
                    
                    elif sequence('left', 'left'):
                        quickchat(variation('goalie'), chatMode='team')
                        break
                    
                    elif sequence('right', 'right'):
                        quickchat(variation('kicker'), chatMode='team')
                        break
                    
                    #elif combine('LB', 'left'): 
                        #quickchat(speechToText(mic))
                        #break

                    #elif combine('LB', 'y'):
                        #quickchat('WHOMP WHOMP WAHH!', spamCount=3)
                        #break


    except Exception as e:
        print(e)
        break

    # limit pygame refresh rate to "20 FPS" (drastically reduces CPU usage)
    clock.tick(20)
