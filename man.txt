DOCKER:
docker build -t googl2 .
docker run -p 4000:80 googl2

***takes 2 mins

FIND DOCKERNAME:
~/Documents/genai-and-democracy-2024$ docker ps
CONTAINER ID   IMAGE     COMMAND               CREATED         STATUS         PORTS                                   NAMES
7b1e1fbf9208   googl     "tail -f /dev/null"   5 minutes ago   Up 5 minutes   0.0.0.0:4000->80/tcp, :::4000->80/tcp   stoic_dewdney

***up to now all the libs are installed

RUN:
docker exec stoic_dewdney python user_inference.py --query "How many people live in London?" --query_de "myFirstQ"

Release Port:
docker stop confident_torvalds

Example:
(base) tianhao@tianhao-HP-ProBook-450-G8-Notebook-PC:~$ docker exec affectionate_antonelli python user_inference.py --query "How many people live in London?" --query_de "myFirstQ"
:) Great! We have found some results for you! And the higher the score, the more relevant the text is.
Score: 100.36144256591797, Doc: London is my country
Score: 95.31155395507812, Doc: London is known for its financial
Score: 81.38209533691406, Doc: Once upon a time, there was a little baby

UPDATE:
(base) tianhao@tianhao-HP-ProBook-450-G8-Notebook-PC:~/Documents/genai-and-democracy-2024$ python user_inference.py --query "introduction of China" --query_de "myFirstQ"
B🅱️e🇪s🇸t🇹 Seminar ever 🎉📚🎓🌟😊👍🔥💡🚀
--------------------
🔧 Setting up environment of user_inference...
🔧 Setting up environment for uese_preprocess...
📚 Transformers libraries imported successfully.
🧠 Model loaded successfully.
🔍 Handling user query...
🚀 Starting file processing...
📄 Processing file: sample5.json
✅ File processed and saved: sample5.json
📄 Processing file: sample2.json
🇩🇪 Translating from German to English...
✅ File processed and saved: sample2.json
📄 Processing file: sample3.json
✅ File processed and saved: sample3.json
📄 Processing file: sample6.json
🇩🇪 Translating from German to English...
✅ File processed and saved: sample6.json
📄 Processing file: sample0.json
🇩🇪 Translating from German to English...
✅ File processed and saved: sample0.json
📄 Processing file: sample1.json
🇫🇷 Translating from French to English...
✅ File processed and saved: sample1.json
📄 Processing file: sample4.json
✅ File processed and saved: sample4.json
🎉 All files processed successfully.
📂 Loading and processing JSON files...
✅ JSON files processed.
🎉 Great! We have found some results for you! And the higher the score, the more relevant the text is.
📄 Score: 99.75304412841797, Doc: China is a great East Asian country with a long history and rich culture. The capital is Beijing. China is known for its impressive monuments like the Great Wall and Forbidden City. The country has a diverse cuisine that varies by region, with dishes like lacquered duck and dim sum. China is also known for its technological advances and rapid economic development.
📄 Score: 96.57510375976562, Doc: China is a large country in East Asia with a long history and rich culture.
📄 Score: 86.44385528564453, Doc: The United Kingdom, often simply called the UK, is a country located in Western Europe. The capital is London. The UK is known for its rich history, monarchy, and cultural institutions like the British Museum and the National Gallery. The country has a diverse landscape, ranging from the mountains of Scotland to the beaches of the southern coast. British cuisine includes dishes like fish and chips, roast beef, and Yorkshire pudding.


