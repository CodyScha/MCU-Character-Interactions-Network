import os
import openai
import numpy as np

openai.api_key = os.getenv("OPENAI_API_KEY")

setup_prompt = "Find the interactions between characters from a given portion of a movie transcript. For each interaction that you find, output it as Character1, Character2 with no other details or output. Below is the transcript to analyze:\n"

movie_name = 'CaptainAmericaTFA.txt'

movie_file = open('..\Experiment Transcripts\\' + movie_name, encoding="utf-8")
movie_lines = movie_file.readlines()

chunk_size = 150

movie_chunks = [movie_lines[x:x+chunk_size] for x in range(0, len(movie_lines), chunk_size)]

# print(movie_chunks[0][10])
# exit()

output_csv = open("../Movie CSVs/2" + movie_name, 'w', encoding="utf-8")

chunk_num = 0
for chunk in movie_chunks:
    print("On Chunk #", chunk_num)

    # * Combine the chunk bits into a single string
    script_portion = ""
    for line in chunk:
        script_portion += line
    
    # print(script_portion)
    # exit()

    # * With the complete script portion, lets call the API
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": (setup_prompt + script_portion)}],
        temperature=0.5,
        max_tokens=250
    )

    # * Now that we have our response, we should write that to a file
    output_csv.write(response.choices[0].message.content)

    print("Chunk #", chunk_num, " prompt tokens: ", response.usage.prompt_tokens)
    print("Chunk #", chunk_num, " answer tokens: ", response.usage.completion_tokens)
    print("Chunk #", chunk_num, " total tokens: ", response.usage.total_tokens)
    
    chunk_num +=1


