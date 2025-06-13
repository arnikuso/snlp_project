
import os

folder_path = '/Users/arina/hu-ru/thesis coding/campaign_texts/the labour party'
output_file = 'labour.txt'

total_tokens = 0

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as infile:
                text = infile.read().strip()
                tokens = len(text.split())
                total_tokens += tokens

            
                outfile.write(text + "\n\n")

print(f'total number of tokens: {total_tokens}')


