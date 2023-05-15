from wordcloud import WordCloud
import matplotlib.pyplot as plt

# create a dictionary with the frequency of each keyword
keywords = ['keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5', 'keyword1', 'keyword2', 'keyword1', 'keyword3']
freq_dict = {}
for keyword in keywords:
    freq_dict[keyword] = freq_dict.get(keyword, 0) + 1

# create the word cloud object
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate_from_frequencies(freq_dict)

# plot the word cloud
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

# display the plot
plt.show() 