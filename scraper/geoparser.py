import subprocess

text = '''Hong Kong (CNN)Speaking on the 10th anniversary of the 2003 SARS crisis, Zhong Nanshan, one of the heroes in China's fight against that disease, described it as a \"turning point\" for the nation.
\"SARS forced the whole country to pay attention to the livelihood of the people,\" he said, before adding a warning. \"We've made huge progress, but our footsteps are slow, especially in terms of healthcare.\"
With the Wuhan coronavirus spreading across the country, killing at least 25 people so far, China is now facing a major test of just how much it has changed since 2003, both in terms of the healthcare system's ability to react to a new deadly pathogen -- and crucially, how the central government handles the developing crisis.
Speaking this week, Chinese President Xi Jinping ordered \"all-out efforts\" to contain the virus' spread and treat those affected. His intervention seemed to carry with it a clear message: the mistakes of SARS will not be repeated.
Wuhan is only the latest crisis to face Xi since he secured personal control of the Communist Party, joining the US-China trade war, ongoing anti-government unrest in Hong Kong, and the recent Taiwan election, in which Tsai Ing-wen, much loathed by Beijing, handily won reelection against a more pro-China candidate.
More than any leader since Mao Zedong, Xi has centralized power around himself. He is the state, and while this gives him immense control, it also means that every crisis is a test of his leadership -- Wuhan perhaps most of all, as the country looks to their leader for reassurance and confidence.
Since Xi's statement, efforts to control the virus have ramped up nationwide, with health authorities ordering the highest level response, typically used to tackle outbreaks of plague or cholera. On Thursday, Wuhan itself -- all 11 million people -- was partially quarantined, with public transport \"temporarily suspended,\" including all planes and trains departing the city.
In state media, editorials urged greater transparency and lauded the central government's quick response and that of Chinese scientists and doctors, who quickly released the virus' genome in order to aid the work of other researchers worldwide in coming up with a vaccine.
Despite the laudatory efforts of Chinese healthcare workers, however, and forceful statements from Beijing, allegations of an initial -- and potentially even ongoing -- cover-up continue to hang over the Wuhan outbreak.
This virus could have been China's chance to exorcise the ghosts of SARS once and for all, instead it may have exposed that, for all the progress in the past 17 years, fundamental flaws remain in place when it comes to handling a crisis like this -- ones that could result in far greater danger in future.'''

text2 = "hello"

subprocess.call(['echo', text])

cmd = ['./run', '-t plain', '-g geonames']